import os
import time
#CLS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#CETAK
def cetak1(isi,total):
    clear_screen()
    print("[Belum ada daftar belanja]")
    cetak(isi,total)
#CETAK1
def cetak2(isi,total):
    clear_screen()
    print("Daftar belanjaan saat ini:")
    for ini in isi:
        print("- "+ini)
    print("--Total harga = Rp",total)
    print("")
    cetak(isi,total)
#CETAK2
def cetak(isi,total):
    print("---Toko Percetakan SHIAN---")
    print("___________________________")
    print("| [01] Cetak Spanduk      |")
    print("| [02] Cetak Stiker       |")
    print("| [03] Cetak Brosur       |")
    print("| [04] Cetak Poster       |")
    print("| [05] Cetak Kalender     |")
    print("| [00] Edit daftar        |")
    print("| [99] Ambil diskon       |")
    print("| [##] Enter untuk keluar |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    cetak = str(input("Masukkan pilihan : "))
    if cetak == "0" or cetak == "00":
        if total == 0:
            print("\nBelum ada daftar belanja")
            print("Tidak dapat mengedit daftar")
            input("Tekan Enter untuk kembali...")
            cetak1(isi,total)
        elif total > 0:
            edit_daftar(isi,total)
    elif cetak == "1" or cetak == "01":
        cetak_spanduk(isi,total)
    elif cetak == "2" or cetak == "02":
        cetak_stiker(isi,total)
    elif cetak == "3" or cetak == "03":
        cetak_brosur(isi,total)
    elif cetak == "4" or cetak == "04":
        cetak_poster(isi,total)
    elif cetak == "5" or cetak == "05":
        cetak_kalender(isi,total)
    elif cetak == "9" or cetak == "99":
        if total == 0:
            print("\nBelum ada daftar belanja")
            print("Tidak dapat mengambil diskon")
            input("Tekan Enter untuk kembali...")
            cetak1(isi,total)
        elif total > 0:
            ambil_diskon(isi,total)
    else:
        if total == 0:
            clear_screen()
            print("[Belum ada daftar belanja]")
            print("---Toko Percetakan SHIAN---")
            print("___________________________")
            print("| [01] Cetak Spanduk      |")
            print("| [02] Cetak Stiker       |")
            print("| [03] Cetak Brosur       |")
            print("| [04] Cetak Poster       |")
            print("| [05] Cetak Kalender     |")
            print("| [00] Edit daftar        |")
            print("| [99] Ambil diskon       |")
            print("| [##] Enter untuk keluar |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("Keluar program...")
            time.sleep(0)
            exit()
        elif total > 0:
            clear_screen()
            print("Daftar belanjaan saat ini:")
            for ini in isi:
                print("- "+ini)
            print("--Total harga = Rp",total)
            print("")
            print("---Toko Percetakan SHIAN---")
            print("___________________________")
            print("| [01] Cetak Spanduk      |")
            print("| [02] Cetak Stiker       |")
            print("| [03] Cetak Brosur       |")
            print("| [04] Cetak Poster       |")
            print("| [05] Cetak Kalender     |")
            print("| [00] Edit daftar        |")
            print("| [##] Enter untuk keluar |")
            print("| [99] Ambil diskon       |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("Keluar program...")
            time.sleep(0)
            exit()
#EDIT_DAFTAR
def edit_daftar(isi,total):
    clear_screen()
    if total == 0:
        print("[Belum ada daftar belanja]")
    elif total > 0:
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
    print("\n--Edit daftar--")
    print("_____________________________________")
    print("| [01] Mengganti daftar belanja     |")
    print("| [02] Menghapus daftar belanja     |")
    print("| [03] Sorting   daftar belanja     |")
    print("| [04] Min & Max daftar belanja     |")
    print("| [05] Menambah  daftar belanja     |")
    print("| [06] Menghapus banyaknya daftar   |")
    print("| [07] Menambah dengan nomor daftar |")
    print("| [08] Menghitung banyak daftar     |")
    print("| [09] Menghapus semua daftar       |")
    print("| [10] Hapus daftar yang sama       |")
    print("| [00] Kembali                      |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    edit = str(input("Masukkan pilihan edit: "))
    if edit == '0' or edit == '00':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif edit == '1' or edit == '01':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("Daftar belanjaan saat ini:")
                    i = 0
                    for ini in isi:
                        i += 1
                        print(i,ini)
                    print("\n--Ganti daftar--")
                    gnt = int(input("Masukkan nomor daftar: "))
                    gant = gnt-1
                    print("Daftar yang di ganti :\n{0} {1}".format(gnt,isi[gant]))
                    ganti = str(input("Masukkan daftar baru : \n"))
                    isi[gant] = ganti
                    print("\nDaftar belanja baru :")
                    j = 0
                    for ini in isi:
                        j += 1
                        print(j,ini)
                    input("\nTekan Enter untuk kembali...")
                    edit_daftar(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
            except IndexError:
                print("\nIndeks yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif edit == '2' or edit == '02':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("Daftar belanjaan saat ini:")
                    i = 0
                    for ini in isi:
                        i += 1
                        print(i,ini)
                    print("\n--Hapus daftar--")
                    nmr = int(input("Masukkan nomor list : "))
                    nomor = nmr-1
                    print("Data yang di hapus :\n{0} {1}".format(nmr,isi[nomor]))
                    isi.pop(nomor)
                    print("\nDaftar belanja baru :")
                    j = 0
                    for ini in isi:
                        j += 1
                        print(j,ini)
                    input("\nTekan Enter untuk kembali...")
                    edit_daftar(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
            except IndexError:
                print("\nIndeks yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif edit == '3' or edit == '03':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Sorting daftar--")
        print("[1] Ascending")
        print("[2] Descending")
        sort = str(input("Masukkan pilihan sorting : "))
        if sort == '1':
            isi.sort()
            print("\nDaftar belanja baru :")
            j = 0
            for ini in isi:
                j += 1
                print(j,ini)
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
        elif sort == '2':
            isi.sort()
            isi.reverse()
            print("\nDaftar belanja baru :")
            k = 0
            for ini in isi:
                k += 1
                print(k,ini)
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
    elif edit == '4' or edit == '04':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Min & Max--")
        print("[1] Mencari nilai min")
        print("[2] Mencari nilai max")
        cari = str(input("Masukkan pilihan : "))
        if cari == '1':
            kecil = min(isi)
            print("Nilai min = "+kecil)
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
        elif cari == '2':
            besar = max(isi)
            print("Nilai max = "+besar)
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
    elif edit == '5' or edit == '05':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Menambah daftar--")
        berenti = False
        j = 1
        data_baru = []
        while (not berenti):
            data_baru = str(input("Masukkan daftar ke-{0} ".format(j)))
            isi.extend([data_baru])
            j += 1
            ask = input("Input 0 jika cukup : ")
            if ask == '0':
                berenti = True
        print("\nDaftar belanja baru :")
        k = 0
        for ini in isi:
            k += 1
            print(k,ini)
        input("\nTekan Enter untuk kembali...")
        edit_daftar(isi,total)
    elif edit == '6' or edit == '06':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("Daftar belanjaan saat ini:")
                    i = 0
                    for ini in isi:
                        i += 1
                        print(i,ini)
                    print("\n--Menghapus banyak daftar--")
                    hapus1 = int(input("Menghapus dari daftar  : "))
                    hapus = hapus1-1
                    hapus2 = int(input("Menghapus hingga daftar: "))
                    del isi[hapus:hapus2]
                    print("\nDaftar belanja baru :")
                    j = 0
                    for ini in isi:
                        j += 1
                        print(j,ini)
                    input("\nTekan Enter untuk kembali...")
                    edit_daftar(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
            except IndexError:
                print("\nIndeks yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif edit == '7' or edit == '07':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("Daftar belanjaan saat ini:")
                    i = 0
                    for ini in isi:
                        i += 1
                        print(i,ini)
                    print("\n--Menambah dengan nomor daftar--")
                    tambah = int(input("Masukkan nomor daftar : "))
                    tambah1 = tambah-1
                    tambah2 = str(input("Masukkan daftar baru  : "))
                    isi.insert(tambah1,tambah2)
                    print("\nDaftar belanja baru :")
                    j = 0
                    for ini in isi:
                        j += 1
                        print(j,ini)
                    input("\nTekan Enter untuk kembali...")
                    edit_daftar(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif edit == '8' or edit == '08':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Menghitung banyak daftar--")
        print("Banyak daftar belanjaan ada : ",len(isi))
        input("\nTekan Enter untuk kembali...")
        edit_daftar(isi,total)
    elif edit == '9' or edit == '09':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Menghapus semua daftar--")
        print("Konfirmasi:")
        yakin = str(input("Yakin ingin menghapus semua daftar? (y/t) "))
        if yakin == 'y':
            print("Menghapus daftar...")
            time.sleep(2)
            isi.clear()
            total = 0
            print("Daftar berhasil dhapus!")
            input("\nTekan Enter untuk kembali...")
            cetak1(isi,total)
        elif yakin == 't':
            print("Menghapus semua daftar dibatalkan.")
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            edit_daftar(isi,total)
    elif edit == '10':
        clear_screen()
        print("Daftar belanjaan saat ini:")
        i = 0
        for ini in isi:
            i += 1
            print(i,ini)
        print("\n--Menghapus daftar yang sama--")
        input("Tekan Enter untuk melanjutkan...")
        print("Menghapus...")
        time.sleep(2)
        #SET
        set = {0}
        for ini in isi:
            set.add(ini)
        set.remove(0)
        print("Daftar berhasil dhapus!")
        print("\nDaftar belanja baru:")
        i = 0
        for ini in set:
            i += 1
            print(i,ini)
        isi = set
        input("\nTekan Enter untuk kembali...")
        edit_daftar(isi,total)
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        edit_daftar(isi,total)
#CETAK_SPANDUK
def cetak_spanduk(isi,total):
    clear_screen()
    print("--Cetak Spanduk--")
    print("Jenis spanduk:")
    print("[1] Spanduk Flexi Cina")
    print("[2] Spanduk Flexi Korea")
    print("[0] Kembali")
    spanduk = str(input("Masukkan jenis spanduk : "))
    if spanduk == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif spanduk == '1':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Spanduk--")
                    print("Jenis spanduk:")
                    print("[#] Spanduk Flexi Cina")
                    print("[2] Spanduk Flexi Korea")
                    print("[0] Kembali")
                    print("Masukkan jenis spanduk : 1")
                    print("\nFlexi Cina 280gsm")
                    print("Harga spanduk 20k/meter")
                    ukuran = int(input("Masukkan panjang spanduk : "))
                    print("\nDaftar belanja baru:")
                    harga_spanduk = lambda ukuran: ukuran*20000
                    spanduk1 = ("Flexi China 260gsm ; {0} Meter      ; Harga Rp.{1}".format(ukuran,harga_spanduk(ukuran)))
                    isi.append(spanduk1)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_spanduk(ukuran)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif spanduk == '2':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Spanduk--")
                    print("Jenis spanduk:")
                    print("[1] Spanduk Flexi Cina")
                    print("[#] Spanduk Flexi Korea")
                    print("[0] Kembali")
                    print("Masukkan jenis spanduk : 2")
                    print("\nFlexi Korea 440gsm")
                    print("Harga spanduk 45k/meter")
                    ukuran = int(input("Panjang spanduk : "))
                    print("\nDaftar belanja baru:")
                    harga_spanduk = lambda ukuran : ukuran*45000
                    spanduk2 = ("Flexi Korea 440gsm ; {0} Meter      ; Harga Rp.{1}".format(ukuran,harga_spanduk(ukuran)))
                    isi.append(spanduk2)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_spanduk(ukuran)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        cetak_spanduk(isi,total)
#CETAK_STIKER
def cetak_stiker(isi,total):
    clear_screen()
    print("--Cetak Stiker--")
    print("Jenis stiker:")
    print("Ukuran A3+")
    print("[1] Stiker Bontax")
    print("[2] Stiker Vinyl Doff")
    print("[3] Stiker Transparan")
    print("[0] Kembali")
    stiker = str(input("Pilih jenis stiker : "))
    if stiker == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif stiker == '1':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Stiker--")
                    print("Jenis stiker:")
                    print("Ukuran A3+")
                    print("[#] Stiker Bontax")
                    print("[2] Stiker Vinyl Doff")
                    print("[3] Stiker Transparan")
                    print("[0] Kembali")
                    print("Pilih jenis stiker : 1")
                    print("\nStiker Bontax")
                    print("Uk. A3+ 5k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*5000
                    stiker1 = ("Stiker Bontax  A3+ ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(stiker1)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif stiker == '2':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Stiker--")
                    print("Jenis stiker:")
                    print("Ukuran A3+")
                    print("[1] Stiker Bontax")
                    print("[#] Stiker Vinyl Doff")
                    print("[3] Stiker Transparan")
                    print("[0] Kembali")
                    print("Pilih jenis stiker : 2")
                    print("\nStiker Vinyl Doff")
                    print("Uk. A3+ 7k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*7000
                    stiker2 = ("Stiker Vinyl   A3+ ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(stiker2)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif stiker == '3':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Stiker--")
                    print("Jenis stiker:")
                    print("Ukuran A3+")
                    print("[1] Stiker Bontax")
                    print("[2] Stiker Vinyl Doff")
                    print("[#] Stiker Transparan")
                    print("[0] Kembali")
                    print("Pilih jenis stiker : 3")
                    print("\nStiker Transparan")
                    print("Uk. A3+ 10k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*10000
                    stiker3 = ("Stiker Transp. A3+ ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(stiker3)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        cetak_stiker(isi,total)
#CETAK_BROSUR
def cetak_brosur(isi,total):
    clear_screen()
    print("--Cetak Brosur--")
    print("Jenis Brosur:")
    #DICTIONARY
    mydict = {1:["[1] Art Paper 100gr","[2] Art Paper 120gr","[3] Art Paper 150gr"]}
    for dict in mydict[1]:
        print(dict)
    print("[0] Kembali")
    #DICTIONARY
    squares = {1:[420000,422500], 2:[432000,434250], 3:[445000,447500]}
    #TUPLE
    tuple = ("Brosur 100gr A5", "Brosur 120gr A5", "Brosur 150gr A5")
    #Unpacking TUPLE
    tuple2 = "1","2",'3'
    a, b, c = tuple2
    brosur = str(input("Masukkan jenis brosur : "))
    if brosur == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif brosur == '1':
        jenis = a
        brosur = tuple[0]
        brosurs1 = squares[1][0]
        brosurs2 = squares[1][1]
        clear_screen()
        print("--Cetak Brosur--")
        print("Jenis Brosur:")
        mydict.update({1:["[#] Art Paper 100gr","[2] Art Paper 120gr","[3] Art Paper 150gr"]})
        for dict in mydict[1]:
            print(dict)
        print("[0] Kembali")
        print("Masukkan jenis brosur : "+jenis+"\n")
        print(brosur)
        print("Opsi cetak 1/2 sisi")
        sisi = str(input("Masukkan opsi pilihan : "))
        if sisi == '0':
            cetak_brosur(isi,total)
        elif sisi == '1':
            sisi1(isi,total,brosurs1,brosur,jenis,mydict)
        elif sisi == '2':
            sisi2(isi,total,brosurs2,brosur,jenis,mydict)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            cetak_brosur(isi,total)
    elif brosur == '2':
        jenis = b
        brosur = tuple[1]
        brosurs1 = squares[2][0]
        brosurs2 = squares[2][1]
        clear_screen()
        print("--Cetak Brosur--")
        print("Jenis Brosur:")
        mydict.update({1:["[1] Art Paper 100gr","[#] Art Paper 120gr","[3] Art Paper 150gr"]})
        for dict in mydict[1]:
            print(dict)
        print("[0] Kembali")
        print("Masukkan jenis brosur : "+jenis+"\n")
        print(brosur)
        print("Opsi cetak 1/2 sisi")
        sisi = str(input("Masukkan opsi pilihan : "))
        if sisi == '0':
            cetak_brosur(isi,total)
        elif sisi == '1':
            sisi1(isi,total,brosurs1,brosur,jenis,mydict)
        elif sisi == '2':
            sisi2(isi,total,brosurs2,brosur,jenis,mydict)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            cetak_brosur(isi,total)
    elif brosur == '3':
        jenis = c
        brosur = tuple[2]
        brosurs1 = squares[3][0]
        brosurs2 = squares[3][1]
        clear_screen()
        print("--Cetak Brosur--")
        print("Jenis Brosur:")
        mydict.update({1:["[1] Art Paper 100gr","[2] Art Paper 120gr","[#] Art Paper 150gr"]})
        for dict in mydict[1]:
            print(dict)
        print("[0] Kembali")
        print("Masukkan jenis brosur : "+jenis+"\n")
        print(brosur)
        print("Opsi cetak 1/2 sisi")
        sisi = str(input("Masukkan opsi pilihan : "))
        if sisi == '0':
            cetak_brosur(isi,total)
        elif sisi == '1':
            sisi1(isi,total,brosurs1,brosur,jenis,mydict)
        elif sisi == '2':
            sisi2(isi,total,brosurs2,brosur,jenis,mydict)
        else:
            print("Input tidak valid!")
            input("\nTekan Enter untuk kembali...")
            cetak_brosur(isi,total)
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        cetak_brosur(isi,total)
#BROSUR_S1
def sisi1(isi,total,brosurs1,brosur,jenis,mydict):
    EROR = True
    while(EROR):
        try:
            salah = True
            while(salah):
                clear_screen()
                print("--Cetak Brosur--")
                print("Jenis Brosur:")
                for dict in mydict[1]:
                    print(dict)
                print("[0] Kembali")
                print("Masukkan jenis brosur : "+jenis+"\n")
                print(brosur+" 1 sisi")
                print("1 rim = Rp",brosurs1,"/500lbr")
                rim = int(input("Masukkan banyak rim : "))
                print("\nDaftar belanja baru:")
                harga_brosur = lambda rim: rim*brosurs1
                sisi1 = (brosur+"    ; {0} Rim 1 sisi ; Harga Rp.{1}".format(rim,harga_brosur(rim)))
                isi.append(sisi1)
                for ini in isi:
                    print("- "+ini)
                total = total+harga_brosur(rim)
                print("--Total harga = Rp",total)
                input("\nTekan Enter untuk kembali...")
                cetak2(isi,total)
        except ValueError:
            print("\nInput yang dimasukkan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")
            clear_screen()
#BROSUR_S2
def sisi2(isi,total,brosurs2,brosur,jenis,mydict):
    EROR = True
    while(EROR):
        try:
            salah = True
            while(salah):
                clear_screen()
                print("--Cetak Brosur--")
                print("Jenis Brosur:")
                for dict in mydict[1]:
                    print(dict)
                print("[0] Kembali")
                print("Masukkan jenis brosur : "+jenis+"\n")
                print(brosur+" 2 sisi")
                print("1 rim = Rp",brosurs2,"/500lbr")
                rim = int(input("Masukkan banyak rim : "))
                print("\nDaftar belanja baru:")
                harga_brosur = lambda rim: rim*brosurs2
                sisi2 = (brosur+"    ; {0} Rim 2 sisi ; Harga Rp.{1}".format(rim,harga_brosur(rim)))
                isi.append(sisi2)
                for ini in isi:
                    print("- "+ini)
                total = total+harga_brosur(rim)
                print("--Total harga = Rp",total)
                input("\nTekan Enter untuk kembali...")
                cetak2(isi,total)
        except ValueError:
            print("\nInput yang dimasukkan tidak valid!")
            input("Tekan Enter untuk mencoba lagi...")
            clear_screen()
#CETAK_POSTER
def cetak_poster(isi,total):
    clear_screen()
    print("--Cetak Poster--")
    print("Jenis Poster:")
    print("Ukuran A3+")
    print("[1] Art Paper 210gr")
    print("[2] Art Paper 230gr")    
    print("[3] Art Paper 260gr")
    print("[0] Kembali")
    poster = str(input("Pilih jenis poster : "))
    if poster == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif poster == '1':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Poster--")
                    print("Jenis Poster:")
                    print("Ukuran A3+")
                    print("[#] Art Paper 210gr")
                    print("[2] Art Paper 230gr")    
                    print("[3] Art Paper 260gr")
                    print("[0] Kembali")
                    print("Pilih jenis poster : 1")
                    print("\nPoster Art Paper 210gr")
                    print("Uk. A3+ 5k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*5000
                    poster1 = ("Poster 210gr A3+   ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(poster1)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif poster == '2':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Poster--")
                    print("Jenis Poster:")
                    print("Ukuran A3+")
                    print("[1] Art Paper 210gr")
                    print("[#] Art Paper 230gr")    
                    print("[3] Art Paper 260gr")
                    print("[0] Kembali")
                    print("Pilih jenis poster : 2")
                    print("\nPoster Art Paper 230gr") 
                    print("Uk. A3+ 7k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*7000
                    poster2 = ("Poster 230gr A3+   ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(poster2)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif poster == '3':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Poster--")
                    print("Jenis Poster:")
                    print("Ukuran A3+")
                    print("[1] Art Paper 210gr")
                    print("[2] Art Paper 230gr")    
                    print("[#] Art Paper 260gr")
                    print("[0] Kembali")
                    print("Pilih jenis poster : 3")
                    print("\nPoster Art Paper 260gr") 
                    print("Uk. A3+ 10k/lembar")
                    lembar = int(input("Berapa lembar : "))
                    print("\nDaftar belanja baru:")
                    harga_lembar = lambda lembar: lembar*10000
                    poster3 = ("Poster 260gr A3+   ; {0} Lembar     ; Harga Rp.{1}".format(lembar,harga_lembar(lembar)))
                    isi.append(poster3)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_lembar(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        cetak_poster(isi,total)
#CETAK_KALENDER
def cetak_kalender(isi,total):
    clear_screen()
    print("--Cetak Kalender--")
    print("Pilihan Kalender:")
    print("Ukuran A3+")
    print("[1] Kalender 12 lbr")   
    print("[2] Kalender  6 lbr") 
    print("[3] Kalender  4 lbr") 
    print("[4] Kalender  3 lbr") 
    print("[5] Kalender  2 lbr") 
    print("[6] Kalender  1 lbr")
    print("[0] Kembali")
    kalender = str(input("Pilih jenis kalender : "))
    if kalender == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif kalender == '1':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[#] Kalender 12 lbr")   
                    print("[2] Kalender  6 lbr") 
                    print("[3] Kalender  4 lbr") 
                    print("[4] Kalender  3 lbr") 
                    print("[5] Kalender  2 lbr") 
                    print("[6] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 1")
                    print("==========")
                    print("Kalender 12 lembar")
                    print("Art Paper 120gr A3+")
                    print("Klep plat seng")
                    print("1 Kalender 12lbr = Rp.22680")
                    lembar = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*22680
                    lembar1 = ("Kalender 120gr A3+ ; 12 lbr {0} pcs  ; Harga Rp.{1}".format(lembar,harga_kalender(lembar)))
                    print("\nDaftar belanja baru:")
                    isi.append(lembar1)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif kalender == '2':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[1] Kalender 12 lbr")   
                    print("[#] Kalender  6 lbr") 
                    print("[3] Kalender  4 lbr") 
                    print("[4] Kalender  3 lbr") 
                    print("[5] Kalender  2 lbr") 
                    print("[6] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 2")
                    print("==========")
                    print("Kalender 6 lembar")
                    print("Art Paper 120gr A3+")
                    print("Klep plat seng")
                    print("1 Kalender 6lbr = Rp.12720")
                    lembar = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*12720
                    lembar2 = ("Kalender 120gr A3+ ; 6 lbr {0} pcs  ; Harga Rp.{1}".format(lembar,harga_kalender(lembar)))
                    print("\nDaftar belanja baru:")
                    isi.append(lembar2)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif kalender == '3':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[1] Kalender 12 lbr")   
                    print("[2] Kalender  6 lbr") 
                    print("[#] Kalender  4 lbr") 
                    print("[4] Kalender  3 lbr") 
                    print("[5] Kalender  2 lbr") 
                    print("[6] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 3")
                    print("==========")
                    print("Kalender 4 lembar")
                    print("Art Paper 120gr A3+")
                    print("Klep plat seng")
                    print("1 Kalender 4lbr = Rp.9360")
                    lembar = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*9360
                    lembar3 = ("Kalender 120gr A3+ ; 4 lbr {0} pcs  ; Harga Rp.{1}".format(lembar,harga_kalender(lembar)))
                    print("\nDaftar belanja baru:")
                    isi.append(lembar3)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif kalender == '4':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[1] Kalender 12 lbr")   
                    print("[2] Kalender  6 lbr") 
                    print("[3] Kalender  4 lbr") 
                    print("[#] Kalender  3 lbr") 
                    print("[5] Kalender  2 lbr") 
                    print("[6] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 4")
                    print("==========")
                    print("Kalender 3 lembar")
                    print("Art Paper 120gr A3+")
                    print("Klep plat seng")
                    print("1 Kalender 3lbr = Rp.7200")
                    lembar = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*7200
                    lembar4 = ("Kalender 120gr A3+ ; 3 lbr {0} pcs  ; Harga Rp.{1}".format(lembar,harga_kalender(lembar)))
                    print("\nDaftar belanja baru:")
                    isi.append(lembar4)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif kalender == '5':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[1] Kalender 12 lbr")   
                    print("[2] Kalender  6 lbr") 
                    print("[3] Kalender  4 lbr") 
                    print("[4] Kalender  3 lbr") 
                    print("[#] Kalender  2 lbr") 
                    print("[6] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 5")
                    print("==========")
                    print("Kalender 2 lembar")
                    print("Art Paper 120gr A3+")
                    print("Klep plat seng")
                    print("1 Kalender 3lbr = Rp.5400")
                    lembar = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*5400
                    lembar5 = ("Kalender 120gr A3+ ; 2 lbr {0} pcs  ; Harga Rp.{1}".format(lembar,harga_kalender(lembar)))
                    print("\nDaftar belanja baru:")
                    isi.append(lembar5)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(lembar)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    elif kalender == '6':
        EROR = True
        while(EROR):
            try:
                salah = True
                while(salah):
                    clear_screen()
                    print("--Cetak Kalender--")
                    print("Pilihan Kalender:")
                    print("Ukuran A3+")
                    print("[1] Kalender 12 lbr")   
                    print("[2] Kalender  6 lbr") 
                    print("[3] Kalender  4 lbr") 
                    print("[4] Kalender  3 lbr") 
                    print("[5] Kalender  2 lbr") 
                    print("[#] Kalender  1 lbr")
                    print("[0] Kembali")
                    print("Pilih jenis kalender : 6")
                    print("==========")
                    print("Kalender 1 lembar")
                    print("Art Paper 260gr A3+")
                    print("Lubang mata ayam")
                    print("1 Kalender 1lbr = Rp.3840")
                    kalend = int(input("Masukkan banyak kalender : "))
                    harga_kalender = lambda lembar: lembar*3840
                    kalend2 = ("Kalender 260gr A3+ ; 1 lbr {0} pcs  ; Harga Rp.{1}".format(kalend,harga_kalender(kalend)))
                    print("\nDaftar belanja baru:")
                    isi.append(kalend2)
                    for ini in isi:
                        print("- "+ini)
                    total = total+harga_kalender(kalend)
                    print("--Total harga = Rp",total)
                    input("\nTekan Enter untuk kembali...")
                    cetak2(isi,total)
            except ValueError:
                print("\nInput yang dimasukkan tidak valid!")
                input("Tekan Enter untuk mencoba lagi...")
                clear_screen()
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        cetak_kalender(isi,total)
#DISKON
def ambil_diskon(isi,total):
    clear_screen()
    print("--Total harga belanjaan anda = Rp",total)
    print("\n--Ambil Diskon--")
    print("(1) Diskon 20% minimal total belanja Rp.100K")
    print("(2) Diskon 29% minimal total belanja Rp.230K")
    print("(3) Diskon 50% minimal total belanja Rp.500K")
    print("[0] Kembali")
    diskon = str(input("Ambil diskon : "))
    if diskon == '0':
        if total == 0:
            clear_screen()
            cetak1(isi,total)
        elif total > 0:
            clear_screen()
            cetak2(isi,total)
    elif diskon == '1':
        if total > 230000:
            print("Belanjaan anda lebih dari Rp.230k")
            print("Anda disarankan mengambil diskon 29%/15%!")
            input("\nTekan Enter untuk kembali...")
            ambil_diskon(isi,total)
        elif total >= 100000:
            total1 = total
            print("\n--Total harga saat ini = Rp",total1)
            total = (lambda x:x*20/100)(total1)
            print("--Total harga baru     = Rp",total)
            print("- Anda berhasil mendapat diskon 20%!")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
        else:
            print("Tidak dapat mengambil diskon!")
            print("Belanjaan anda kurang dari Rp.100k")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
    elif diskon == '2':
        if total > 500000:
            print("Belanjaan anda lebih dari Rp.500k")
            print("Anda disarankan mengambil diskon 50%!")
            input("\nTekan Enter untuk kembali...")
            ambil_diskon(isi,total)
        elif total >= 230000:
            total1 = total
            print("\n--Total harga saat ini = Rp",total1)
            total = (lambda x:x*29/100)(total1)
            print("--Total harga baru     = Rp",total)
            print("- Anda berhasil mendapat diskon 29%!")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
        else:
            print("Tidak dapat mengambil diskon!")
            print("Belanjaan anda kurang dari Rp.230k")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
    elif diskon == '3':
        if total >= 500000:
            total1 = total
            print("\n--Total harga saat ini = Rp",total1)
            total = (lambda x:x*50/100)(total1)
            print("--Total harga baru     = Rp",total)
            print("- Anda berhasil mendapat diskon 50%!")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
        else:
            print("Tidak dapat mengambil diskon!")
            print("Belanjaan anda kurang dari Rp.500k")
            input("\nTekan Enter untuk kembali...")
            cetak2(isi,total)
    else:
        print("Input tidak valid!")
        input("\nTekan Enter untuk kembali...")
        ambil_diskon(isi,total)
#MAIN
if __name__ == "__main__":
    clear_screen()
    print("    --SHIAN PRINTING--    ")
    print("by Rausyanfikr ; 2009106020")
    time.sleep(0.5)
    isi = []
    total = 0
    clear_screen()
    cetak1(isi,total)