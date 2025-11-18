from tambahan import layar
from dafpus_manager import masukan_data, lihat_daftar, ubah_data, hapus_data, muat_data, simpan_data
from format_style import format_styles
from colorama import Fore, Style, init

init(autoreset=True)

muat_data()
layar()

def tampilan_utama():
    layar()
    print(Fore.CYAN + "-"*100)
    print(Fore.LIGHTGREEN_EX + f"{'~~~ DAFTAR PUSTAKA ~~~':^100}")
    print(Fore.CYAN + "-"*100)
    print(Fore.MAGENTA + "\nSelamat Datang!")

    while True:
        print(Fore.CYAN + "_"*100)
        print(Fore.YELLOW + "\nSilahkan Pilih!")
        print(Fore.YELLOW + "1. Masukan Data")
        print(Fore.YELLOW + "2. Ubah Data")
        print(Fore.YELLOW + "3. Hapus Data")
        print(Fore.YELLOW + "4. Lihat Daftar Pustaka")
        print(Fore.YELLOW + "5. Selesai")

        try:
            opsi = int(input(Fore.MAGENTA + "\nmasukan opsi : " + Style.RESET_ALL))
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
                lihat_daftar()
                simpan_data()
            elif opsi == 5:
                print(Fore.CYAN + "~~~ Terimakasih telah menggunakan daftar pustaka sederhana ini ~~~")
                break
            else:
                print(Fore.RED + "masukan angka dari 1-5!")
        except ValueError:
            print(Fore.RED + "masukan angka dari 1-5!")

tampilan_utama()

simpan_data()