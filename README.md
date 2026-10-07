<h1 align="center">
 StudyCase6_DDP_Muhammad-Atha-Andhika_065_B
</h1>

--------------------------------------------

## Sistem Pencatatan Nilai Mahasiswa
--------------------------------------------

**Nama : Muhammad Atha Andhika**

**Nim : 2609116065**

**Kelas : B**

**Dasar Dasar Pemrograman**

--------------------------------------------

**1. Sinopsis Program**

    Sistem Pencatatan Nilai Mahasiswa merupakan program sederhana berbasis Python yang digunakan untuk mencatat 
    dan menampilkan data nilai mahasiswa. Program memanfaatkan file CSV untuk menjadi tempat penyimpanan data.

    Program memiliki 3 menu utama, yaitu melihat data, menambahkan data dan keluar dari program. Program juga menerapkan validasi
    input untuk memastikan data yang dimasukkan sesuai dengan ketentuan.

--------------------------------------------

**2. Penjelasan Kode**

<img width="1015" height="418" alt="Screenshot 2026-10-07 154858" src="https://github.com/user-attachments/assets/5f8cae88-5456-4033-8781-6c8193215c66" />

    Jadi disini program dimulai dengan menggunakan import csv untuk membaca dan menyimpan data dalam file CSV, dan PrettyTable digunakan untuk membuat tampilan
    data dengan tabel yang rapi. Variabel nama_file menyimpan nama file CSV yang digunakan program. while True membuat menu berjalan terus sampai dihentikan dengan
    break.print() berfungsi menampilkan judul dan pilihan menu, sedangkan ‘input()’ menerima pilihan pengguna dan menyimpannya ke variabel pilihan.

<img width="1498" height="1223" alt="Screenshot 2026-10-07 154915" src="https://github.com/user-attachments/assets/ab8173c6-78eb-4f37-a5d3-8893b9d36142" />

    Dibagian ini pilihan = 1, data =[] membuat list kosong untuk menampung data. open() digunakan untuk membuka file CSV, kemudian csv.reader() membaca data berdasarkan
    pemisah koma melalui delimiter=",". Setiap baris dimasukkan ke list menggunakan append(), sedangkan pop(0) digunakan untuk mengambil dan menghapus baris header. PrettyTable() 
    membuat tabel dan field_names menentukan nama kolom yang ditampilkan. Nilai dari CSV diubah menjadi angka menggunakan int(), kemudian if, elif, dan else menentukan grade serta 
    status kelulusan berdasarkan nilai. Terakhir, add_row() menambahkan data mahasiswa ke dalam tabel dan print() menampilkan hasilnya.

<img width="1345" height="1121" alt="Screenshot 2026-10-07 155033" src="https://github.com/user-attachments/assets/975b741b-c8e3-4ec7-a1ad-a0634f3e3028" />

    Dibagian ini pilihan = 2, pengguna diminta memasukkan No, Nama, NIM, Kelas, dan Nilai. while True digunakan agar setiap input terus diminta sampai benar. isdigit() memastikan 
    input berupa angka, int() mengubah data menjadi bilangan, len() memeriksa jumlah digit NIM, sedangkan strip() memastikan nama dan kelas tidak kosong. Nilai juga diperiksa agar 
    berada pada rentang 0–100. Jika input salah, print() menampilkan pesan kesalahan dan pengguna diminta mengulang. Setelah semua data valid, open() dengan mode "a" membuka CSV 
    untuk menambahkan data, csv.writer() membuat objek untuk menulis data, dan writerow() menyimpan data baru tanpa menghapus data sebelumnya.

<img width="859" height="187" alt="Screenshot 2026-10-07 155044" src="https://github.com/user-attachments/assets/093517ec-827d-4ad8-b4b5-8af1bf6a4996" />

    Dibagian ini pilihan = 3, print() menampilkan pesan "Program Selesai.", kemudian break menghentikan while True sehingga program berakhir. Sementara itu, else digunakan untuk 
    menangani pilihan menu selain 1, 2, atau 3. Jika pilihan tidak sesuai, program menampilkan "Pilihan tidak tersedia!" dan kembali menampilkan menu. Dengan demikian, program
    tetap berjalan sampai pengguna memberikan pilihan yang benar atau memilih untuk keluar.

--------------------------------------------

**3. Output dan Penjelasannya**

<img width="516" height="141" alt="Screenshot 2026-10-07 155105" src="https://github.com/user-attachments/assets/ed551173-be5f-42a8-b709-a7e2a97e758a" />

    Program menyajikan 3 pilihan menu, pengguna bisa memilih salah satu dari ketiga menu.

<img width="724" height="378" alt="Screenshot 2026-10-07 155125" src="https://github.com/user-attachments/assets/8921369f-bb88-46b9-967b-930edbb8a765" />

    Pada menu 1, program menampilkan tabel mahasiswa yang sebelumnya sudah di buat dalam file CSV.

<img width="836" height="731" alt="Screenshot 2026-10-07 155415" src="https://github.com/user-attachments/assets/28dc73dd-a254-49e2-ac4f-e0bfc352acce" />

    Pada menu 2, pengguna dapat memasukkan data mahasiswa yang terdiri dari No, Nama, NIM, Kelas, dan Nilai. Menu ini dilengkapi dengan validasi input yang berfungsi untuk 
    memastikan setiap data yang dimasukkan sesuai dengan ketentuan. Jika pengguna memasukkan data yang tidak sesuai, seperti input kosong, karakter pada bagian yang seharusnya 
    berupa angka, NIM dengan jumlah digit yang tidak sesuai, atau nilai di luar rentang 0–100, program akan menampilkan pesan peringatan dan meminta pengguna menginputkan data 
    kembali hingga data yang dimasukkan valid.

<img width="771" height="376" alt="Screenshot 2026-10-07 155503" src="https://github.com/user-attachments/assets/1839e9b7-d89a-49a6-882f-e032a00a8515" />

    Ketika sudah dilakukan penambahan data pada menu 2, pengguna bisa mengecek apakah data tersebut sudah ter input pada menu 1.

<img width="626" height="208" alt="Screenshot 2026-10-07 155511" src="https://github.com/user-attachments/assets/207a16cf-d3a0-4a1d-8e4b-9d9da64c0e4e" />

    Pada menu 3, pengguna bisa mengakhiri program dengan break untuk menghentikan perulangan menu dan 
    program akan menampilkan output "Program Selesai." 

--------------------------------------------

**4. Bukti Data Baru Tetap Tersimpan**

<img width="467" height="180" alt="Screenshot 2026-10-07 170438" src="https://github.com/user-attachments/assets/5bf989e8-fbf9-40e2-8414-71ee909c5e9e" />

<img width="1400" height="628" alt="Screenshot 2026-10-07 170501" src="https://github.com/user-attachments/assets/e0fecbfd-4e54-4e12-9e9c-bab4b4a2ca34" />

    Bagian ini menunjukkan bahwa data yang telah di input sebelumnya ke dalam file CSV akan tetap muncul, tersimpan, dan bisa dilihat
    kembali ketika program dijalankan kembali.
