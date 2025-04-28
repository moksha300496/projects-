import streamlit as st
from PIL import Image
import numpy as np
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet, InvalidToken
import io

# Set page configuration
st.set_page_config(
    page_title="Steganography Dashboard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #ff3131;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff3131;
    }
    .info-box {
        background-color: #1e1e1e;
        border: 1px solid #ff3131;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: #ffffff;
    }
    .stApp {
        background-color: #0a0a0a;
    }
    h1, h2, p, .stMarkdown {
        color: #ffffff;
    }
    .css-10trblm {
        color: #ffffff;
    }
    section[data-testid="stSidebar"] {
        background-color: #1e1e1e;
        border-right: 1px solid #ff3131;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: #ffffff;
    }
    .stButton button {
        background-color: #ff3131 !important;
        color: white !important;
        border: none !important;
    }
    .stButton button:hover {
        background-color: #cc0000 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #ff3131;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-header'>Steganography Dashboard</h1>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("<h2 style='color: #ff3131;'>Navigation</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Choose Steganography Method", ["Image in Image", "Text in Image"])

# Image in Image Steganography Functions (Blowfish LSB)
IV = b'12345678'  # 8-byte IV for CBC mode

def encrypt_data_img(data, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, IV)
    return cipher.encrypt(pad(data, Blowfish.block_size))

def decrypt_data_img(encrypted_data, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, IV)
    return unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)

def resize_secret_image(secret_image, cover_image, key):
    cover_width, cover_height = cover_image.size
    max_capacity = (cover_width * cover_height * 3) // 8 - 8
    while True:
        secret_width, secret_height = secret_image.size
        secret_data = bytearray(secret_image.tobytes())
        encrypted_data = encrypt_data_img(secret_data, key)
        if len(encrypted_data) <= max_capacity:
            return secret_image
        new_width = int(secret_width * 0.85)
        new_height = int(secret_height * 0.85)
        if new_width < 10 or new_height < 10:
            raise ValueError("Secret image is too large, even after resizing!")
        secret_image = secret_image.resize((new_width, new_height))

def encode_image_steg(cover_file, secret_file, output_name, key):
    key_bytes = key.encode('utf-8')
    if not (8 <= len(key_bytes) <= 56):
        raise ValueError("Key must be between 8 and 56 bytes long!")
    
    cover_image = Image.open(cover_file)
    secret_image = Image.open(secret_file)
    secret_image = resize_secret_image(secret_image, cover_image, key_bytes)
    cover_image = cover_image.convert("RGB")
    secret_image = secret_image.convert("RGB")
    secret_data = bytearray(secret_image.tobytes())
    encrypted_data = encrypt_data_img(secret_data, key_bytes)
    encrypted_data = (len(encrypted_data).to_bytes(4, 'big') + 
                      secret_image.width.to_bytes(2, 'big') + 
                      secret_image.height.to_bytes(2, 'big') + 
                      encrypted_data)
    
    encoded_image = cover_image.copy()
    data_index = 0
    total_data_bits = len(encrypted_data) * 8
    for x in range(cover_image.width):
        for y in range(cover_image.height):
            if data_index >= total_data_bits:
                break
            r, g, b = cover_image.getpixel((x, y))
            if data_index < total_data_bits:
                r = (r & 0xFE) | ((encrypted_data[data_index // 8] >> (7 - (data_index % 8))) & 0x01)
                data_index += 1
            if data_index < total_data_bits:
                g = (g & 0xFE) | ((encrypted_data[data_index // 8] >> (7 - (data_index % 8))) & 0x01)
                data_index += 1
            if data_index < total_data_bits:
                b = (b & 0xFE) | ((encrypted_data[data_index // 8] >> (7 - (data_index % 8))) & 0x01)
                data_index += 1
            encoded_image.putpixel((x, y), (r, g, b))
    
    encoded_image.save(output_name)
    return output_name

def decode_image_steg(encoded_file, output_name, key):
    key_bytes = key.encode('utf-8')
    if not (8 <= len(key_bytes) <= 56):
        raise ValueError("Key must be between 8 and 56 bytes long!")
    
    encoded_image = Image.open(encoded_file).convert("RGB")
    bits = []
    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            r, g, b = encoded_image.getpixel((x, y))
            bits.extend([r & 0x01, g & 0x01, b & 0x01])
    
    extracted_data = bytearray()
    for i in range(0, len(bits) - 7, 8):
        byte = sum(bit << (7 - j) for j, bit in enumerate(bits[i:i+8]))
        extracted_data.append(byte)
    
    encrypted_data_length = int.from_bytes(extracted_data[:4], 'big')
    secret_width = int.from_bytes(extracted_data[4:6], 'big')
    secret_height = int.from_bytes(extracted_data[6:8], 'big')
    encrypted_data = extracted_data[8:8 + encrypted_data_length]
    
    try:
        decrypted_data = decrypt_data_img(encrypted_data, key_bytes)
        secret_image = Image.frombytes("RGB", (secret_width, secret_height), decrypted_data)
        secret_image.save(output_name)
        return output_name
    except Exception as e:
        st.error(f"Decryption error: {e} (Check if the key is correct)")
        return None

# Text in Image Steganography Functions (Fernet Binary)
def generate_key_text():
    return Fernet.generate_key()

def encrypt_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

def text_to_binary_image(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    size = int(np.ceil(np.sqrt(len(binary_data))))
    binary_image = np.zeros((size, size), dtype=np.uint8)
    for i in range(len(binary_data)):
        binary_image[i // size, i % size] = 255 if binary_data[i] == '1' else 0
    return Image.fromarray(binary_image, mode='L')

def binary_image_to_text(binary_image):
    binary_data = ''.join('1' if pixel > 128 else '0' for pixel in np.array(binary_image).flatten())
    text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return text.strip('\x00')

# Pages
if page == "Image in Image":
    st.markdown("<h2 class='sub-header'>Image in Image Steganography</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
    <p>Hide a secret image within a cover image using LSB steganography and Blowfish encryption.</p>
    <p><strong>Note:</strong> The encryption key must be 8-56 bytes long. Use the same key for encoding and decoding!</p>
    </div>
    """, unsafe_allow_html=True)
    
    action = st.radio("Choose an action:", ("Encode Image", "Decode Image"))
    key = st.text_input("Enter Blowfish Encryption Key (8-56 bytes):", type="password", help="Must be 8-56 characters long")
    
    if action == "Encode Image":
        st.subheader("Encode a Secret Image")
        cover_file = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg"], key="cover_img")
        secret_file = st.file_uploader("Upload Secret Image", type=["png", "jpg", "jpeg"], key="secret_img")
        output_name = st.text_input("Output file name (e.g., encoded.png)", "encoded.png")
        
        if st.button("Encode"):
            if not key:
                st.warning("Please enter an encryption key!")
            elif not (8 <= len(key) <= 56):
                st.error("Key must be between 8 and 56 characters long!")
            elif cover_file and secret_file:
                try:
                    with st.spinner("Encoding image..."):
                        output_path = encode_image_steg(cover_file, secret_file, output_name, key)
                        st.success(f"Encoded image saved as {output_path}")
                        with open(output_path, "rb") as file:
                            st.download_button("Download Encoded Image", file, file_name=output_name)
                except Exception as e:
                    st.error(f"Error during encoding: {e}")
            else:
                st.warning("Please upload both cover and secret images.")
    
    elif action == "Decode Image":
        st.subheader("Decode a Hidden Image")
        encoded_file = st.file_uploader("Upload Encoded Image", type=["png", "jpg", "jpeg"], key="encoded_img")
        output_name = st.text_input("Output file name for secret image (e.g., secret.png)", "secret.png")
        
        if st.button("Decode"):
            if not key:
                st.warning("Please enter an encryption key!")
            elif not (8 <= len(key) <= 56):
                st.error("Key must be between 8 and 56 characters long!")
            elif encoded_file:
                try:
                    with st.spinner("Decoding image..."):
                        output_path = decode_image_steg(encoded_file, output_name, key)
                        if output_path:
                            st.success(f"Decoded secret image saved as {output_path}")
                            with open(output_path, "rb") as file:
                                st.download_button("Download Secret Image", file, file_name=output_name)
                except Exception as e:
                    st.error(f"Error during decoding: {e}")
            else:
                st.warning("Please upload an encoded image.")

elif page == "Text in Image":
    st.markdown("<h2 class='sub-header'>Text in Image Steganography</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
    <p>Hide encrypted text in an image as a binary representation or extract text from a binary image.</p>
    <p><strong>Note:</strong> Save the encryption key when hiding text; paste it exactly as shown to extract!</p>
    </div>
    """, unsafe_allow_html=True)
    
    option = st.radio("Choose an action:", ("Hide Text in Image", "Extract Text from Image"))
    
    if option == "Hide Text in Image":
        text = st.text_area("Enter the text to hide")
        uploaded_image = st.file_uploader("Upload a carrier image (optional)", type=["png", "jpg", "jpeg"], key="carrier_text")
        if st.button("Hide Text"):
            if text:
                with st.spinner("Processing..."):
                    key = generate_key_text()
                    encrypted_text = encrypt_text(text, key)
                    binary_image = text_to_binary_image(encrypted_text.decode('utf-8'))
                    
                    st.image(binary_image, caption="Binary representation of encrypted text", use_column_width=True)
                    key_str = key.decode('utf-8')
                    st.write("Encryption Key (copy this exactly!):", key_str)
                    
                    img_byte_arr = io.BytesIO()
                    binary_image.save(img_byte_arr, format='PNG')
                    img_byte_arr = img_byte_arr.getvalue()
                    st.download_button("Download Binary Image", img_byte_arr, file_name="stego_binary.png", mime="image/png")
            else:
                st.warning("Please enter some text to hide!")
    
    elif option == "Extract Text from Image":
        uploaded_image = st.file_uploader("Upload a stego binary image", type=["png", "jpg", "jpeg"], key="stego_text")
        key_input = st.text_input("Paste the decryption key exactly as provided", type="password")
        if st.button("Extract Text"):
            if uploaded_image and key_input:
                with st.spinner("Extracting..."):
                    try:
                        key_bytes = key_input.encode('utf-8')
                        Fernet(key_bytes)  # Validate key format
                        binary_image = Image.open(uploaded_image).convert("L")
                        extracted_text = binary_image_to_text(binary_image)
                        decrypted_text = decrypt_text(extracted_text.encode('utf-8'), key_bytes)
                        st.write("Extracted Text:", decrypted_text)
                    except ValueError as ve:
                        st.error(f"Invalid key format: {ve} (Key must be 32 url-safe base64-encoded bytes)")
                    except InvalidToken:
                        st.error("Decryption failed: Incorrect key or corrupted data")
                    except Exception as e:
                        st.error(f"Error during extraction: {e}")
            else:
                st.warning("Please upload an image and paste the decryption key!")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #ff3131;'>Steganography Dashboard | Created with Streamlit</div>", unsafe_allow_html=True)