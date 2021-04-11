import os
import time

# UTAMA

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def utama():
    clear_screen()
    print("Data sekarang:",isi)
    print("_______________________________________")
    print("| [1] Menambahkan data                |")
    print("| [2] Menghapus data                  |")
    print("| [3] Mengganti data                  |")
    print("| [4] Mengurutkan data                |")
    print("| [5] Cari nilai min dan maks pd data |")
    print("| [6] Menghitung banyak data          |")
    print("| [7] Membalik urutan data            |")
    print("| [0] Keluar                          |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    menu = str(input("| Eksekusi menu : "))

# Keluar

    if menu == "0":
        clear_screen()
        print("Data sekarang:",isi)
        print("_______________________________________")
        print("| [1] Menambahkan data                |")
        print("| [2] Menghapus data                  |")
        print("| [3] Mengganti data                  |")
        print("| [4] Mengurutkan data                |")
        print("| [5] Cari nilai min dan maks pd data |")
        print("| [6] Menghitung banyak data          |")
        print("| [7] Membalik urutan data            |")
        print("| [#] Keluar                          |")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("| Eksekusi menu : 0")
        print("| Program keluar...")
        time.sleep(1)
        print("| Terimaksih sudah menggunakan")
        time.sleep(2)
        exit()

# Tambah data

    elif menu == "1":
        EROR = True
        while (EROR):
            try:
                clear_screen()
                print("Data sekarang:",isi)
                print("#1 Menambahkan data")
                print("______________________________")
                print("| [1] Menambah dari belakang |")
                print("| [2] Menambah dengan indeks |")
                print("| [3] Menambah dengan extend |")
                print("| [0] Kembali                |")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                brp = int(input("| Menambah dengan    : "))
                if brp == 0:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#1 Menambahkan data")
                    print("______________________________")
                    print("| [1] Menambah dari belakang |")
                    print("| [2] Menambah dengan indeks |")
                    print("| [3] Menambah dengan extend |")
                    print("| [#] Kembali                |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| #0 Kembali...")
                    time.sleep(1)
                    clear_screen()
                    utama()
                elif brp == 1:
                    EROR = True
                    while (EROR):
                        try:
                            salah = True
                            while(salah):
                                clear_screen()
                                print("Data sekarang:",isi)
                                print("#1 Menambahkan data")
                                print("______________________________")
                                print("| [#] Menambah dari belakang |")
                                print("| [2] Menambah dengan indeks |")
                                print("| [3] Menambah dengan extend |")
                                print("| [0] Kembali                |")
                                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print("| Menambah dengan    : append")
                                tambah = int(input("| Masukkan data      : "))
                                isi.append(tambah)
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                elif brp == 2:
                    EROR = True
                    while (EROR):
                        try:
                            salah = True
                            while(salah):
                                clear_screen()
                                print("Data sekarang:",isi)
                                print("#1 Menambahkan data")
                                print("______________________________")
                                print("| [1] Menambah dari belakang |")
                                print("| [#] Menambah dengan indeks |")
                                print("| [3] Menambah dengan extend |")
                                print("| [0] Kembali                |")
                                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print("| Menambah dengan    : indeks")
                                tambah1 = int(input("| Masukkan indeks    : "))
                                tambah2 = int(input("| Masukkan data      : "))
                                isi.insert(tambah1,tambah2)
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                elif brp == 3:
                    EROR = True
                    while (EROR):
                        clear_screen()
                        print("Data sekarang:",isi)
                        print("#1 Menambahkan data")
                        print("______________________________")
                        print("| [1] Menambah dari belakang |")
                        print("| [2] Menambah dengan indeks |")
                        print("| [#] Menambah dengan extend |")
                        print("| [0] Kembali                |")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        print("| Menambah dengan    : extend")
                        try:
                            salah = True
                            while(salah):
                                berenti = False
                                i = 1
                                data_baru = []
                                while(not berenti):
                                    data_baru = int(input("| Masukkan data ke-{} : ".format(i)))
                                    isi.extend([data_baru])
                                    i += 1
                                    tanya = input("| Input 0 jika cukup : ")
                                    if(tanya == "0"): 
                                        berenti = True
                                print("|")
                                print("| Banyak data yang ditambahkan ada {}".format(i-1))
                                print("| Data baru :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                else :
                    print("|")
                    print("| Input tidak valid!")
                    input("| Coba lagi...")
            except ValueError:
                print("|")
                print("| Input tidak valid!")
                input("| Coba lagi...")

# Hapus data

    elif menu == "2":
        EROR = True
        while (EROR):
            try:
                clear_screen()
                print("Data sekarang:",isi)
                print("#2 Menghapus data")
                print("_______________________________")
                print("| [1] Menghapus dengan data   |")
                print("| [2] Menghapus dengan indeks |")
                print("| [3] Menghapus dengan del    |")
                print("| [4] Hapus semua data        |")
                print("| [0] Kembali                 |")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                hapus = int(input("| Menghapus dengan   : "))
                if hapus == 0:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#2 Menghapus data")
                    print("_______________________________")
                    print("| [1] Menghapus dengan data   |")
                    print("| [2] Menghapus dengan indeks |")
                    print("| [3] Menghapus dengan del    |")
                    print("| [4] Hapus semua data        |")
                    print("| [#] Kembali                 |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| #0 Kembali...")
                    time.sleep(1)
                    clear_screen()
                    utama()
                elif hapus == 1:
                    EROR = True
                    while (EROR):
                        try:
                            clear_screen()
                            print("Data sekarang:",isi)
                            print("#2 Menghapus data")
                            print("_______________________________")
                            print("| [#] Menghapus dengan data   |")
                            print("| [2] Menghapus dengan indeks |")
                            print("| [3] Menghapus dengan del    |")
                            print("| [4] Hapus semua data        |")
                            print("| [0] Kembali                 |")
                            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            print("| Menghapus dengan   : data")
                            hapus = int(input("| Masukkan data      : "))
                            salah = True
                            while(salah):
                                isi.remove(hapus)
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Data tidak ditemukan!")
                            input("| Coba lagi...")
                elif hapus == 2:
                    EROR = True
                    while (EROR):
                        try:
                            clear_screen()
                            print("Data sekarang:",isi)
                            print("#2 Menghapus data")
                            print("_______________________________")
                            print("| [1] Menghapus dengan data   |")
                            print("| [#] Menghapus dengan indeks |")
                            print("| [3] Menghapus dengan del    |")
                            print("| [4] Hapus semua data        |")
                            print("| [0] Kembali                 |")
                            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            print("| Menghapus dengan   : indeks")
                            hapus = int(input("| Masukkan indeks    : "))
                            salah = True
                            while(salah):
                                isi.pop(hapus)
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except IndexError:
                            print("|")
                            print("| Index tidak ditemukan!")
                            input("| Coba lagi...")
                elif hapus == 3:
                    EROR = True
                    while (EROR):
                        try:
                            salah = True
                            while(salah):
                                clear_screen()
                                print("Data sekarang:",isi)
                                print("#2 Menghapus data")
                                print("_______________________________")
                                print("| [1] Menghapus dengan data   |")
                                print("| [2] Menghapus dengan indeks |")
                                print("| [#] Menghapus dengan del    |")
                                print("| [4] Hapus semua data        |")
                                print("| [0] Kembali                 |")
                                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print("| Menghapus dengan   : del")
                                hapus1 = int(input("| Menghapus dari     : "))
                                hapus2 = int(input("| Menghapus sebanyak : "))
                                del isi[hapus1:hapus2]
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                elif hapus == 4:
                    EROR = True
                    while (EROR):
                        try:
                            salah = True
                            while(salah):
                                clear_screen()
                                print("Data sekarang:",isi)
                                print("#2 Menghapus data")
                                print("_______________________________")
                                print("| [1] Menghapus dengan data   |")
                                print("| [2] Menghapus dengan indeks |")
                                print("| [3] Menghapus dengan del    |")
                                print("| [#] Hapus semua data        |")
                                print("| [0] Kembali                 |")
                                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print("| Menghapus          : semua data")
                                isi.clear()
                                print("| Data baru          :",isi,"\n")
                                back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                else:
                    print("|")
                    print("| Input tidak valid!")
                    input("| Coba lagi...")
            except ValueError:
                print("|")
                print("| Input tidak valid!")
                input("| Coba lagi...")

# Update data

    elif menu == "3":
        EROR = True
        while (EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("_______________________________________")
                    print("| [1] Menambahkan data                |")
                    print("| [2] Menghapus data                  |")
                    print("| [#] Mengganti data                  |")
                    print("| [4] Mengurutkan data                |")
                    print("| [5] Cari nilai min dan maks pd data |")
                    print("| [6] Menghitung banyak data          |")
                    print("| [7] Membalik urutan data            |")
                    print("| [0] Keluar                          |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| Data sekarang       :",isi)
                    print("| #3 Mengganti data")
                    print("|")
                    baru = int(input("| Mengganti indeks ke : "))
                    barw = int(input("| Masukkan data baru  : "))
                    isi[baru] = barw
                    print("| Data sekarang       :",isi,"\n")
                    back_menu()
            except IndexError:
                print("|")
                print("| Index tidak ditemukan!")
                input("| Coba lagi...")
            except ValueError:
                print("|")
                print("| Input tidak valid!")
                input("| Coba lagi...")


# Urut data

    elif menu == "4":
        EROR = True
        while (EROR):
            try:
                clear_screen()
                print("Data sekarang:",isi)
                print("#4 Mengurutkan data")
                print("______________________")
                print("|   [1] Ascending    |")
                print("|   [2] Descending   |")
                print("|   [0] Kembali      |")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                urut = int(input("| Mengurut berdasarkan: "))
                if urut == 0:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#4 Mengurutkan data")
                    print("______________________")
                    print("|   [1] Ascending    |")
                    print("|   [2] Descending   |")
                    print("|   [#] Kembali      |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| #0 Kembali...")
                    time.sleep(1)
                    clear_screen()
                    utama()
                elif urut == 1:
                    EROR = True
                    while (EROR):
                        try:
                            clear_screen()
                            print("Data sekarang:",isi)
                            print("#4 Mengurutkan data")
                            print("______________________")
                            print("|   [#] Ascending    |")
                            print("|   [2] Descending   |")
                            print("|   [0] Kembali      |")
                            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            print("| Mengurut berdasarkan: Ascending")
                            print("| data yang akan di sorting")
                            print("|",isi)
                            print("| Metode Selection Sort;\n")
                            urutan = 0
                            for x in range(len(isi)-1):
                                kecil = x
                                for y in range(x+1,len(isi)):
                                    if isi[y] < isi[kecil]:
                                        kecil = y
                                urutan += 1
                                isi[kecil],isi[x]=isi[x], isi[kecil]
                                print("|",urutan, isi)
                            print("\nData baru :",isi,"\n")
                            back_menu()
                        except ValueError:
                            print("\n| Data tidak ditemukan!")
                            input("| Coba lagi...")
                elif urut == 2:
                    EROR = True
                    while (EROR):
                        try:
                            clear_screen()
                            print("Data sekarang:",isi)
                            print("#4 Mengurutkan data")
                            print("______________________")
                            print("|   [1] Ascending    |")
                            print("|   [#] Descending   |")
                            print("|   [0] Kembali      |")
                            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            print("| Mengurut berdasarkan: Descending")
                            print("| data yang akan di sorting")
                            print("|",isi)
                            print("| Metode Selection Sort;\n")
                            urutan = 0
                            for x in range(len(isi)-1):
                                besar = x
                                for y in range(x+1,len(isi)):
                                    if isi[y] > isi[besar]:
                                        besar = y
                                urutan += 1
                                isi[besar],isi[x]=isi[x], isi[besar]
                                print("|",urutan, isi)
                            print("\nData baru:",isi,"\n")
                            back_menu()
                        except ValueError:
                            print("|")
                            print("| Input tidak valid!")
                            input("| Coba lagi...")
                else:
                    print("|")
                    print("| Input tidak valid!")
                    input("| Coba lagi...")
            except ValueError:
                print("|")
                print("| Input tidak valid!")
                input("| Coba lagi...")

# Cari data

    elif menu == "5":
        EROR = True
        while (EROR):
            try:
                clear_screen()
                print("Data sekarang:",isi)
                print("#5 Mencari nilai;")
                print("_______________________")
                print("| [1] Nilai terkecil  |")
                print("| [2] Nilai terbsesar |")
                print("| [0] Kembali         |")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                cari = int(input("| Mencari nilai : "))
                if cari == 0:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#5 Mencari nilai;")
                    print("_______________________")
                    print("| [1] Nilai terkecil  |")
                    print("| [2] Nilai terbsesar |")
                    print("| [#] Kembali         |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| #0 Kembali...")
                    time.sleep(1)
                    clear_screen()
                    utama()
                elif cari == 1:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#5 Mencari nilai;")
                    print("_______________________")
                    print("| [#] Nilai terkecil  |")
                    print("| [2] Nilai terbsesar |")
                    print("| [0] Kembali         |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| Mencari nilai : terkecil")
                    terkecil = 9999
                    for angka in (isi) :
                        if angka < terkecil:
                            terkecil = angka
                    print("| Nilai yang terkecil adalah", terkecil,"\n")
                    back_menu()
                elif cari == 2:
                    clear_screen()
                    print("Data sekarang:",isi)
                    print("#5 Mencari nilai;")
                    print("_______________________")
                    print("| [1] Nilai terkecil  |")
                    print("| [#] Nilai terbsesar |")
                    print("| [0] Kembali         |")
                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("| Mencari nilai : terbsesar")
                    terbesar = -9999
                    for angka in (isi) :
                        if angka > terbesar:
                            terbesar = angka
                    print("| Nilai yang terbesar adalah", terbesar,"\n")
                    back_menu()
                else:
                    print("|")
                    print("| Input tidak valid!")
                    input("| Coba lagi...")
            except ValueError:
                print("|")
                print("| Input tidak valid!")
                input("| Coba lagi...")

# Jumlah data

    elif menu == "6":
        clear_screen()
        print("Data sekarang:",isi)
        print("_______________________________________")
        print("| [1] Menambahkan data                |")
        print("| [2] Menghapus data                  |")
        print("| [3] Mengganti data                  |")
        print("| [4] Mengurutkan data                |")
        print("| [5] Cari nilai min dan maks pd data |")
        print("| [#] Menghitung banyak data          |")
        print("| [7] Membalik urutan data            |")
        print("| [0] Keluar                          |")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("| #6 Menghitung banyak data")
        print("| Data sekarang :",isi)
        print("| Banyak data ada",len(isi),"\n")
        back_menu()

# Balik data

    elif menu == "7":
        clear_screen()
        print("Data sekarang:",isi)
        print("_______________________________________")
        print("| [1] Menambahkan data                |")
        print("| [2] Menghapus data                  |")
        print("| [3] Mengganti data                  |")
        print("| [4] Mengurutkan data                |")
        print("| [5] Cari nilai min dan maks pd data |")
        print("| [6] Menghitung banyak data          |")
        print("| [#] Membalik urutan data            |")
        print("| [0] Keluar                          |")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("| #7 Membalik urutan data")
        print("| Data sekarang :",isi)
        isi.reverse()
        print("| Data dibalik  :",isi,"\n")
        back_menu()

# Tidak valid

    else:
        print("| Input tidak valid!")
        input("| Coba lagi...")
        utama()

# LUAR DATA

def back_menu():
    input("Tekan Enter untuk kembali...")
    clear_screen()
    utama()

if __name__ == "__main__":
    clear_screen()
    print("      PROGRAM MENU DATA     ")
    print("by Rausyanfikr Adi Karmayoga")
    print("      --2009106020--        ")
    time.sleep(1)
    clear_screen()
    isi = [17, 11, 2, 3, -14, 285]
    utama()
