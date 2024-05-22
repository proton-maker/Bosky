# Bosky Online Store Module

Halo sobat developer! 🎉

Selamat datang di modul **Bosky Online Store** untuk Odoo. Ini adalah modul keren yang akan mengubah Odoo kamu menjadi toko online yang kekinian dan siap untuk berbisnis. Yuk, kita lihat apa saja yang bisa dilakukan oleh modul ini!

## Fitur-Fitur Keren

1. **Manajemen Produk:**
   - Tambahkan, edit, dan hapus produk dengan mudah.
   - Tentukan harga dan diskon produk, hitung harga akhir setelah diskon. Diskon gila-gilaan? Bisa banget!
   
2. **Manajemen Kategori:**
   - Atur produk kamu berdasarkan kategori biar lebih rapi dan gampang dicari. Tambahkan, edit, dan hapus kategori sesuka hati.

3. **Manajemen Pesanan:**
   - Kelola pesanan pelanggan dengan mudah. Pantau status pembayaran (Pending/Paid) dan hitung total pesanan secara otomatis.

4. **Laporan Penjualan:**
   - Hasilkan laporan penjualan dengan detail total penjualan dan produk terlaris. Jadi, kamu bisa tahu produk apa yang lagi ngehits!

5. **Notifikasi Email:**
   - Kirim notifikasi email otomatis ke pelanggan setelah pesanan dibuat. Biar pelanggan tetap update dan merasa diperhatikan. 😎

## Instalasi

### Prasyarat

- Odoo 17.0
- Python 3.8 atau lebih tinggi

### Langkah-Langkah Instalasi

1. **Clone repositori ini:**

    ```bash
    git clone https://github.com/proton-maker/Bosky.git
    ```

2. **Pindahkan direktori modul ke direktori addons Odoo:**

    ```bash
    mv Bosky/online_store /path/to/odoo/addons/
    ```

3. **Tambahkan path direktori custom addons ke file konfigurasi Odoo (odoo.conf):**

    ```ini
    [options]
    addons_path = /path/to/odoo/addons,/path/to/odoo/custom_addons
    ```

4. **Restart server Odoo:**

    ```bash
    sudo systemctl restart odoo
    ```

5. **Aktifkan developer mode di Odoo, lalu pergi ke menu `Apps` dan klik `Update Apps List`.**

6. **Cari modul `Online Store` dan klik `Install`.**

## Penggunaan

### Manajemen Produk

1. Pergi ke menu `Online Store` > `Products`.
2. Klik `Create` untuk menambahkan produk baru.
3. Isi detail produk, termasuk nama, deskripsi, harga, diskon, dan kategori.

### Manajemen Kategori

1. Pergi ke menu `Online Store` > `Categories`.
2. Klik `Create` untuk menambahkan kategori baru.
3. Isi nama kategori dan tambahkan produk yang termasuk dalam kategori tersebut.

### Manajemen Pesanan

1. Pergi ke menu `Online Store` > `Orders`.
2. Klik `Create` untuk membuat pesanan baru.
3. Isi detail pesanan, termasuk nama pelanggan, tanggal pesanan, produk yang dipesan, dan status pembayaran.

### Laporan Penjualan

1. Pergi ke menu `Online Store` > `Sales Reports`.
2. Isi rentang tanggal yang diinginkan dan klik `Generate Report`.
3. Laporan akan menampilkan total penjualan dan produk terlaris dalam rentang tanggal tersebut.

### Notifikasi Email

Setiap kali pesanan dibuat, notifikasi email akan dikirim secara otomatis ke alamat email pelanggan yang terdaftar.

## Kontribusi

Kami selalu terbuka untuk kontribusi! Fork repositori ini dan buat pull request dengan perubahan yang kamu buat. Pastikan semua tes berjalan lancar sebelum mengirimkan PR kamu. Ayo bareng-bareng bikin modul ini makin keren! 😍

## Status Pengembangan

Modul ini masih dalam tahap pengembangan. Fitur-fitur baru dan peningkatan akan terus ditambahkan. Jadi, tetap pantau terus ya!

## Lisensi

Modul ini dilisensikan di bawah LGPL-3.0. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

## Kontak

Punya pertanyaan atau butuh bantuan? Jangan ragu untuk kontak kami di phionix32@protonmail.com atau kunjungi [bosmudasky.com](http://www.bosmudasky.com).

Selamat berkreasi dan selamat berjualan online! 🚀
