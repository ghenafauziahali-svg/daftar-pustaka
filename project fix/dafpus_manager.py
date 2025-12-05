import json # modul untuk manipulasi data
from format_style import format_styles # Mengimport fungsi mengatur gaya atau format standar Daftar Pustaka pada umumnya. Yang berada di file format_style
from colorama import Fore, Back, Style, init #memanggil fungsi pengubah warna text, warna background, gaya text, serta inisialisasi colorama
from tambahan import layar # mengimpor fungsi layar dari modul tambahan dan fungsinya untuk membersihkan layar sesuai Jenis OS.
import os #mengimport modul os(sistem operasi) mengakses terminal, nama os, dll

init(autoreset=True) # Inisialisasi modul colorama dan mereset warna text dan warna Background text

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # mengelola file dari folder absolut
JSON_PATH = os.path.join(BASE_DIR, "daftar_pustaka.json")

daftar_pustaka = [] # bikin list kosong untuk menyimpan dan menampilkan data Daftar pustaka

# simpan data daftar pustaka ketika ada perubahan (entahitu di ubah,dihapus,ditambahin)
def simpan_data():
    # with adalah keyword bawaan dari python dia mengandung file path __enter__() yang akan membuka file dan berakhiran file path __exit__() ketika block kode with selsai dijalankan
    # open untuk membuka file, parameternya open(lokasi script yang ada di folder absolut path, modenya, format encondingnya) cth JSON_PATH -> lokasi folder script, w -> write, enconding=UTF-8 -> membaca karakter unicode
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(daftar_pustaka, f, ensure_ascii=False, indent=4)

def muat_data(): # definisi fungsi untuk memuat data dari file JSON
    global daftar_pustaka # gunakan variabel global daftar_pustaka biar bisa diakses di luar fungsi
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f: # buka file JSON untuk dibaca dengan encoding UTF-8
            daftar_pustaka = json.load(f) # baca isi file JSON dan ubah menjadi list/dict Python, simpan ke daftar_pustaka
    except FileNotFoundError: # jika file JSON tidak ditemukan
        daftar_pustaka = [] # buat list kosong supaya program tetap berjalan tanpa error


def pilih_referensi(): # fungsi untuk menampilkan menu pilihan tipe referensi
    print(Fore.GREEN + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Tipe Referensi':^67} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> [1] Journal/Article        │ Memilih Sumber dari Journal/Article  │
┝━> [2] Book                   │ Memilih Sumber dari Buku             │
┝━> [3] Book Section           │ Memilih Sumber dari Kutipan Bab buku │
┝━> [4] Kembali Ke Menu Utama  │ Kembali ke menu utama                │
└──────────────────────────────┴──────────────────────────────────────┘''')

    while True: # loop tak terbatas, agar terus tampil ketika salah memasukan angka(setelah statement line 62 dan 64 di jalankan)
        try:
            # minta input user dan ubah menjadi integer
            tipe_ref = int(input('''
  ╭─────────────────────────────────╮
┏━┥  Pilih tipe referensi (1/2/3/4) │
┃ ╰─────────────────────────────────╯
┗━━━━━➤  '''))

            if tipe_ref == 1:
                print(Fore.YELLOW + "Kamu memilih : Journal/Article\n") # tampilkan pilihan dengan warna kuning
                return "Journal/Article" # kembalikan string pilihan, keluar dari fungsi, masuk ke golongan referensi Jounal/Article
            elif tipe_ref == 2:
                print(Fore.YELLOW + "Kamu memilih : Book\n")
                return "Book"
            elif tipe_ref == 3:
                print(Fore.YELLOW + "Kamu memilih : Book Section\n")
                return "Book Section"
            elif tipe_ref == 4:
                layar() # besihkan layar sesuai OSnya
                import main #siapin modul main
                main.tampilan_utama() #panggil fungsi tampilan_utama() di modul main
            else:
                print(Fore.RED + "𝙈𝙖𝙨𝙪𝙠𝙖𝙣 𝙩𝙞𝙙𝙖𝙠 𝙫𝙖𝙡𝙞𝙙! 𝙋𝙞𝙡𝙞𝙝 1, 2, 3 𝙖𝙩𝙖𝙪 4 ❌\n")
        #eksepsi yaitu ketika program yang sedang berjalan memiliki kesalahan yang di tentukan, program tersebut tidak akan berhenti, akan tetapi memberi tahu kesalahan user, dan mengulangi program sampai tidak ada masalah
        except ValueError:
            print(Fore.RED + "𝙈𝙖𝙨𝙪𝙠𝙖𝙣 𝘼𝙣𝙜𝙠𝙖 𝙔𝙖𝙣𝙜 𝙑𝙖𝙡𝙞𝙙 ❌\n")


def masukan_style(mode="menu utama"): # menentukan gaya penulisan Daftar Pustaka
    styles = ["APA", "IEEE", "MLA", "Harvard", "Vancouver"] #inisialisasi gaya penulisan dafpus
    slicee = '│' #border dengan pengkondisian, di tentukan dari panjang element

    while True: #ulangi terus inputan, jika user membuat kesalahan atau jika user memanggil fungsi masukan_style()
        print("="*100) #simbol '=' di kali 100 sebagai batas
        # mulai mebuat table
        print(Fore.GREEN + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Pilih Gaya Sitasi':^72} ┃
┡━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''') #bikin header table dengan 
        for i, data in enumerate(styles, start=1): # cetak jumlah gaya Sitasi, i adalah variable perulangan yang nilainya itu nomor urut, data juga variable perulangan tetapi nilainya jumlah data2 atau element styles, angka di mulai dari 1(start=1)
            if len(data) == 3: #jika jumlah karakter dari nilai data adalah 3, maka beri border table dan beri perataan string '|' rata kanan, menggunakan f-string. {}adalah untuk mengakses variable,membuat string di dalam string, operasi aritmatika, dan lain2.
                # :>14 artinya beri perataan, rata kanan, dengan jarak 14 karakter
                slicee = f'{"│ ":>14}'
                if data == styles[0]: #jika data styles index 0 di temukan maka jalankan perintah ini
                    slicee += 'American Psychological Association                │' # bariable slicee (|) + string"American....."
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
            print(Fore.GREEN + f"┝━> [{i}] {data}{slicee}") # fore.green pemberian warna text menjadi hijau
        print(Fore.GREEN + '''┝━> [0] Kembali        │ Kembali ke menu sebelumnya                        │''') #membuar opsi kembali ke menu sebelumnya
        print(Fore.GREEN + '''└──────────────────────┴───────────────────────────────────────────────────┘''')
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
                    return masukan_style() #balik ke sebelumnya
                elif mode == "ubah":
                    return "kembali"
            else:
                print(Fore.RED + "Masukkan angka 1 sampai 5.")
        except ValueError:
            print(Fore.RED + "Masukkan angka bukan huruf.") #jika kesalahn input adalah huruf padahal yg di minta itu angka tipedatanya

def masukan_data(): #ini opsi 1 dari landing program (main)
    print(Fore.YELLOW + "-"*100)
    print(Fore.GREEN + f"{'𝗠𝗮𝘀𝘂𝗸𝗸𝗮𝗻 𝗗𝗮𝘁𝗮 𝗗𝗮𝗳𝘁𝗮𝗿 𝗣𝘂𝘀𝘁𝗮𝗸𝗮':^100}") #text rata tengah
    print(Fore.YELLOW + "-"*100)
    #menyimpan data sementara
    authors = [] 
    editors = []
    editors_booksection = []
    index = 0 # variable global dalam fungsi masukan_data saja untuk menentukan mau di panggil index 0 yang nanti nilainya akan berubah sesuai yang di tentukan

    tipe = pilih_referensi() #tipe akan bernilai returnnya pilih_referensi sesuai kondisi returnnya
    gaya = masukan_style() #tipe akan bernilai returnnya pilih_referensi sesuai kondisi returnnya
    # menentukan judul daftar pustaka
    judul = input('''
  ╭───────────────╮
┏━┥ Masukan judul │
┃ ╰───────────────╯
┗━━━━━➤  ''')

    print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Masukan Nama Penulis [Format : Last name, First name (e.g. Prasetya, Erdi)] ┃
┗━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    while True:
        nama = input(f"    ╰[ Penulis {len(authors)+1} ]──> ")
        if nama.strip() == "": # fungsi strip() disini adalah metode string, maksudnya menghapus spasi kanan dan kiri
            print("Nama tidak boleh kosong. ❌")
            continue
        authors.append(nama.title().strip()) #append adalah metode list yang maksudnya untuk menambahkan item ke dalam list authors, title untuk itu metode string, yang gunannya untuk memformat kapitalisasi text, yaitu kapital di setiap awal kata saja
        while True:
            '''menanyakan apakah mau menambah penulis lain?
            {len(authors)} -> cek apakah ada karakter di dalem variable authors, klo ada, ada berapa?.
            {authors[index]} mengambil nama penulis sesuai index yang ditentuin'''
            tambah = input(f'''
      ╭[ {f'{Back.LIGHTBLUE_EX} {Fore.LIGHTGREEN_EX}Penulis {len(authors)} {authors[index]} {Style.RESET_ALL}':^10} ]
  ╭───┴────────────────────────────────────────╮
┏━┥  Apakah ingin menambah penulis lain? (y/n) │
┃ ╰────────────────────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
            if tambah == "y": #jika ya maka index yang tadinya 0 menambah jadi 1
                index += 1
                break #berhenti dari perulangan baris 147
            elif tambah == "n":
                print("\n𝙄𝙣𝙥𝙪𝙩 𝙥𝙚𝙣𝙪𝙡𝙞𝙨 𝙨𝙚𝙡𝙚𝙨𝙖𝙞. ✅\n")
                break
            else:
                print(Fore.RED + "Input tidak valid, ❌ ketik 'y' untuk menambah atau 'n' untuk selesai.\n")
        if tambah == "n": #jika tambah bernilai n maka keluar dari perulangan baris141, lanjut ke baris 166
            break 

    while True:
        try:
            # menetukan tahun
            tahun = int(input('''  ╭─────────────────╮
┏━┥  Masukkan Tahun │
┃ ╰─────────────────╯
┗━━━━━➤  '''))
            break
        except ValueError:
            print(Fore.RED + "Tahun harus berupa angka")
    # dari haalaman berapa sampai ke berapa
    halaman = input('''  ╭─────────────────────╮
┏━┥  Halaman [from-to]  │
┃ ╰─────────────────────╯
┗━━━━━➤  ''')
    # ini bagian ke berapa di terbitkannya
    volume = input('''  ╭──────────╮
┏━┥  Volume  │
┃ ╰──────────╯
┗━━━━━➤  ''')

    if tipe == "Journal/Article":
        # nama jurnal
        jurnal = input('''  ╭───────────────────╮
┏━┥  Masukkan jurnal  │
┃ ╰───────────────────╯
┗━━━━━➤  ''')
        # subbagian ke berapa dari bagian ke berapa
        issue = input('''  ╭─────────╮
┏━┥  Issue  │
┃ ╰─────────╯
┗━━━━━➤  ''')
    elif tipe == "Book": #referensi dari buku
        #edisi keberapa
        edition = input('''  ╭───────────╮
┏━┥  Edition  │
┃ ╰───────────╯
┗━━━━━➤  ''')
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
                    print(Fore.GREEN + "\nInput editor selesai. ✅\n")
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
        edition = input('''  ╭───────────╮
┏━┥  Edition  │
┃ ╰───────────╯
┗━━━━━➤  ''')

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
        # kota tempat penerbit
        city = input('''  ╭────────╮
┏━┥  City  │
┃ ╰────────╯
┗━━━━━➤  ''')
        #nama penerbit buku
        publisher = input('''  ╭─────────────╮
┏━┥  Publisher  │
┃ ╰─────────────╯
┗━━━━━➤  ''')
        # nomor bab
        chapter = input('''  ╭──────────────────╮
┏━┥  Chapter Number  │
┃ ╰──────────────────╯
┗━━━━━➤  ''')
    # sumber link
    link = input('''  ╭────────────────╮
┏━┥  Link URL/DOI  │
┃ ╰────────────────╯
┗━━━━━➤  ''')
    # membuat varibale tipedatanya dictionary yang akan menyimpan data referensi di variable daftar_pustaka = [], dan akan di simpan di file daftar_pustaka.json
    data = {
    "referensi": tipe, #nilai referensi ini akan bernilai tergantung nilai varibale tipe
    "style": gaya,
    "judul": judul,
    "authors": authors.copy(),
    "tahun": tahun,
    "jurnal": jurnal if tipe=="Journal/Article" else "", #jika nilai tipe adalah jurnal/artikel maka nilai variable jurnal di tambahkan ke nilai dictionary jurnal
    "volume": volume,
    "issue": issue if tipe=="Journal/Article" else "", #hanya berlaku untuk tipe jurnal/article saja, jurnal,issue,edition,dll
    "halaman": halaman,
    "edition": edition if tipe!="Journal/Article" else "",
    "editors": editors.copy() if tipe=="Book" else editors_booksection.copy(), # fungsi .cpoy() disini yaitu menduplikat list Asli menjadi list Baru, yang mana ddata dictionary tidak terpengaruh jika list asli nanti berubah.
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
        return # keluarfungsi dan akan kembali ke landing program ke bagian muat_data() dan menjalankan fungsi tampilan_utama()
    cek_panjangH = '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓' #untuk mengecek panjang karakter tabel
    print(Fore.CYAN + f'''{cek_panjangH}
┃ {'Daftar Pustaka yang tersimpan':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''')
    for i, data in enumerate(daftar_pustaka, start=1):
        #i adalah nomor urut, {data['judul']}mengambil nilai judul di dictionary data, begitupun seterusnya
        list_ubah_data =  f"┝━> [{i}] {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]" 
        for ckk in range(0,len(cek_panjangH)-1): #bikin perulangan sebanyak karakter cek_panjangH lalu di kurangi 1 agar bisa sejajar dengan header table aslinya
            if len(list_ubah_data) == ckk:
                spasi = ' '
                list_ubah_data += spasi
        print(Fore.CYAN + list_ubah_data + '│')
    print(Fore.CYAN + '''┝━> [0] Tidak jadi hehe 😁                                                         │''')
    print(Fore.CYAN + '''└──────────────────────────────────────────────────────────────────────────────────┘''')

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
                print(Fore.RED + "Nomor tidak valid. Coba lagi! ❌\n")
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid, bukan huruf! ❌\n")

    data = daftar_pustaka[index] #menentukan data daftar pusaka yang di pilih user untuk mengubah datanya
    print(Fore.MAGENTA + f"\nMengubah data: {data['judul']} ({data['referensi']})\n")

    while True:
        print(Fore.MAGENTA + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Pilih bagian yang ingin diubah':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> {Fore.CYAN + f'[1] Judul' + Fore.RESET + Fore.MAGENTA}                                          │ {Fore.CYAN + f'Ubah Judul' + Fore.RESET + Fore.MAGENTA}                │
┝━> {Fore.CYAN + f'[2] Penulis' + Fore.RESET + Fore.MAGENTA}                                        │ {Fore.CYAN + f'Ubah Penulis' + Fore.RESET + Fore.MAGENTA}              │
┝━> {Fore.CYAN + f'[3] Tahun' + Fore.RESET + Fore.MAGENTA}                                          │ {Fore.CYAN + f'Ubah Tahun' + Fore.RESET + Fore.MAGENTA}                │
┝━> {Fore.CYAN + f'[4] Volume/Halaman' + Fore.RESET + Fore.MAGENTA}                                 │ {Fore.CYAN + f'Ubah Volume/Halaman' + Fore.RESET + Fore.MAGENTA}       │
┝━> {Fore.CYAN + f'[5] Style' + Fore.RESET + Fore.MAGENTA}                                          │ {Fore.CYAN + f'Ubah Style' + Fore.RESET + Fore.MAGENTA}                │
┝━> {Fore.CYAN + f'[6] Informasi Tambahan (tergantung tipe referensi)' + Fore.RESET + Fore.MAGENTA} │ {Fore.CYAN + f'Ubah Tambahan' + Fore.RESET + Fore.MAGENTA}             │
┝━> {Fore.CYAN + f'[7] URL/DOI' + Fore.RESET + Fore.MAGENTA}                                        │ {Fore.CYAN + f'Ubah URL/DOI' + Fore.RESET + Fore.MAGENTA}              │
┝━> {Fore.CYAN + f'[8] Selesai' + Fore.RESET + Fore.MAGENTA}                                        │ {Fore.CYAN + f'Keluar dari ubah data' + Fore.RESET + Fore.MAGENTA}     │
└──────────────────────────────────────────────────────┴───────────────────────────┘''')

        pilihan = input(Fore.MAGENTA + '''  ╭──────────────────────────╮
┏━┥  Masukkan Pilihan (1-8)  │
┃ ╰──────────────────────────╯
┗━━━━━➤  ''' + Style.RESET_ALL).strip()

        if pilihan == "1":
            data["judul"] = input('''  ╭───────────────────────╮
┏━┥  Masukkan Judul Baru  │
┃ ╰───────────────────────╯
┗━━━━━➤  ''').strip() # buat judul baru serta menghapus spasi di awal string dan akhir

        elif pilihan == "2": #tambah author
            authors_baru = []
            print("Masukkan ulang daftar penulis [Last name, First name (e.g. Prasetya, Erdi)]:")
            while True:
                nama = input(f'''  ╭─────────────────────╮
┏━┥      Penulis {len(authors_baru)+1}      │
┃ ╰─────────────────────╯
┗━━━━━➤  ''').strip()
                if not nama: #not disini maksudnya kondisi salah, jadinya jika nilai variable nama gada
                    print("Nama tidak boleh kosong.")
                    continue
                authors_baru.append(nama.title())
                while True:
                    lagi = input('''  ╭─────────────────────────────╮
┏━┥  Tambahkan nama lain (y/n)  │
┃ ╰─────────────────────────────╯
┗━━━━━➤  ''').lower().strip()
                    if lagi == "y":
                        break #keluar perulangan
                    elif lagi == "n":
                        print("\nInput penulis selesai.\n")
                        break
                    else:
                        print(Fore.RED + "Input tidak valid, ketik 'y' untuk menambah atau 'n' untuk selesai.\n")
                if lagi == "n":
                    data["authors"] = authors_baru
                    break

        elif pilihan == "3":
            while True:
                try:
                    data["tahun"] = int(input('''  ╭───────────────────────╮
┏━┥  Masukkan Tahun Baru  │
┃ ╰───────────────────────╯
┗━━━━━➤  '''))
                    break
                except ValueError: #jika user menginputkan alfabet
                    print("Tahun harus berupa angka.")

        elif pilihan == "4":
            volume_baru = input('''  ╭───────────────╮
┏━┥  Volume Baru  │
┃ ╰───────────────╯
┗━━━━━➤  ''').strip()
            if volume_baru:
                data['volume'] = volume_baru # nilai dari kunci volume di dictionary data yaitu nilai volume_baru

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

            # apakah nilai kunci referensi sama dengan nilai book section
            elif data["referensi"] == "Book Section":
                #cek kondisi box
                len_dataBook = data.get('book', '')
                header = '  ╭───────────────────' #header box
                headerEND = '╮' # end header box
                footer = '┃ ╰───────────────────'
                footerEND = '╯'
                space = ' ' #untuk mengatur jarak antra box dengan text
                c = 2 # penambahan spasi
                for i in range(0, 50): # bikin perulangan maksimal sampai 49
                    if len(len_dataBook) == i: #jika jumlah karakter dari nilai kuncinya book (14) itu sama dengan perulangan, maka lanjut baris 541
                        if len(len_dataBook) >= 1: #jika panjang karakter dari nilai kuncinya book (14) lebih beasr sama dengan 1, maka header di tambah dengan string '-' untuk penyesuaian border
                            h_f = '─'
                            h_f += h_f*(len(len_dataBook)+c)
                            header += h_f
                            footer += h_f
                            space *= c
                        
                        if len(len_dataBook) == 0: # klo jumlah karakter nilai kuncinya 0??? ganti variable char jadi default 0
                            # jika kosong tampilannyaa normal
                            char = "]  │"
                            break # berhenti jan lanjut, klo lanjut malahhhan keubah

                        char = "]" + space + "│"
                        break
                # mengambil nilai kunci book di dalem dictionary data, klo gada maka isi nilai kunci book jadi string kosong ''
                book_baru = input(f'''{header+headerEND}
┏━┥  Judul buku baru [{len_dataBook+char}
{footer+footerEND}
┗━━━━━➤  ''').strip()
                if book_baru:
                    data["book"] = book_baru

                len_dataChapter = data.get('chapter', '')
                header = '  ╭───────────────────'
                headerEND = '╮'
                footer = '┃ ╰───────────────────'
                footerEND = '╯'
                space = ' '
                c = 2
                for i in range(0, 50):
                    if len(len_dataChapter) == i:
                        if len(len_dataChapter) == 0:
                            # jika kosong tampilannyaa normal
                            char = "]  │"
                            break

                        elif len(len_dataChapter) >= 1:
                            h_f = '─'
                            h_f += h_f * (len(len_dataChapter) - c)
                            header += h_f
                            footer += h_f
                            space *= c

                        char = "]" + space + "│"
                        break

                chapter_baru = input(f'''{header+headerEND}
┏━┥  Chapter baru [{len_dataChapter+char}
{footer+footerEND}
┗━━━━━➤  ''').strip()
                if chapter_baru:
                    data["chapter"] = chapter_baru

                len_dataEdition = data.get('edition', '')
                header = '  ╭───────────────────'
                headerEND = '╮'
                footer = '┃ ╰───────────────────'
                footerEND = '╯'
                space = ' '
                c = 2
                for i in range(0, 50):
                    if len(len_dataEdition) == i:
                        if len(len_dataEdition) == 0:
                            # jika kosong tampilannyaa normal
                            char = "]  │"
                            break

                        elif len(len_dataEdition) >= 1:
                            h_f = '─'
                            h_f += h_f * (len(len_dataEdition) - c)
                            header += h_f
                            footer += h_f
                            space *= c

                        char = "]" + space + "│"
                        break


                ed_baru = input(f'''{header+headerEND}
┏━┥  Edition baru [{len_dataEdition+char}
{footer+footerEND}
┗━━━━━➤  ''').strip()
                if ed_baru:
                    data["edition"] = ed_baru

                len_dataCity = data.get('city', '')
                header = '  ╭────────────────'
                headerEND = '╮'
                footer = '┃ ╰────────────────'
                footerEND = '╯'
                space = ' '
                c = 2
                for i in range(0, 50):
                    if len(len_dataCity) == i:
                        if len(len_dataCity) == 0:
                            # jika kosong tampilannyaa normal
                            char = "]  │"
                            break

                        elif len(len_dataCity) >= 1:
                            h_f = '─'
                            h_f += h_f * (len(len_dataCity) - c)
                            header += h_f
                            footer += h_f
                            space *= c

                        char = "]" + space + "│"
                        break

                city_baru = input(f'''{header+headerEND}
┏━┥  City baru [{len_dataCity+char}
{footer+footerEND}
┗━━━━━➤  ''').strip()
                if city_baru:
                    data["city"] = city_baru

                len_dataPublisher = data.get('publisher', '')
                header = '  ╭─────────────────────'
                headerEND = '╮'
                footer = '┃ ╰─────────────────────'
                footerEND = '╯'
                space = ' '
                c = 2
                for i in range(0, 50):
                    if len(len_dataPublisher) == i:
                        if len(len_dataPublisher) == 0:
                            # jika kosong tampilannyaa normal
                            char = "]  │"
                            break

                        elif len(len_dataPublisher) >= 1:
                            h_f = '─'
                            h_f += h_f * (len(len_dataPublisher) - c)
                            header += h_f
                            footer += h_f
                            space *= c

                        char = "]" + space + "│"
                        break

                pub_baru = input(f'''{header+headerEND}
┏━┥  Publisher baru [{len_dataPublisher+char}
{footer+footerEND}
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
                        print('''  ╭────────────────────────────────────────────────────────────╮
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
                                lagi = input('''  ╭─────────────────────────────╮
┏━┥  Tambah editor lain? (y/n)  │
┃ ╰─────────────────────────────╯
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
            break #keluar perulangan

        else:
            print("Pilihan tidak valid, coba lagi.")

    daftar_pustaka[index] = data
    print("Data berhasil diperbarui!\n")

def hapus_data():
    if not daftar_pustaka:
        print(Fore.RED + "\nBelum ada data untuk dihapus.\n")
        return

    # bikin list daftar pustaka yang tersimpan menggunakan perulangan for dengan nomor urut, urutan item juga
    print(Fore.CYAN + f'''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Daftar Pustaka yang tersimpan':^80} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩''')
    for i, data in enumerate(daftar_pustaka, start=1):
        list_hapus_data =  f"┝━> [{i}] {data['judul']} ({data['tahun']}) - {data['referensi']} [{data['style']}]" #akan di panggil terus sebanyak list daftar pustaka yang tersimpan
        for ckk in range(0,83):
            if len(list_hapus_data) == ckk:
                spasi = ' '
                list_hapus_data += spasi
        print(Fore.CYAN + list_hapus_data + '│')
    print(Fore.CYAN + '''┝━> [0] Tidak jadi hehe 😁                                                         │''')
    print(Fore.CYAN + '''└──────────────────────────────────────────────────────────────────────────────────┘''')

    while True:
        try:
            index = int(input(Fore.YELLOW + '''
  ╭───────────────────────────────────────╮
┏━┥  Pilih nomor data yang ingin dihapus  │
┃ ╰───────────────────────────────────────╯
┗━━━━━➤  ''')) - 1

            print(index)
            if index == -1: # user menginputkan 0, maka index sekarang -1 karena di "...━━━━━➤  ''')) - 1" nominal index di kurang 1, menjadi -1
                layar()
                from main import tampilan_utama
                tampilan_utama()
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
            del daftar_pustaka[index] #hapus list daftar pustaka sesuai index yang di input user tadi
            print(Fore.GREEN + "Data berhasil dihapus.\n")
            break
        elif konfirmasi == "n":
            print(Fore.RED + "Penghapusan dibatalkan.\n")
            break
        else:
            print("masukan tidak valid, ketik y atau n")


def lihat_daftar(): # fungsi melihat list daftar pustaka
    if not daftar_pustaka: #klo isi list daftar pustaka belom ada isinya maka jalanin statemtn ini
        print(Fore.RED + "\nBelum ada data daftar pustaka.\n")
        return

    kelompok = {} #buat dictionary sementara
    # mengkelompokkan data sesuai style
    for item in daftar_pustaka:
        style = item["style"] #mengambil nilai style dari item
        if style not in kelompok: # klo style gada di dalem kelompok maka 
            kelompok[style] = [] #Buat nilai style baru yang ada dalam dictionary kelompok sesuai nilai style.
        kelompok[style].append(item) #setelah di buat kategori baru dalem kelompok maka tambahin item ke dalem listnya 
    #hiasan awal
    jumbotron2 = r'''
            ___   _   ___ _____ _   ___   ___ _   _ ___ _____ _   _  __   _   
           |   \ /_\ | __|_   _/_\ | _ \ | _ \ | | / __|_   _/_\ | |/ /  /_\  
           | |) / _ \| _|  | |/ _ \|   / |  _/ |_| \__ \ | |/ _ \| ' <  / _ \ 
           |___/_/ \_\_|   |_/_/ \_\_|_\ |_|  \___/|___/ |_/_/ \_\_|\_\/_/ \_\
'''
    print(Fore.GREEN + f'\t\t{jumbotron2}') #cetak jumbotronnya
    for style, daftar in kelompok.items(): #items adalah metode dari dictionary, perulangan ini memecah setiap pasangan yaitu style adalah kuncinya, daftar sebagai nilainya
        print("─"*50 + f" {style.upper()} " + "─"*50) #gaya daftar pustaka(APA,dll)
        for i, data in enumerate(daftar, start=1): # i sebagai nomor urut yang di mulai dari 1, data yaitu urutan data sesuai nomor urut
            if style == "IEEE":
                print(f"[{i}]. {format_styles(data)}\n")#menampilkan nomor urut. memanggil fungsi. jika format  pakai gaya IEEE maka penomoran dikasih kurung kotak []
            else:
                print(f"{i}. {format_styles(data)}\n")  #jika tidak, penomoran memakai .

