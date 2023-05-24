import cv2
from pyzbar.pyzbar import decode
import pandas as pd
from openpyxl import Workbook
from datetime import datetime
workbook = Workbook()
sheet = workbook.active
sheet.append(['QR Code Data', 'Timestamp'])
def scan_qr_code():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # Decode QR code
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sheet.append([qr_data, timestamp])
            workbook.save('data.xlsx')
            print(f"QR Code Data: {qr_data}")
            print(f"Timestamp: {timestamp}")

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
scan_qr_code()
