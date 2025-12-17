try: # try/except yaitu menangani masalah program yang dapat membuat program tersebut terhenti menjadi program yang akan tetap menjalankan program tersebut (tidak berhenti)
    from colorama import Fore, Style, Back, init #memanggil fungsi pengubah warna text, warna background, gaya text, serta inisialisasi colorama
    #cek apakah modul colorama sudah terinstall?
    print('''
┌─────────────────────────────────────────┐
│⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣘⣠⡄⣹⠇⣠⠟⠀⠀⠀⠀⠀⠀ │
│⠀⠀⠀⠀⠀⠀⠀⢸⡟⣿⠀⢸⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠋⣾⠣⠞⣙⢷⡄⠀⠀⠀⠀⠀ │
│⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⠀⢸⡇⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣻⣦⣀⣹⣦⣀⣠⣞⣁⣀⣀⣀⣀⣀ │
│⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⠀⢸⡷⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀ │
│⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ │
│⣠⠒⢄⠀⠀⠀⠀⢸⡟⣧⠀⢸⡇⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ │
│⠀⠑⠤⡉⠢⡀⠀⢸⣧⣿⠀⢸⣧⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ │
│⠀⠀⠀⠈⢲⠎⢀⣶⣶⣶⣶⣶⠆⠀⠀⢰⣶⣶⣶⡆⠀⠀⢀⣴⣶⣶⡶⠂⠀⠀⠀⣰⣶⣶⣶⣶⡶⠀⠀⠀ │ MODULE COLORAMA SUDAH PERNAH TERPASANG
│⠑⠢⡀⡰⠁⠀⣴⣶⣶⡆⠀⠀⠀⠀⠀⠈⣉⣉⣉⡁⠀⣀⣈⣉⡉⠉⠀⠀⠀⠀⠀⠀⣰⣶⣶⡶⠀⠀⠀⠀ │ MAKA PROGRAM BOLE LANJT ✅
│⠀⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠁⠀⠀⠀⠀ │
│⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠁⠀⠀⠀⠀⠀ │
│⠀⠀⠀⣼⣿⣿⣿⣤⡄⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⢠⣤⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀ │
│⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⣀⠀⢀⣀⣀⠀⢉⡉⠉⣉⣉⡁⠀⣀⠀⣀⠀⠀⠀ │
│⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⠀⣉⠀⢸⡏⣿⡅⢈⡁⠀⣿⢹⡇⠀⣿⣆⣿⠀⠀⠀ │
│⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⣿⠀⣿⠀⣿⠀⢸⡇⠈⠁⢸⡇⠀⣿⢸⡇⠀⣿⣿⣿⠀⠀⠀ │
│⢠⠤⠤⠤⠀⠀⠀⠒⠒⠲⡀⠀⠀⠀⠀⠀⠀⣿⠀⣿⠀⣿⠀⠸⠷⣶⡆⢸⡇⠀⣿⢸⡇⠀⣿⢸⣿⠀⠀⠀ │
│⠙⢏⢉⠉⠀⠀⠀⠀⠀⢐⠐⡄⠀⠀⠀⠀⠀⢿⣤⡿⠀⣿⠀⠀⠀⣿⡇⢸⡇⠀⣿⢸⡇⠀⣿⠠⣿⠀⠀⠀ │
│⠀⠈⢎⢀⠒⠦⡀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⢸⣿⡇⠀⣿⠀⢰⡆⣿⡇⢸⡇⠀⣿⢸⡇⠀⣿⢈⣿⠀⠀⠀ │
│⠀⠀⠀⠣⠢⠀⠁⠛⠛⠛⠃⠀⠈⢢⠀⠀⠀⠈⠿⠀⠀⠿⠀⠸⠷⠿⠇⠸⠇⠀⠿⠾⠇⠀⠿⠘⠿⠀⠀⠀ │
│⠀⠀⠀⠀⠑⠛⠛⠛⠛⠛⠛⠛⠒⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  │
└─────────────────────────────────────────┘''')
    input('[Enter ⤷]') #pause
    # jika belum terinstall maka jalankan file setup.py
except ModuleNotFoundError:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⣵⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⢰⡾⠀⣀⣀⠀⢀⣀⡟⢀⡀⢀⡀⢸⠁⢀⣀⠀⢰⣇⢰⠂⢀⣀⠀⣠⣆⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣿⣿⣿⠿⡻⢿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⣎⡇⢰⠇⣹⠀⡟⢸⡇⢸⠇⣸⠀⣿⠀⣯⢼⠃⣼⢹⣼⠀⡏⢸⡇⢸⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣧⢫⢕⣫⣿⣿⣿⣧⠄⠀⠀⠀⠀⠀⠀⠀⠠⠇⠿⠸⠃⠘⠦⠏⠀⠷⠾⠁⠸⠦⠟⠀⠇⠈⠳⠴⠀⠿⠈⠇⠈⠷⠞⠀⠸⠦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣷⢩⢎⣼⣿⣿⣿⣿⣯⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡘⢮⢼⣿⣿⣿⣿⣿⣯⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⢾⣿⣿⣿⣿⣿⣿⣿⢜⡣⢿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢀⡟⠉⠀⡤⣄⠀⣤⠀⡄⢀⣄⣤⠀⢀⣤⡟⠀⡟⠉⠀⣤⣄⢠⣄⡄⢠⣤⡀⢀⣤⡄⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣮⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⡤⠀⠀⢰⡟⠃⢸⡃⣼⠀⣯⠐⡇⢸⡇⢸⠂⣿⠀⡏⢸⡟⠃⢠⡇⠀⢸⠁⠀⡟⢠⡇⢸⠃⠀⠀
⠀⠀⢠⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣣⠀⠘⠁⠀⠘⠓⠋⠀⠛⠚⠃⠘⠂⠛⠀⠙⠚⠃⠘⠓⠃⠘⠃⠀⠛⠀⠀⠛⠚⠁⠘⠀⠀⠀
⠀⡠⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠰⣩⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⣿⠿⡿⣏⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
WKWKWK ADA MODULE KMU YANG BELUM TERINSTALL TUCHH😹, TENANG AJA AKU UDAH KASIH KMU SETUP BIAR GA BINGUNG :v
TUNGGUU YEAHH!
''')
    input('LANJUTT??? TEKEN [ENTER ⤷]') # pause
    import setup
    setup()
    exit()
    
from dafpus_manager import masukan_data, lihat_daftar, ubah_data, hapus_data, muat_data, simpan_data # Mengimport modul membuat data, melihat data, merubah data, menghapus data, menyinkronkan data, dan menyimpan data. Yang berada di file dafpus_manager
from tambahan import layar # mengimpor fungsi layar dari modul tambahan dan fungsinya untuk membersihkan layar sesuai Jenis OS.
init(autoreset=True) # Inisialisasi modul colorama dan mereset warna text dan warna Background text

muat_data() # sinkronisasi data
layar() # membersihkan layar menggunakan modul os di file tambahan

def tampilan_utama(): # Deklarasi fungsi menampilkan setup awal
    layar()

    # Lakukan terus Perulangan ketika fungsi tampilan_utama() di panggil
    while True:
        layar()
        print(Fore.CYAN + "_"*100) # Fore.Cyan, dll yang mana fore ini sebenarnya adalah foreGround dan yang di maksud disini adalah "atur warna text dengan warna cyan"
        # disini kami membuat landing program agar terlihat indah, dan pengguna program ini bisa tahu bahwa program ini dibuat oleh kelompok Be FiveVision ✌🏼😎🤟🏼
        # dan fungsi huruf r'''''' disini itu bisa disebut dengan raw-string jadi karakter slash(\, |,=,dan -) ini ga di anggap yaah!! 
        print(Fore.LIGHTGREEN_EX + r'''
                 .--.   _
             .---|__| .((\=.
          .--|===|--|/    ,(,     ████▄  ▄████▄ ██████ ██████ ▄████▄ █████▄
          |  |===| V|\      y     ██  ██ ██▄▄██ ██▄▄     ██   ██▄▄██ ██▄▄██▄
          |%%| F | i| `.__,'      ████▀  ██  ██ ██       ██   ██  ██ ██   ██ 
          |%%| i | s| /  \\\
          |  | v | i|/|  | \`----.
          |  | e | o||\  \  |___.'_     █████▄ ██  ██ ▄█████ ██████ ▄████▄ ██ ▄█▀ ▄████▄
         _|  |   |_n||,\  \-+-._.' )_   ██▄▄█▀ ██  ██ ▀▀▀▄▄▄   ██   ██▄▄██ ████   ██▄▄██
        / |  |===|--|\  \  \      /  \  ██     ▀████▀ █████▀   ██   ██  ██ ██ ▀█▄ ██  ██
       /  `--^---'--' `--`-'---^-'    \
      '================================`
''')
        print(Back.LIGHTBLUE_EX + f'Ｋｅｌｏｍｐｏｋ Ｂｅ ＦｉｖｅＶｉｓｉｏｎ.')
        print(Fore.MAGENTA + f"\n{'Selamat Datang!':^100}") # memberikan pemformatan perataan teks (text align) disini kami memberi perataan teks di tengah yaitu menggunakan simbol '^' dan '100' disini maksudnya jarak kanan dan kiri dari tekse tersevut
        print(Fore.CYAN + "_"*100) #membuat batas atau garis dengan meng-kalikan string'_' x100
        input('𝓣𝓮𝓴𝓪𝓷 𝓔𝓷𝓽𝓮𝓻 😊') # konfirmasi untuk melanjutkan ke konfigurasi daftar pustaka
        # konfigurasi daftar pustaka kepada pengguna, disini ada 5 opsi yang terdapat beberapa keterangan
        print(Fore.YELLOW + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Silahkan Pilih Opsi Yang Tersedia!':^55} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> [1] Masukan Data           │ Menambahkan data         │
┝━> [2] Ubah Data              │ Mengganti data           │
┝━> [3] Hapus Data             │ Menghapus data           │
┝━> [4] Lihat Daftar Pustaka   │ Melihat Daftar/List data │
┝━> [5] Selesai                │ Keluar Program           │
└──────────────────────────────┴──────────────────────────┘''')

        # mencoba menjalankan statement block try dari baris 100 sampai 134
        try:
            # inputan pemilihan opsi atau konfigurasi dengan mengkonversi input() menjadi tipe data integer
            opsi = int(input(Fore.MAGENTA + '''
  ╭──────────────╮
┏━┥ masukan opsi │
┃ ╰──────────────╯
┗━━━━━➤  ''' + Style.RESET_ALL))
            if opsi == 1: #jika user menginputkan '1' maka program akan masuk kedalam fungsi masukan_data() yang ada di dalam modul dafpus_manager
                masukan_data()
            elif opsi == 2: #jika user menginputkan '2' maka program akan masuk kedalam fungsi ubah_data() setelah itu menjalanka fungsi simpan_data(), yang ada di modul dafpus_manager
                ubah_data()
                simpan_data()
            elif opsi == 3:#jika user menginputkan '3' maka program akan masuk kedalam fungsi hapus_data() setelah itu menjalanka fungsi simpan_data(), yang ada di modul dafpus_manager
                hapus_data()
                simpan_data()
            elif opsi == 4: # di opsi 4 ini kami memakai input() agar di pause terlebih dahlu biar output lihat_daftar()nya tidak tertimpa oleh landing programnya
                konfig_landing = False
                input(Back.LIGHTBLUE_EX + 'Tekan enter untuk melihat daftar pustaka . . .' + Back.RESET)
                layar()
                lihat_daftar()
                input(Back.LIGHTBLUE_EX + 'Tekan enter untuk melanjutkan . . .' + Back.RESET)
                simpan_data()
            elif opsi == 5: # keluar program
                input(Fore.CYAN + '''
              ╭────────────────────────────────────────────────────────────────────╮
              │ ~~~ Terimakasih telah menggunakan daftar pustaka sederhana ini ~~~ │
              ╰────────────────────────────────────────────────────────────────────╯
              ''')
                exit()
            else: #jika user menginputkan angka lebih dari 5 atau kurang dari 1 maka akan menjalankan baris kode 129 sebagai pemberitahuan
                print(Fore.RED + "masukan angka dari 1-5!")
                input('[Enter]') #pause
        # except menangani masalah program yang sedang berjalan agar programnya tidak berhenti
        # ValueError disini yaitu kesalahan penginputan user(menginput dengan tipe data string, yang sebenarnya penginputan tersebut harus be tipe data integer)
        except ValueError:
            print(Fore.RED + "masukan angka dari 1-5!, bukan huruf atau tidak boleh kosong")
            input('[Enter]')

tampilan_utama() #ini adlah start program

simpan_data() # setelah tampilan_utama() dijalankan sampai selesai maka akan menyimpan data (menjalanakn fungsi simpan_data())