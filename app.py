from flask import Flask, render_template, request, redirect, send_file
import cv2
import os
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
END_MARKER = "$$END$$"

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    message = request.form['message'] + END_MARKER
    password = request.form['password']

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    if img is None:
        return "Error loading image!"

    d = {chr(i): i for i in range(256)}
    n = m = z = 0
    for char in message:
        img[n, m, z] = d.get(char, 0)
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encrypted.png')
    cv2.imwrite(encrypted_path, img)

    with open("password.txt", "w") as f:
        f.write(password)

    return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['image']
    password_input = request.form['password']

    with open("password.txt", "r") as f:
        stored_password = f.read().strip()

    if password_input != stored_password:
        return "YOU ARE NOT AUTHORIZED"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    if img is None:
        return "Error loading image!"

    c = {i: chr(i) for i in range(256)}
    n = m = z = 0
    message = ""
    while n < img.shape[0] and m < img.shape[1]:
        pixel_value = int(img[n, m, z])
        char = c.get(pixel_value, '')
        message += char
        if END_MARKER in message:
            message = message.replace(END_MARKER, "")
            break
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    return f"Decrypted message: {message}"

if __name__ == '__main__':
    app.run(debug=True)
