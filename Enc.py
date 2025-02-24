import cv2
import os
img = cv2.imread("img1.webp")
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
d = {chr(i): i for i in range(255)}
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
cv2.imwrite("encryptedImage.png", img)
with open("password.txt", "w") as f:
    f.write(password)
