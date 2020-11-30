# HRISA 
merupakan project tugas matakuliah Basis Data Oracle

## menjalankan project di local komputer

## pre-requires
1. sudah terinstall gitkraken & sudah daftar akun
2. sudah punya akun gitlab
3. terinstall pyhton

## langkah-langkah

1. clone repo git https://gitlab.com/IKHINtech/hrisa ke giktraken
2. masuk ke direktori repo(untuk yang menggunakan vscode cukup buka menggunakan vscode)
3. buka terminal ke direktori repo
4. ketik pip install virtualenv
5. ketik py -3 -m venv venv
6. aktifasi venv ketik venv\Scripts\activate
7. ketik pip install -r requirements.txt
8. ketik pip install cx_Oracle
9. kalo sudah berhasil bisa coba :
    1. set FLASK_APP=hrsia.py
    2. set FLASK_DEBUG=1
    3. flask run
    4. web akan berjalan di 127.0.0.1:5000