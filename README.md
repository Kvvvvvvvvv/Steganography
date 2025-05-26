# 🕵️‍♂️ Steganography Web App using Flask

This is a Flask-based web application that allows users to **hide secret messages inside images (Image Steganography)** using **Least Significant Bit (LSB) substitution** and retrieve them securely with password protection.

---

## 📌 Features

- 🔐 Hide secret text messages inside PNG images.
- 🖼️ Upload your own image or use a default one.
- 🔍 Extract hidden messages using a password.
- 📁 Simple and clean file structure.
- 🔒 Password protection for both encoding and decoding.
- 🧠 Built using the concept of LSB (Least Significant Bit) manipulation.

---

## 🧠 What is Steganography?

**Steganography** is the practice of concealing information within another medium to ensure secrecy. Unlike cryptography, which only hides the content, steganography hides the **existence** of the message itself.

This project uses:
- 📷 **Image Steganography** via **LSB substitution**, where the least significant bits of image pixels are modified to hide data.

---

## 🚀 How It Works

1. **Encoding Process**
   - User uploads an image.
   - Enters the secret message and password.
   - The message is hidden inside the image using LSB technique.
   - Output is a downloadable stego-image.

2. **Decoding Process**
   - User uploads the stego-image.
   - Enters the password.
   - The hidden message is extracted and displayed if the password is correct.

---

## 🛠️ Technologies Used

- 🐍 Python 3.x
- 🔥 Flask (Web Framework)
- 📦 Pillow (Image Processing)
- 🌐 HTML/CSS (Frontend)

---

## 📂 Project Structure

