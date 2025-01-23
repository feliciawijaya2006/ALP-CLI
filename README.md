# CLI Linux Emulator in Python

## **Overview**
Aplikasi ini adalah implementasi dari emulator Command Line Interface (CLI) yang meniru beberapa perintah dasar yang ada pada shell/terminal sistem Linux, namun diimplementasikan menggunakan bahasa pemrograman Python. Program ini memungkinkan pengguna untuk menjalankan perintah-perintah seperti `ls`, `pwd`, `cd`, dan perintah lainnya melalui terminal berbasis Python.

## **Tujuan Proyek**
Tujuan dari proyek ini adalah untuk memberikan pemahaman tentang cara kerja sistem file di dalam terminal, serta memungkinkan mahasiswa untuk mengimplementasikan manipulasi file dan direktori menggunakan Python. Proyek ini juga mencakup penambahan beberapa perintah unik yang berguna dan relevan dengan konteks penggunaan sehari-hari.

## **Fitur Utama**
Aplikasi ini mendukung beberapa perintah yang sering digunakan pada terminal Linux, antara lain:
- Menampilkan file dan direktori.
- Mengubah direktori kerja.
- Membuat, menghapus, menyalin, dan memindahkan file serta direktori.
- Mencari file atau direktori berdasarkan pola tertentu.
- Menampilkan struktur direktori dalam bentuk pohon.

## **Daftar Perintah yang Tersedia**

### **Perintah Wajib**
1. **`ls`**  
   Menampilkan daftar file dan folder di direktori saat ini.
   ```bash
   ls
   ```
2. **`pwd`**  
   Menampilkan direktori kerja saat ini.
   ```bash
   pwd
   ```
3. **`cd <path>`**  
   Mengubah direktori kerja ke direktori yang ditentukan.
   ```bash
   cd /home/user/Documents
   ```
4. **`mkdir <name>`**  
   Membuat direktori baru dengan nama yang ditentukan.
   ```bash
   mkdir new_directory
   ```
5. **`rmdir <name>`**  
   Menghapus direktori yang kosong.
   ```bash
   rmdir old_directory
   ```
6. **`touch <name>`**  
   Membuat file baru yang kosong.
   ```bash
   touch newfile.txt
   ```
7. **`rm <name>`**  
   Menghapus file dengan nama yang ditentukan.
   ```bash
   rm oldfile.txt
   ```
8. **`cp <source> <destination>`**  
   Menyalin file dari lokasi sumber ke lokasi tujuan.
   ```bash
   cp file.txt /path/to/destination/
   ```
9. **`mv <source> <destination>`**  
   Memindahkan atau mengganti nama file atau direktori.
   ```bash
   mv file.txt /path/to/destination/
   ```
10. **`help`**  
   Menampilkan daftar perintah yang tersedia dan deskripsi singkat tentang penggunaannya.
   ```bash
   help
   ```
11. **`clear`**  
   Membersihkan layar terminal.
   ```bash
   clear
   ```
12. **`exit`**  
   Keluar dari aplikasi CLI.
   ```bash
   exit
   ```
### **Perintah Tambahan**
1. **`search <pattern>`**  
   Mencari file atau direktori berdasarkan pola tertentu dalam nama.
   ```bash
   search test
   ```
2. **`tree`**  
   Menampilkan struktur direktori dari lokasi saat ini dalam bentuk pohon.
   ```bash
   tree
   ```
3. **`log <command>`**  
  Menyimpan riwayat penggunaan command ke file log command_log.txt.
   ```bash
   log mkdir new_directory
   ```
### **Cara Penggunaan**
1. Persyaratan Sistem Pastikan Python 3 sudah terpasang di sistem Anda. Anda dapat memeriksanya dengan menjalankan perintah berikut di terminal:
   ```bash
   python3 --version
   ```
2. Menjalankan Program Setelah mengunduh atau mengkloning repository ini, Anda dapat menjalankan program dengan cara:
   ```bash
   python alp-cli.py
   ```
3. Menjalankan Perintah Setelah program berjalan, Anda akan melihat prompt cli>. Di sini Anda dapat mengetikkan perintah yang tersedia, seperti yang tercantum di atas. Program akan memproses perintah dan menampilkan hasilnya.
4. Contoh Penggunaan
- Menampilkan daftar file:
  ```bash
   cli> ls
   ```
- Mengubah direktori:
  ```bash
   cli> cd /home/user/Documents
   ```
- Mencari file dengan pola tertentu:
  ```bash
   cli> search example
   ```
- Menampilkan struktur direktori:
  ```bash
   cli> tree
   ```
- Mencatat perintah ke file log:
  ```bash
   cli> log mkdir new_directory
   ```
### **Penjelasan Perintah Tambahan**
- **`search <pattern>`**  
Mencari file atau direktori yang mengandung pola yang diberikan dalam nama file atau direktori di seluruh struktur direktori yang ada.
- **`tree`**  
Menampilkan struktur direktori di bawah direktori kerja saat ini dalam bentuk pohon yang mudah dibaca. Ini berguna untuk melihat hubungan antar direktori dan file.
- **`log <command>`**  
Menyimpan riwayat setiap perintah yang dijalankan oleh pengguna ke dalam file command_log.txt. Ini memungkinkan pengguna untuk melacak perintah-perintah yang telah dijalankan sebelumnya.
### **Kesimpulan**
Proyek ini memberikan kesempatan untuk memahami dan mengimplementasikan berbagai perintah yang ada di dalam CLI sistem operasi Linux, serta mengembangkan aplikasi berbasis terminal menggunakan Python. Dengan menggunakan berbagai library standar seperti **`os`**  , **`sys`**  , dan **`shutil`**  , aplikasi ini berhasil meniru perintah-perintah dasar yang sering digunakan di terminal Linux. Penambahan perintah unik seperti **`search`**  , **`tree`**  , dan **`log`**   menambah kegunaan dan fleksibilitas dari aplikasi CLI ini.
Aplikasi ini tidak hanya berguna untuk memahami cara terminal bekerja, tetapi juga sebagai latihan dalam memanipulasi file dan direktori melalui Python. Dengan dokumentasi yang lengkap, pengguna dapat dengan mudah memahami cara menjalankan aplikasi dan menggunakan berbagai perintah yang tersedia.
