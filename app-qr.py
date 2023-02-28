import cv2
import numpy as np
import streamlit as st

image = st.camera_input("Show QR code")

if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    data_makanan = [
        {
            'code': 12345678,
            'nama_makanan': 'seblak madya',
            'stok': 5
        },
        {
            'code': 12345679,
            'nama_makanan': 'Bakso',
            'stok': 3
        }
    ]

    data_makanan_temp = {}
    st.write("Kode Qr : ", data)

    # cari pada data_makanan
    for i in data_makanan:
        if i['code'] == int(data):
            data_makanan_temp = {
                'code': i['code'],
                'nama_makanan': i['nama_makanan'],
                'stok': i['stok']
            }
            break

    st.write("Data Makanan sebelum dibeli", data_makanan_temp)

    # cari pada data_makanan
    for i in data_makanan:
        if i['code'] == int(data):
            stok = i['stok'] - 1
            data_makanan_temp = {
                'code': i['code'],
                'nama_makanan': i['nama_makanan'],
                'stok': stok
            }
            break
    
    st.write("Data Makanan Setelah dibeli", data_makanan_temp)