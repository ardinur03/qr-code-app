import cv2
import numpy as np
import streamlit as st
import json

image = st.camera_input("Show QR code")

if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    # load data makanan dari file json
    with open('food-api.json') as json_file:
        data_makanan = json.load(json_file)


    data_makanan_temp = {}
    st.write("Kode Qr : ", data)

    # cari pada data_makanan
    for i in data_makanan:
        if i['code'] == str(data):
            data_makanan_temp = {
                'code': i['code'],
                'nama_makanan': i['nama_makanan'],
                'stok': i['stok']
            }
            break

    st.write("Data Makanan sebelum dibeli", data_makanan_temp)
    
     # kurangin stok pada json data_makanan_temp 
    if data_makanan_temp['stok'] > 0:
        data_makanan_temp['stok'] = data_makanan_temp['stok'] - 1

    # update data makanan
    for i in data_makanan:
        if i['code'] == str(data):
            if i['stok'] > 0:
                i['stok'] = data_makanan_temp['stok']
                # simpan data makanan ke file json
                with open('food-api.json', 'w') as outfile:
                    json.dump(data_makanan, outfile)
                st.write("Data Makanan Setelah dibeli", data_makanan_temp)
            else:
                st.write("Stok habis")
            break

    