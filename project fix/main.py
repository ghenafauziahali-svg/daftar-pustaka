from tambahan import layar
import os
from dafpus_manager import masukan_data, lihat_daftar, ubah_data, hapus_data, muat_data, simpan_data
from format_style import format_styles
from colorama import Fore, Style, Back, init

init(autoreset=True)

muat_data()
layar()

def tampilan_utama():
    layar()

    while True:
        print(Fore.CYAN + "_"*100)
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

Ｋｅｌｏｍｐｏｋ Ｂｅ ＦｉｖｅＶｉｓｉｏｎ.''')
        print(Fore.MAGENTA + "\nSelamat Datang!")
        print(Fore.CYAN + "_"*100)
        print(Fore.YELLOW + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {'Silahkan Pilih Opsi Yang Tersedia!':^55} ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┝━> [1] Masukan Data           │ Menambahkan data         │
┝━> [2] Ubah Data              │ Mengganti/mengatur data  │
┝━> [3] Hapus Data             │ Menghapus data           │
┝━> [4] Lihat Daftar Pustaka   │ Melihat Daftar/List data │
┝━> [5] Selesai                │ Keluar Program           │
└──────────────────────────────┴──────────────────────────┘''')

        try:
            opsi = int(input(Fore.MAGENTA + '''
  ╭──────────────╮
┏━┥ masukan opsi │
┃ ╰──────────────╯
┗━━━━━➤  ''' + Style.RESET_ALL))
            if opsi == 1:
                masukan_data()
            elif opsi == 2:
                ubah_data()
                simpan_data()
            elif opsi == 3:
                hapus_data()
                simpan_data()
            elif opsi == 4:
                layar()
                input(Back.LIGHTBLUE_EX + 'Tekan enter untuk melihat daftar pustaka . . .' + Back.RESET)
                lihat_daftar()
                input(Back.LIGHTBLUE_EX + 'Tekan enter untuk melanjutkan . . .' + Back.RESET)
                simpan_data()
            elif opsi == 5:
                print(Fore.CYAN + '''
              ╭────────────────────────────────────────────────────────────────────╮
              │ ~~~ Terimakasih telah menggunakan daftar pustaka sederhana ini ~~~ │
              ╰────────────────────────────────────────────────────────────────────╯
              ''')
                exit()
            else:
                print(Fore.RED + "masukan angka dari 1-5!")
        except ValueError:
            print(Fore.RED + "masukan angka dari 1-5!")

tampilan_utama()

simpan_data()