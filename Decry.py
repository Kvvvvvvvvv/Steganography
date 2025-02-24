import cv2
import os
import numpy as np
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Image not found or could not be loaded.")
    exit()
password_file = "password.txt"
if not os.path.exists(password_file):
    print("Error: Password file not found.")
    exit()
with open(password_file, "r") as f:
    stored_password = f.read().strip()
c = {i: chr(i) for i in range(256)}
n, m, z = 0, 0, 0
message = ""
pas = input("Enter passcode for Decryption: ")
if stored_password == pas:
    while n < img.shape[0] and m < img.shape[1]:
        pixel_value = int(img[n, m, z])
        if pixel_value == 0:
            break
        try:
            message += c[pixel_value]
        except KeyError:
            print(f"Warning: Unexpected value {pixel_value} found at position ({n},{m},{z})")
            break
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
