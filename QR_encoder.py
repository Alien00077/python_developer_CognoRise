import qrcode
import cv2

def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    if data:
        print("Decoded data:", data)
    else:
        print("No data found")

choice = input("Choose (encode/decode): ").strip().lower()
if choice == "encode":
    data = input("Enter data to encode: ")
    filename = input("Enter filename to save (e.g., qrcode.png): ")
    generate_qr(data, filename)
elif choice == "decode":
    filename = input("Enter filename to decode (e.g., qrcode.png): ")
    decode_qr(filename)
else:
    print("Invalid choice")
