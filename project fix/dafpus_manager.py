import json
from format_style import format_styles
from colorama import Fore, Style, init
from tambahan import layar
import os

init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "daftar_pustaka.json")

daftar_pustaka = []

def simpan_data():
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(daftar_pustaka, f, ensure_ascii=False, indent=4)

def muat_data():
    global daftar_pustaka
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            daftar_pustaka = json.load(f)
    except FileNotFoundError:
        daftar_pustaka = []


def pilih_referensi():
    print(Fore.GREEN + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Tipe Referensi':^67} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> [1] Journal/Article        │ Memilih Sumber dari Journal/Article  │
┝━> [2] Book                   │ Memilih Sumber dari Buku             │
┝━> [3] Book Section           │ Memilih Sumber dari Kutipan Bab buku │
┝━> [4] Kembali Ke Menu Utama  │ Kembali ke menu utama                │
└──────────────────────────────┴──────────────────────────────────────┘''')

    while True:
        try:
            tipe_ref = int(input('''
  ╭─────────────────────────────────╮
┏━┥  Pilih tipe referensi (1/2/3/4) │
┃ ╰─────────────────────────────────╯
┗━━━━━➤  '''))

            if tipe_ref == 1:
                print(Fore.YELLOW + "Kamu memilih : Journal/Article\n")
                return "Journal/Article"
            elif tipe_ref == 2:
                print(Fore.YELLOW + "Kamu memilih : Book\n")
                return "Book"
            elif tipe_ref == 3:
                print(Fore.YELLOW + "Kamu memilih : Book Section\n")
                return "Book Section"
            elif tipe_ref == 4:
                layar()
                import main
                main.tampilan_utama()
            else:
                print(Fore.RED + "Masukan tidak valid! Pilih 1, 2, 3 atau 4\n")
        except ValueError:
            print(Fore.RED + "Masukan Angka yang valid\n")


def masukan_style(mode="menu utama"):
    styles = ["APA", "IEEE", "MLA", "Harvard", "Vancouver"]
    slicee = '│'
    print("="*100)
    print(Fore.GREEN + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Pilih Gaya Sitasi':^72} ┃
┡━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''')
    for i, data in enumerate(styles, start=1):
        if len(data) == 3:
            slicee = f'{"│ ":>14}'
            if data == styles[0]:
                slicee += 'American Psychological Association                │'
            if data == styles[2]:
                slicee += 'Modern Language Association                       │'
        elif len(data) == 4:
            slicee = f'{"│ ":>13}'
            slicee += 'Institute of Electrical and Electronics Engineers │'
        elif len(data) == 7:
            slicee = f'{"│ ":>10}'
            slicee += 'Harvard                                           │'
        elif len(data) == 9:
            slicee = f'{"│ ":>8}'
            slicee += 'Vancouver                                         │'
        print(Fore.GREEN + f"┝━> [{i}] {data}{slicee}")
    print(Fore.GREEN + '''┝━> [0] Kembali        │ Kembali ke menu sebelumnya                        │''')
    print(Fore.GREEN + '''└──────────────────────┴───────────────────────────────────────────────────┘''')

    while True:
        try:
            pilihan = int(input('''
  ╭────────────────────╮
┏━┥  Pilih Style (1-5) │
┃ ╰────────────────────╯
┗━━━━━➤  '''))
            if 1 <= pilihan <= len(styles):
                print(Fore.YELLOW + f"Style yang dipilih: {styles[pilihan-1]}")
                return styles[pilihan-1]
            elif pilihan == 0:
                if mode == "menu utama":
                    layar()
                    pilih_referensi()
                    return masukan_style()
                elif mode == "ubah":
                    return "kembali"
            else:
                print(Fore.RED + "Masukkan angka 1 sampai 5.")
        except ValueError:
            print(Fore.RED + "Masukkan angka bukan huruf.")

def masukan_data():
    print(Fore.YELLOW + "-"*100)
    print(Fore.GREEN + f"{'𝗠𝗮𝘀𝘂𝗸𝗸𝗮𝗻 𝗗𝗮𝘁𝗮 𝗗𝗮𝗳𝘁𝗮𝗿 𝗣𝘂𝘀𝘁𝗮𝗸𝗮':^100}")
    print(Fore.YELLOW + "-"*100)
    authors = []
    editors = []
    editors_booksection = []

    tipe = pilih_referensi()
    gaya = masukan_style()
    judul = input('''
  ╭────────────────╮
┏━┥  Masukan judul │
┃ ╰────────────────╯
┗━━━━━➤  ''')

    print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Masukan Nama Penulis [Format : Last name, First name (e.g. Prasetya, Erdi)] ┃
┗━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    while True:
        nama = input(f"    ╰[ Penulis {len(authors)+1} ]──> ")
        if nama.strip() == "":
            print("Nama tidak boleh kosong.")
            continue
        authors.append(nama.title().strip())
        while True:
            tambah = input('''  ╭────────────────────────────────────────────╮
┏━┥  Apakah ingin menambah penulis lain? (y/n) │
┃ ╰────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
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
            tahun = int(input('''  ╭─────────────────╮
┏━┥  Masukkan Tahun │
┃ ╰─────────────────╯
┗━━━━━➤  '''))
            break
        except ValueError:
            print(Fore.RED + "Tahun harus berupa angka")

    halaman = (input('''  ╭─────────────────────╮
┏━┥  Halaman [from-to]  │
┃ ╰─────────────────────╯
┗━━━━━➤  '''))
    volume = (input('''  ╭──────────╮
┏━┥  Volume  │
┃ ╰──────────╯
┗━━━━━➤  '''))

    if tipe == "Journal/Article":
        jurnal = input('''  ╭───────────────────╮
┏━┥  Masukkan jurnal  │
┃ ╰───────────────────╯
┗━━━━━➤  ''')
        issue = input('''  ╭─────────╮
┏━┥  Issue  │
┃ ╰─────────╯
┗━━━━━➤  ''')
    elif tipe == "Book":
        edition = (input('''  ╭───────────╮
┏━┥  Edition  │
┃ ╰───────────╯
┗━━━━━➤  '''))

        print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Masukan Nama Editor [Format : Last name, First name (e.g. Prasetya, Erdi)]  ┃
┗━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        while True:
            namaeditor = input(f"    ╰[ Editor {len(editors)+1} ]──> ")
            if namaeditor.strip() == "":
                break

            editors.append(namaeditor.title().strip())
            while True:
                tambaheditor = input('''  ╭────────────────────────────────────────────╮
┏━┥  Apakah ingin menambah Editor lain? (y/n)  │
┃ ╰────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                if tambaheditor == "y":
                    break
                elif tambaheditor == "n":
                    print(Fore.GREEN + "\nInput editor selesai.\n")
                    break
                else:
                    print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")

            if tambaheditor == "n":
                break

        city = input('''  ╭────────╮
┏━┥  City  │
┃ ╰────────╯
┗━━━━━➤  ''')
        publisher = input('''  ╭─────────────╮
┏━┥  Publisher  │
┃ ╰─────────────╯
┗━━━━━➤  ''')
    else:
        book = input('''  ╭────────╮
┏━┥  Book  │
┃ ╰────────╯
┗━━━━━➤  ''')
        
        edition = (input('''  ╭───────────╮
┏━┥  Edition  │
┃ ╰───────────╯
┗━━━━━➤  '''))

        print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Masukan Nama Editor [Format : Last name, First name (e.g. Prasetya, Erdi)]  ┃
┗━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        while True:
            namaeditor = input(f"[ Editor {len(editors_booksection)+1} ]──> ")
            if namaeditor.strip() == "":
                break

            editors_booksection.append(namaeditor.title())
            while True:
                tambaheditor = input('''  ╭────────────────────────────────────────────╮
┏━┥  Apakah ingin menambah Editor lain? (y/n)  │
┃ ╰────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                if tambaheditor == "y":
                    break
                elif tambaheditor == "n":
                    print("\nInput editor selesai.\n")
                    break
                else:
                    print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")

            if tambaheditor == "n":
                break

        city = input('''  ╭────────╮
┏━┥  City  │
┃ ╰────────╯
┗━━━━━➤  ''')
        publisher = input('''  ╭─────────────╮
┏━┥  Publisher  │
┃ ╰─────────────╯
┗━━━━━➤  ''')

        
        chapter = (input('''  ╭──────────────────╮
┏━┥  Chapter Number  │
┃ ╰──────────────────╯
┗━━━━━➤  '''))

    link = input('''  ╭────────────────╮
┏━┥  Link URL/DOI  │
┃ ╰────────────────╯
┗━━━━━➤  ''')

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

    print(Fore.CYAN + f'''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Daftar Pustaka yang tersimpan':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''')
    for i, data in enumerate(daftar_pustaka, start=1):
        list_hapus_data =  f"┝━> [{i}] {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]"
        for ckk in range(0,83):
            if len(list_hapus_data) == ckk:
                spasi = ' '
                list_hapus_data += spasi
        print(Fore.CYAN + list_hapus_data + '│')
    print(Fore.CYAN + '''└──────────────────────────────────────────────────────────────────────────────────┘'''+ Fore.RESET)

    while True:
        try:
            index = int(input(Fore.YELLOW + '''
  ╭────────────────────────────────╮
┏━┥  Pilih Data yang ingin diubah  │
┃ ╰────────────────────────────────╯
┗━━━━━➤  ''' + Style.RESET_ALL)) - 1
            if 0 <= index < len(daftar_pustaka):
                break
            else:
                print(Fore.RED + "Nomor tidak valid. Coba lagi!\n")
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid, bukan huruf!\n")
            

    data = daftar_pustaka[index]
    print(Fore.MAGENTA + f"\nMengubah data: {data['judul']} ({data['referensi']})\n")

    while True:
        print(Fore.MAGENTA + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Pilih bagian yang ingin diubah':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> {Fore.CYAN + f'[1] Judul' + Fore.RESET + Fore.MAGENTA}                                          │ Ubah Judul                │
┝━> {Fore.CYAN + f'[2] Penulis' + Fore.RESET + Fore.MAGENTA}                                        │ Ubah Penulis              │
┝━> {Fore.CYAN + f'[3] Tahun' + Fore.RESET + Fore.MAGENTA}                                          │ Ubah Tahun                │
┝━> {Fore.CYAN + f'[4] Volume/Halaman' + Fore.RESET + Fore.MAGENTA}                                 │ Ubah Volume/Issue/Halaman │
┝━> {Fore.CYAN + f'[5] Style' + Fore.RESET + Fore.MAGENTA}                                          │ Ubah Style                │
┝━> {Fore.CYAN + f'[6] Informasi Tambahan (tergantung tipe referensi)' + Fore.RESET + Fore.MAGENTA} │ Ubah Tambahan             │
┝━> {Fore.CYAN + f'[7] URL/DOI' + Fore.RESET + Fore.MAGENTA}                                        │ Ubah URL/DOI              │
┝━> {Fore.CYAN + f'[8] Selesai' + Fore.RESET + Fore.MAGENTA}                                        │ Keluar Program            │
└──────────────────────────────────────────────────────┴───────────────────────────┘''')

        pilihan = input(Fore.MAGENTA + '''  ╭──────────────────────────╮
┏━┥  Masukkan Pilihan (1-8)  │
┃ ╰──────────────────────────╯
┗━━━━━➤  ''' + Style.RESET_ALL).strip()

        if pilihan == "1":
            data["judul"] = input('''  ╭───────────────────────╮
┏━┥  Masukkan Judul Baru  │
┃ ╰───────────────────────╯
┗━━━━━➤  ''').strip()

        elif pilihan == "2":
            authors_baru = []
            print("Masukkan ulang daftar penulis [Last name, First name (e.g. Prasetya, Erdi)]:")
            while True:
                nama = input(f'''  ╭─────────────────────╮
┏━┥      Penulis {len(authors_baru)+1}      │
┃ ╰─────────────────────╯
┗━━━━━➤  ''').strip()
                if not nama:
                    print("Nama tidak boleh kosong.")
                    continue
                authors_baru.append(nama.title())
                while True:
                    lagi = input('''  ╭─────────────────────────────╮
┏━┥  Tambahkan nama lain (y/n)  │
┃ ╰─────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                    if lagi == "y":
                        break
                    elif lagi == "n":
                        print("\nInput penulis selesai.\n")
                        break
                    else:
                        print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")
                if lagi == "n":
                    break
                data["authors"] = authors_baru

        elif pilihan == "3":
            while True:
                try:
                    data["tahun"] = int(input('''  ╭───────────────────────╮
┏━┥  Masukkan Tahun Baru  │
┃ ╰───────────────────────╯
┗━━━━━➤  '''))
                    break
                except ValueError:
                    print("Tahun harus berupa angka.")

        elif pilihan == "4":
            volume_baru = input('''  ╭───────────────╮
┏━┥  Volume Baru  │
┃ ╰───────────────╯
┗━━━━━➤  ''').strip()
            if volume_baru:
                data['volume'] = volume_baru
            
            hal_baru = input('''  ╭────────────────╮
┏━┥  Halaman Baru  │
┃ ╰────────────────╯
┗━━━━━➤  ''').strip()
            if hal_baru:
                data['halaman'] = hal_baru

        elif pilihan == "5":
            hasil_style = masukan_style(mode="ubah")
            if hasil_style == "kembali":
                continue
            data['style'] = hasil_style

        elif pilihan == "6":
            if data["referensi"] == "Journal/Article":
                jurnal_baru = input(f'''  ╭────────────────────╮
┏━┥  Nama Jurnal Baru  │
┃ ╰────────────────────╯
┗━━━━━➤  ''').strip()
                if jurnal_baru:
                    data["jurnal"] = jurnal_baru

                issue_baru = input('''  ╭──────────────╮
┏━┥  Issue Baru  │
┃ ╰──────────────╯
┗━━━━━➤  ''').strip()
                if issue_baru:
                    data['issue'] = issue_baru

            elif data["referensi"] == "Book":
                edition_baru = input(f'''  ╭────────────────╮
┏━┥  Edition Baru  │
┃ ╰────────────────╯
┗━━━━━➤  ''').strip()
                if edition_baru:
                    data["edition"] = edition_baru
                
                city_baru = input(f'''  ╭─────────────╮
┏━┥  City Baru  │
┃ ╰─────────────╯
┗━━━━━➤  ''').strip()
                if city_baru:
                    data["city"] = city_baru

                pub_baru = input(f'''  ╭──────────────────╮
┏━┥  Publisher Baru  │
┃ ╰──────────────────╯
┗━━━━━➤  ''').strip()
                if pub_baru:
                    data["publisher"] = pub_baru
                
                while True:
                    ubah_editor = input('''  ╭──────────────────────────────────────────────╮
┏━┥  Apakah ingin mengubah daftar editor? (y/n)  │
┃ ╰──────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                    if ubah_editor == "y":
                        editors_baru = []
                        print('''  ╭─────────────────────────────────────────────────────────────╮
┏━┥  Masukkan ulang daftar editor [format : Last, First name])  │
┃ ╰─────────────────────────────────────────────────────────────╯
┗━━━━━➤  ''')
            
                        while True:
                            nama = input(f'''  ╭────────────────────────────────╮
┏━┥  Editor {len(editors_baru)+1}  │
┃ ╰────────────────────────────────╯
┗━━━━━➤  ''').strip()
                            if not nama:
                                break
                            editors_baru.append(nama.title())
                            while True:
                                lagi = input('''  ╭──────────────────────────────╮
┏━┥  Tambah editor lain? (y/n)}  │
┃ ╰──────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                                if lagi == "y":
                                    break
                                elif lagi == "n":
                                    print("input editor baru selesai")
                                    break
                                else:
                                    print("masukan huruf y atau n")
                            if lagi == "n":
                                break
                        if editors_baru:
                            data["editors"] = editors_baru
                        break

                    elif ubah_editor == "n":
                        print("editor tidak diubah")
                        break
                    else:
                        print("masukan tidak valid")
                        continue

            elif data["referensi"] == "Book Section":
                book_baru = input(f'''  ╭───────────────────────────────────────────╮
┏━┥  Judul buku baru [{data.get('book','')}]  │
┃ ╰───────────────────────────────────────────╯
┗━━━━━➤  ''').strip()
                if book_baru:
                    data["book"] = book_baru

                chapter_baru = input(f'''  ╭───────────────────────────────────────────╮
┏━┥  Chapter baru [{data.get('chapter','')}]  │
┃ ╰───────────────────────────────────────────╯
┗━━━━━➤  ''').strip()
                if chapter_baru:
                    data["chapter"] = chapter_baru

                ed_baru = input(f'''  ╭───────────────────────────────────────────╮
┏━┥  Edition baru [{data.get('edition','')}]  │
┃ ╰───────────────────────────────────────────╯
┗━━━━━➤  ''').strip()
                if ed_baru:
                    data["edition"] = ed_baru

                city_baru = input(f'''  ╭─────────────────────────────────────╮
┏━┥  City baru [{data.get('city','')}]  │
┃ ╰─────────────────────────────────────╯
┗━━━━━➤  ''').strip()
                if city_baru:
                    data["city"] = city_baru

                pub_baru = input(f'''  ╭───────────────────────────────────────────────╮
┏━┥  Publisher baru [{data.get('publisher','')}]  │
┃ ╰───────────────────────────────────────────────╯
┗━━━━━➤  ''').strip()
                if pub_baru:
                    data["publisher"] = pub_baru
  
                while True:
                    ubah_editor = input('''  ╭──────────────────────────────────────────────╮
┏━┥  Apakah ingin mengubah daftar editor? (y/n)  │
┃ ╰──────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                    if ubah_editor == "y":
                        editors_baru = []
                        print('''  ╭─────────────────────────────────────────────────────────────╮
┏━┥  Masukkan ulang daftar editor [format : Last, First name])  │
┃ ╰─────────────────────────────────────────────────────────────╯
┗━━━━━➤  ''')
                        while True:
                            nama = input(f'''  ╭────────────────────────────────╮
┏━┥  Editor {len(editors_baru)+1}  │
┃ ╰────────────────────────────────╯
┗━━━━━➤  ''').strip()
                            if not nama:
                                break
                            editors_baru.append(nama.title())
                            while True:
                                lagi = input('''  ╭──────────────────────────────╮
┏━┥  Tambah editor lain? (y/n)}  │
┃ ╰──────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                                if lagi == "y":
                                    break
                                elif lagi == "n":
                                    print("input editor baru selesai")
                                    break
                                else:
                                    print("masukan huruf y atau n")
                            if lagi == "n":
                                break
                        if editors_baru:
                            data["editors"] = editors_baru
                        break

                    elif ubah_editor == "n":
                        print("editor tidak diubah")
                        break
                    else:
                        print("masukan tidak valid")
                        continue
                
        elif pilihan == "7":
            data["link"] = input('''  ╭─────────────────────────╮
┏━┥  Masukkan URL/DOI Baru  │
┃ ╰─────────────────────────╯
┗━━━━━➤  ''').strip()

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

    print(Fore.CYAN + f'''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Daftar Pustaka yang tersimpan':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''')
    for i, data in enumerate(daftar_pustaka, start=1):
        list_hapus_data =  f"┝━> [{i}] {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]"
        for ckk in range(0,83):
            if len(list_hapus_data) == ckk:
                spasi = ' '
                list_hapus_data += spasi
        print(Fore.CYAN + list_hapus_data + '│')
    print(Fore.CYAN + '''└──────────────────────────────────────────────────────────────────────────────────┘'''+ Fore.RESET)

    while True:
        try:
            index = int(input(Fore.YELLOW + '''
  ╭───────────────────────────────────────╮
┏━┥  Pilih nomor data yang ingin dihapus  │
┃ ╰───────────────────────────────────────╯
┗━━━━━➤  ''')) - 1
            if 0 <= index < len(daftar_pustaka):
                break
            else:
                print(Fore.RED + "Nomor tidak valid.\n")
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid.\n")

    data = daftar_pustaka[index]
    while True:
        konfirmasi = input(Fore.YELLOW + '''
  ╭──────────────────────────────────────────────────────────────╮
┏━┥        Apakah kamu yakin ingin menghapus ini? (y/n)          │
┃ ╰──────────────────────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()

        if konfirmasi == "y":
            del daftar_pustaka[index]
            print(Fore.GREEN + "Data berhasil dihapus.\n")
            break
        elif konfirmasi == "n":
            print(Fore.RED + "Penghapusan dibatalkan.\n")
            break
        else:
            print("masukan tidak valid, ketik y atau n")


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

    jumbotron2 = r'''
            ___   _   ___ _____ _   ___   ___ _   _ ___ _____ _   _  __   _   
           |   \ /_\ | __|_   _/_\ | _ \ | _ \ | | / __|_   _/_\ | |/ /  /_\  
           | |) / _ \| _|  | |/ _ \|   / |  _/ |_| \__ \ | |/ _ \| ' <  / _ \ 
           |___/_/ \_\_|   |_/_/ \_\_|_\ |_|  \___/|___/ |_/_/ \_\_|\_\/_/ \_\
'''
    print(Fore.GREEN + f'\t\t{jumbotron2}')
    for style, daftar in kelompok.items():
        print("─"*50 + f" {style.upper()} " + "─"*50)
        for i, data in enumerate(daftar, start=1):
            if style == "IEEE":
                print(f"[{i}]. {format_styles(data)}\n")
            else:
                print(f"{i}. {format_styles(data)}\n")