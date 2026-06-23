# 🔒 Steganography Dashboard

A comprehensive web-based application built with **Streamlit** that enables secure data hiding within images using modern steganography and cryptographic techniques. The dashboard supports both image-in-image and text-in-image steganography while ensuring confidentiality through robust encryption algorithms.

---

## 1. Project Overview

The Steganography Dashboard is designed to provide a secure and user-friendly platform for concealing sensitive information within digital images. By combining steganography with encryption, the application ensures that hidden data remains protected from unauthorized access.

---

## 2. Key Features

### 🖼️ Image-in-Image Steganography

* Uses **Least Significant Bit (LSB)** substitution to hide a secret image within a cover image.
* Encrypts the secret image using **Blowfish Encryption (CBC Mode)** before embedding.
* Automatically resizes secret images when necessary to fit within the cover image's storage capacity.
* Supports secure image extraction using the correct encryption key.

### 📝 Text-in-Image Steganography

* Encrypts text using **Fernet Symmetric Encryption**.
* Converts encrypted text into a binary image representation.
* Generates downloadable stego-images in PNG format.
* Supports secure text recovery through decryption keys.

### 🎨 Interactive Dashboard

* Built using **Streamlit**.
* Dark-themed responsive interface.
* File upload and download support.
* Real-time encoding and decoding operations.

---

## 3. Technology Stack

### Frontend/UI

* Streamlit

### Image Processing

* Pillow (PIL)
* NumPy

### Cryptography

* PyCryptodome (Blowfish)
* Cryptography Library (Fernet)

### Programming Language

* Python

---

## 4. Usage Instructions

### Install Dependencies

```bash
pip install streamlit pillow numpy pycryptodome cryptography
```

### Launch the Application

```bash
streamlit run cs3.py
```

---

## 5. Workflow

### Image-in-Image Encoding

1. Upload a cover image.
2. Upload a secret image.
3. Enter a Blowfish encryption key (8–56 bytes).
4. Encode the image.
5. Download the generated stego-image.

### Image-in-Image Decoding

1. Upload the encoded image.
2. Enter the same encryption key.
3. Extract the hidden image.

### Text-in-Image Encoding

1. Enter secret text.
2. Generate encrypted binary image.
3. Save the generated decryption key.
4. Download the binary stego-image.

### Text-in-Image Decoding

1. Upload the stego-image.
2. Enter the saved decryption key.
3. Recover the original text.

---

## 6. Security Features

* Blowfish Encryption (CBC Mode)
* Fernet Symmetric Encryption
* Password-Protected Data Recovery
* Secure Hidden Data Transmission
* Encrypted Image and Text Storage

---

## 7. Repository Structure

```text
Secure-Steganography-Dashboard/
│
├── cs3.py
├── encoded.png
├── secret.png
├── stegenc.png
└── README.md
```

---

## 8. Applications

* Secure Communication
* Digital Watermarking
* Cybersecurity Research
* Confidential Information Sharing
* Educational Demonstrations of Steganography

---

## 9. Future Enhancements

* Audio Steganography
* Video Steganography
* AES-256 Encryption Support
* Cloud Storage Integration
* Multi-Factor Authentication

---

## 10. Security Warning

* The security of hidden data depends entirely on the secrecy of encryption keys.
* Loss of the encryption key may result in permanent data loss.
* Use **PNG** format to avoid corruption caused by lossy image compression.

---

## Author

**P. Moksha**
B.Tech Computer Science Engineering (Artificial Intelligence)
