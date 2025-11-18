import json
from format_style import format_styles
from colorama import Fore, Style, init

init(autoreset=True)

daftar_pustaka = []

def simpan_data():
    with open("daftar_pustaka.json", "w", encoding="utf-8") as f:
        json.dump(daftar_pustaka, f, ensure_ascii=False, indent=4)

def muat_data():
    global daftar_pustaka
    try:
        with open("daftar_pustaka.json", "r", encoding="utf-8") as f:
            daftar_pustaka = json.load(f)
    except FileNotFoundError:
        daftar_pustaka = []


def pilih_referensi():
    print(Fore.GREEN + "Tipe Referensi:")
    print(Fore.GREEN + "1. Journal/Article")
    print(Fore.GREEN + "2. Book")
    print(Fore.GREEN + "3. Book Section")

    while True:
        try:
            tipe_ref = int(input("Pilih tipe referensi (1/2/3): "))

            if tipe_ref == 1:
                print(Fore.YELLOW + "Kamu memilih : Journal/Article\n")
                return "Journal/Article"
            elif tipe_ref == 2:
                print(Fore.YELLOW + "Kamu memilih : Book\n")
                return "Book"
            elif tipe_ref == 3:
                print(Fore.YELLOW + "Kamu memilih : Book Section\n")
                return "Book Section"
            else:
                print(Fore.RED + "Masukan tidak valid! Pilih 1, 2 atau 3.\n")
        except ValueError:
            print(Fore.RED + "Masukan Angka bukan huruf\n")


def masukan_style():
    styles = ["APA", "IEEE", "MLA", "Harvard", "Vancouver"]
    print("="*100)
    print("\nPilih gaya sitasi:")
    for i, data in enumerate(styles, start=1):
        print(Fore.GREEN + f"{i}. {data}")

    while True:
        try:
            pilihan = int(input("Pilih Style (1-5): "))
            if 1 <= pilihan <= len(styles):
                print(Fore.YELLOW + f"Style yang dipilih: {styles[pilihan-1]}")
                return styles[pilihan-1]
            else:
                print(Fore.RED + "Masukkan angka 1 sampai 5.")
        except ValueError:
            print(Fore.RED + "Masukkan angka bukan huruf.")

def masukan_data():
    print(Fore.YELLOW + "-"*100)
    print(Fore.GREEN + f"{'Masukkan Data Daftar Pustaka':^100}")
    print(Fore.YELLOW + "-"*100)
    authors = []
    editors = []
    editors_booksection = []

    tipe = pilih_referensi()
    gaya = masukan_style()
    judul = input("Masukkan Judul : ")

    print("Masukan Nama Penulis [Format : Last name, First name (e.g. Prasetya, Erdi)]")
    while True:
        nama = input(f"Penulis {len(authors)+1}: ")
        if nama.strip() == "":
            print("Nama tidak boleh kosong.")
            continue
        authors.append(nama.title().strip())
        while True:
            tambah = input("Apakah ingin menambah penulis lain? (y/n): ").lower().strip()
            if tambah == "y":
                break
            elif tambah == "n":
                print("\nInput penulis selesai.\n")
                break
            else:
                print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")

        if tambah == "n":
            break 

    while True:
        try:   
            tahun = int(input("Masukkan Tahun : "))
            break
        except ValueError:
            print("Tahun harus berupa angka")

    halaman = (input("Halaman [from-to] : "))
    volume = (input("Volume : "))

    if tipe == "Journal/Article":
        jurnal = input("masukkan jurnal : ")
        issue = input("Issue : ")
    elif tipe == "Book":
        edition = input("Edition : ")
        print("Masukan Nama Editor [Format : Last name, First name (e.g. Prasetya, Erdi)]")
        while True:
            namaeditor = input(f"Editor {len(editors)+1}: ")
            if namaeditor.strip() == "":
                break

            editors.append(namaeditor.title().strip())
            while True:
                tambaheditor = input("Apakah ingin menambah editor yang lain? (y/n): ").lower().strip()
                if tambaheditor == "y":
                    break
                elif tambaheditor == "n":
                    print("\nInput editor selesai.\n")
                    break
                else:
                    print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")

            if tambaheditor == "n":
                break

        city = input("City : ")
        publisher = input("Publisher : ")
    else:
        book = input("Book : ")
        edition = input("Edition : ")

        print("Masukan Nama Editor [Format : Last name, First name (e.g. Prasetya, Erdi)]")
        while True:
            namaeditor = input(f"Editor {len(editors_booksection)+1}: ")
            if namaeditor.strip() == "":
                break

            editors_booksection.append(namaeditor.title())
            while True:
                tambaheditor = input("Apakah ingin menambah editor yang lain? (y/n): ").lower().strip()
                if tambaheditor == "y":
                    break
                elif tambaheditor == "n":
                    print("\nInput editor selesai.\n")
                    break
                else:
                    print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")

            if tambaheditor == "n":
                break
        city = input("City : ")
        publisher = input("Publisher : ")
        chapter = input("Chapter Number : ")
    link = input("Link URL/DOI : ")

    data = {
    "referensi": tipe,
    "style": gaya,
    "judul": judul,
    "authors": authors.copy(),
    "tahun": tahun,
    "jurnal": jurnal if tipe=="Journal/Article" else "",
    "volume": volume,
    "issue": issue if tipe=="Journal/Article" else "",
    "halaman": halaman,
    "edition": edition if tipe!="Journal/Article" else "",
    "editors": editors.copy() if tipe=="Book" else editors_booksection.copy(),
    "city": city if tipe!="Journal/Article" else "",
    "publisher": publisher if tipe!="Journal/Article" else "",
    "chapter": chapter if tipe=="Book Section" else "",
    "link": link,
    "book": book if tipe == "Book Section" else ""
    }
    daftar_pustaka.append(data)

def ubah_data():
    if not daftar_pustaka:
        print(Fore.RED + "\nBelum ada data untuk diubah.\n")
        return

    print(Fore.MAGENTA + "\nDaftar Pustaka yang Tersimpan:")
    for i, data in enumerate(daftar_pustaka, start=1):
        print(Fore.CYAN + f"{i}. {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]")

    try:
        index = int(input(Fore.YELLOW + "\nPilih nomor data yang ingin diubah: " + Style.RESET_ALL)) - 1
        if index < 0 or index >= len(daftar_pustaka):
            print(Fore.RED + "Nomor tidak valid.\n")
            return
    except ValueError:
        print(Fore.RED + "Masukkan angka yang valid.\n")
        return

    data = daftar_pustaka[index]
    print(Fore.MAGENTA + f"\nMengubah data: {data['judul']} ({data['referensi']})\n")

    while True:
        print(Fore.MAGENTA + "\nPilih bagian yang ingin diubah:")
        print(Fore.CYAN + "1. Judul")
        print(Fore.CYAN + "2. Penulis")
        print(Fore.CYAN + "3. Tahun")
        print(Fore.CYAN + "4. Volume/Issue/Halaman")
        print(Fore.CYAN + "5. Style")
        print(Fore.CYAN + "6. Informasi Tambahan (tergantung tipe referensi)")
        print(Fore.CYAN + "7. Link")
        print(Fore.CYAN + "8. Selesai")

        pilihan = input(Fore.MAGENTA + "Masukkan pilihan (1-8): " + Style.RESET_ALL).strip()

        if pilihan == "1":
            data["judul"] = input("Masukkan judul baru: ").strip()

        elif pilihan == "2":
            authors_baru = []
            print("Masukkan ulang daftar penulis:")
            while True:
                nama = input(f"Penulis {len(authors_baru)+1}: ").strip()
                if not nama:
                    print("Nama tidak boleh kosong.")
                    continue
                authors_baru.append(nama.title())
                lagi = input("Tambah penulis lain? (y/n): ").lower().strip()
                if lagi == "n":
                    break
            data["authors"] = authors_baru

        elif pilihan == "3":
            try:
                data["tahun"] = int(input("Masukkan tahun baru: "))
            except ValueError:
                print("Tahun harus berupa angka.")

        elif pilihan == "4":
            volume_baru = input("Volume baru: ").strip()
            if volume_baru:
                data['volume'] = volume_baru
            issue_baru = input("Issue baru: ").strip()
            if issue_baru:
                data['issue'] = issue_baru
            hal_baru = input("Halaman baru: ").strip()
            if hal_baru:
                data['halaman'] = hal_baru

        elif pilihan == "5":
            data["style"] = masukan_style()

        elif pilihan == "6":
            if data["referensi"] == "Journal/Article":
                jurnal_baru = input(f"Nama jurnal baru : ").strip()
                if jurnal_baru:
                    data["jurnal"] = jurnal_baru

            elif data["referensi"] == "Book":
                edition_baru = input(f"Edition baru : ").strip()
                if edition_baru:
                    data["edition"] = edition_baru
                
                city_baru = input(f"City baru : ").strip()
                if city_baru:
                    data["city"] = city_baru

                pub_baru = input(f"Publisher baru : ").strip()
                if pub_baru:
                    data["publisher"] = pub_baru
                
                ubah_editor = input("Apakah ingin mengubah daftar editor? (y/n): ").lower().strip()
                if ubah_editor == "y":
                    editors_baru = []
                    print("Masukkan ulang daftar editor [format : last, first name]:")
                    while True:
                        nama = input(f"Editor {len(editors_baru)+1}: ").strip()
                        if not nama:
                            break
                        editors_baru.append(nama.title())
                        lagi = input("Tambah editor lain? (y/n): ").lower().strip()
                        if lagi == "n":
                            break
                    if editors_baru:
                        data["editors"] = editors_baru


            elif data["referensi"] == "Book Section":
                book_baru = input(f"Judul buku baru [{data.get('book','')}]: ").strip()
                if book_baru:
                    data["book"] = book_baru

                chapter_baru = input(f"Chapter baru [{data.get('chapter','')}]: ").strip()
                if chapter_baru:
                    data["chapter"] = chapter_baru

                ed_baru = input(f"Edition baru [{data.get('edition','')}]: ").strip()
                if ed_baru:
                    data["edition"] = ed_baru

                city_baru = input(f"City baru [{data.get('city','')}]: ").strip()
                if city_baru:
                    data["city"] = city_baru

                pub_baru = input(f"Publisher baru [{data.get('publisher','')}]: ").strip()
                if pub_baru:
                    data["publisher"] = pub_baru

                ubah_editor = input("Apakah ingin mengubah daftar editor? (y/n): ").lower().strip()
                if ubah_editor == "y":
                    editors_baru = []
                    print("Masukkan ulang daftar editor [Format : last, first name] :")
                    while True:
                        nama = input(f"Editor {len(editors_baru)+1}: ").strip()
                        if not nama:
                            break
                        editors_baru.append(nama.title())
                        lagi = input("Tambah editor lain? (y/n): ").lower().strip()
                        if lagi == "n":
                            break
                    if editors_baru:
                        data["editors"] = editors_baru

        elif pilihan == "7":
            data["link"] = input("Masukkan link baru: ").strip()

        elif pilihan == "8":
            print("\nPerubahan disimpan.\n")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

    daftar_pustaka[index] = data
    print("Data berhasil diperbarui!\n")

def hapus_data():
    if not daftar_pustaka:
        print(Fore.RED + "\nBelum ada data untuk dihapus.\n")
        return

    print(Fore.GREEN + "\nDaftar Pustaka yang Tersimpan:")
    for i, data in enumerate(daftar_pustaka, start=1):
        print(Fore.CYAN + f"{i}. {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]")

    try:
        index = int(input(Fore.YELLOW + "\nPilih nomor data yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(daftar_pustaka):
            print(Fore.RED + "Nomor tidak valid.\n")
            return
    except ValueError:
        print(Fore.RED + "Masukkan angka yang valid.\n")
        return

    data = daftar_pustaka[index]
    konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{data['judul']}'? (y/n): ").lower().strip()
    if konfirmasi == "y":
        del daftar_pustaka[index]
        print(Fore.GREEN + "Data berhasil dihapus.\n")
    else:
        print(Fore.RED + "Penghapusan dibatalkan.\n")

def lihat_daftar():
    if not daftar_pustaka:
        print(Fore.RED + "\nBelum ada data daftar pustaka.\n")
        return

    kelompok = {}
    for item in daftar_pustaka:
        style = item["style"]
        if style not in kelompok:
            kelompok[style] = []
        kelompok[style].append(item)

    print(Fore.GREEN + "\nDAFTAR PUSTAKA\n")
    for style, daftar in kelompok.items():
        print("="*50 + f" {style.upper()} " + "="*50)
        for i, data in enumerate(daftar, start=1):
            print(f"{i}. {format_styles(data)}\n")

