# Checker Eligible [Grassfoundation](https://katherineoelsner.com/)

Bot ini adalah script Python sederhana yang digunakan untuk memeriksa beberapa alamat wallet terkait eligibility dalam alokasi airdrop melalui API Grass. Script ini membaca alamat wallet dari file teks (`wallet.txt`), mengirim permintaan API untuk setiap alamat, dan menampilkan apakah wallet tersebut eligible serta jumlah alokasi koin untuk setiap wallet yang eligible.

Fitur tambahan:
- **Total alokasi koin** dari semua wallet yang eligible.
- **Jumlah wallet yang eligible**.
- Output yang diberi **warna** untuk mempermudah interpretasi hasil.

## Fitur
- **Pengecekan banyak wallet**: Memproses beberapa alamat wallet dari satu file.
- **Pengecekan eligibility**: Menentukan apakah sebuah wallet eligible untuk alokasi airdrop.
- **Total alokasi**: Menghitung total alokasi koin untuk setiap wallet dan menampilkan jumlah total semua wallet.
- **Output terminal berwarna**: Hijau untuk wallet yang eligible, merah untuk yang tidak eligible, kuning untuk total alokasi.

## Persyaratan

Untuk menjalankan proyek ini, kamu memerlukan:
- **Python 3.x** yang sudah terpasang di sistem.
- Library **`requests`** untuk melakukan panggilan API.
- Library **`colorama`** untuk pewarnaan teks di terminal.

### Instalasi dependencies
Pertama, pastikan bahwa kamu memiliki library Python yang dibutuhkan dengan menjalankan perintah berikut:

```bash
pip install requests
pip install colorama
```

### Ikuti langkah-langkah berikut untuk memulai proyek:

## Clone repository:

```bash
git clone https://github.com/dinarsanjaya/grass
cd grass
```
## Buat file wallet.txt:

Di dalam direktori proyek, buat file wallet.txt.
Tambahkan satu alamat wallet per baris. Contoh:
```bash
UPSCQNqdbiaqrQou9X9y8mr43ZHzvoNpKC26Mo7GubF
5uD7Z9p3iBznhR7xidhh91NUPUjak1LCxAMnjB5LsXdL
5dDyfdy9fannAdHEkYghgQpiPZrQPHadxBLa1WsGHPFi
```

## Jalankan script:

Jalankan script Python dengan perintah:
```bash
python bot.py
```
- Script akan membaca alamat wallet dari file wallet.txt, memeriksa setiap alamat, dan menampilkan hasilnya.

## Contoh Output
```bash

Wallet: UPSCQNqdbiaqrQou9X9y8mr43ZHzvoNpKC26Mo7GubF - Eligible. Total alokasi: 21.55 coins.
Wallet: 5uD7Z9p3iBznhR7xidhh91NUPUjak1LCxAMnjB5LsXdL - Not eligible for any allocation.
Wallet: 5dDyfdy9fannAdHEkYghgQpiPZrQPHadxBLa1WsGHPFi - Eligible. Total alokasi: 5.49 coins.

Total alokasi koin semua wallet: 27.04 coins.
Total wallet eligible: 2 dari 3 wallet.
```
## Pewarnaan
Output terminal akan diberi warna sebagai berikut:

- Hijau: Wallet eligible untuk airdrop.
- Merah: Wallet tidak eligible.
- Kuning: Total alokasi untuk semua wallet.
- Cyan: Jumlah wallet yang eligible.
## Penanganan Error
- File Tidak Ditemukan: Jika file wallet.txt tidak ditemukan, pesan error akan ditampilkan.
- Error API: Jika permintaan API gagal, script akan menampilkan pesan error dan kode error yang relevan.
## Kontribusi
Silakan berkontribusi pada proyek ini dengan mengirimkan pull request atau membuka issue baru.
