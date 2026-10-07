import csv
from prettytable import PrettyTable

nama_file = "sc6.csv"

while True:
    print("\n===== Menu Pencatatan Nilai =====")
    print("1. Lihat data nilai")
    print("2. Tambah data nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = []

        with open(nama_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)

            labels = data.pop(0)

            tabel = PrettyTable()
            tabel.field_names = ["NO", "NAMA", "NIM", "KELAS", "NILAI", "GRADE", "STATUS"]

            for row in data:
                nilai = int(row[4])

                if nilai >= 85:
                    grade = "A"
                    status = "LULUS"
                elif nilai >= 75:
                    grade = "B"
                    status = "LULUS"
                elif nilai >= 65:
                    grade = "C"
                    status = "LULUS"
                elif nilai >= 50:
                    grade = "D"
                    status = "TIDAK LULUS"
                else:
                    grade = "E"
                    status = "TIDAK LULUS"

                tabel.add_row([row[0], row[1], row[2], row[3], nilai, grade, status])

            print("\nDATA NILAI MAHASISWA SISTEM INFORMASI")
            print(tabel)

    elif pilihan == "2":
        while True:
            no = input("Masukkan No: ")
            if no.isdigit() and int(no) > 0:
                break
            print("Input harus berupa angka!")

        while True:
            nama = input("Masukkan Nama: ")
            if nama.strip() != "":
                break
            else:
                print("Input tidak boleh kosong!")

        while True:
            nim = input("Masukkan Nim: ")
            if nim.isdigit() and len(nim) == 10:
                break
            else:
                print("Nim harus 10 angka!")

        while True:
            kelas = input("Masukkan Kelas: ")
            if kelas.strip() != "":
                break
            else:
                print("Input tidak boleh kosong!")

        while True:
            nilai = input("Masukkan Nilai: ")
            if nilai.isdigit() and 0 <= int(nilai) <= 100:
                break
            else:
                print("Input harus berupa angka (1-100)!")

        with open(nama_file, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow([no, nama, nim, kelas, nilai])

            print("Data berhasil ditambahkan!")

    elif pilihan == "3":
        print("\nProgram Selesai.")
        break

    else:
        print("\nPilihan tidak tersedia!")
