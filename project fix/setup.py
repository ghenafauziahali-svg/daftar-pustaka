import os #mengimport modul os(sistem operasi) mengakses terminal, nama os, dll
from tambahan import layar# mengimpor fungsi layar dari modul tambahan dan fungsinya untuk membersihkan layar sesuai jenis OS.

while True:
    layar() #bersihkan layar
    # konfigurasi setup
    print('''
⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀   ____    __              ___      
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀   / __/__ / /___ _____    / _ )__ __
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀ _\ \/ -_) __/ // / _ \  / _  / // /
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷ ___/\__/\__/\_,,_/.__/ /____/\_, / 
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿                /_/          /___/
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁               
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀⠀⠀⠀⡸⣿⣿⣿⣿⣿⣿⣿⣧⡀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⢀⣀⣀⣀⢀⣀⣀⣀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⡸⣿⣿⣿⡆⠀⠀⣰⣿⣿⣿⢏⣀⣀⣀⠀⣀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⡀⣀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⣀⠀⢀⣀⣀⣀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀⠀⠀⢀⣿⣿⣿⡏⢉⣿⣿⣿⠟⢠⣿⣿⣿⠿⠿⠿⠃⠀⠀⠀⠀⣼⣿⣿⡿⠉⠉⠉⠁⣼⣿⣿⠇⢪⣿⣿⣿⠀⠀⣼⣿⣿⡿⠿⠿⠿⠿⠿⠿⠃⢻⣿⣿⣿⡇⠀⣴⣿⣿⣿⠃⣰⣿⣿⡟⢰⣽⣿⣿⠿⣿⣿⣿⡷⢠⣿⣿⡿⢠⣾⣿⣿⠿⢿⣿⣿⣿⢀⣽⣿⣿⣿⠀⣼⣿⣿⠇     
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀⠀⠀⣼⣿⣿⣿⣴⣿⣿⣿⣅⠀⣾⣿⣿⣇⣀⣀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣧⣤⣤⡄⣸⣿⣿⡟⠀⢸⣿⣿⣿⠀⣼⣿⣿⡟⣀⣀⣀⣀⣀⣀⠀⠀⢸⣿⣿⣿⡇⣼⣿⣿⡿⠃⢠⣿⣿⣿⠁⣾⣿⣿⣧⣀⠛⠛⠋⠁⣿⣿⣿⠇⣼⣿⣿⡏⠀⣾⣿⣿⠇⣼⣿⣿⣿⣿⣼⣿⣿⡿⠀   
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧ ⠀⢰⣿⣿⣿⣿⠟⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⣿⣿⣿⡿⠿⠿⠟⢠⣿⣿⣿⠁⠀⢸⣿⣿⣿⣾⣿⣿⠏⢸⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⣿⣿⡏⠀⠈⠙⢿⣿⣿⣷⣦⡀⣸⣿⣿⡟⢰⣿⣿⣿⠀⢰⣿⣿⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀       
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏ ⢀⣿⣿⣿⣛⣁⣸⣿⣿⣿⢁⣿⣿⣿⣃⣀⣀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠁⠀⠀⠀⣼⣿⣿⡏⠀⠀⢸⣿⣿⣿⣿⣿⠋⢀⣿⣿⣿⣃⣀⣀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠁⠀⢰⣿⣿⡿⢠⣿⣿⣿⣀⣨⣿⣿⣿⢡⣿⣿⣿⠁⣿⣿⣿⣃⣀⣿⣿⣿⢃⣿⣿⣿⠏⣿⣿⣿⣿⡏⠀⠀       
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁  ⣸⣿⣿⣿⣿⣿⣿⣿⠟⠁⣼⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢠⣿⣿⣿⡄⠀⠀⠀⢰⣿⣿⣏⠀⠀⠀⠘⣿⣿⣿⣏⠃⠀⣼⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣿⠙⠀⠀⢀⣿⣿⣿⡁⠘⣿⣿⣿⣿⣿⣿⠟⠃⣼⣿⣿⡍⠘⣿⣿⣿⣿⣿⣿⡿⠋⣸⣿⣿⡏⠀⣿⣿⣿⣯⠀⠀     ''')                                       
    headerStp = f"{'█'*27}" + '> Konfigurasi🥱✋🏼 <' + f"{'█'*26}" #bikin header dengan f-string
    # list konfigurasi yang tersedia
    print(f'''{headerStp}
██ ⮞ [A] Python                   █ Cek versi python berapa 🤔        ██
██ ⮞ [B] Install Modul Colorama   █ Penting 🛠                         ██
██ ⮞ [C] Main                     █ Mulai Program                     ██
{"█"*(len(headerStp)+1)}''') #len(headerstp) yaitu mengecek panjang element di tambah 1 agar bisa sejajar dengan len yang atas(headerStp)
    # konfirmasi
    setupQuest = input('''  ╭─────────────────────────────────────────────────╮
┏━┥  harap pilih A terlebih dahulu, dan seterusnya  │
┃ ╰─────────────────────────────────────────────────╯
┗━━━━━➤  ''')
    # mengecek versi python
    if setupQuest == 'a' or setupQuest == 'A':
        os.system('python --version')
        input('''┏━━━━━━━━━━━━━━━━━┓
┃ teken [ENTER] ⤷ ┃
┗━━━━━━━━━━━━━━━━━┛''')
    # instalasi modul colorama untuk memformat(style dan warna) text dan background
    elif setupQuest == 'b' or setupQuest == 'B':
        print('''▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜
▌ SEBENTAR YAAK INSTALL MODUL COLORAMA DLU BIAR PRGRAMNYA GA ERROR 😋 ▐
▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟''')
        os.system('pip install colorama') # instalasi colorama
        from colorama import Fore, Back, Style, init #memanggil fungsi pengubah warna text, warna background, gaya text, serta inisialisasi colorama
        init(autoreset=True) # inisialisasi colorama
        input('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Wih kelar ni instal modulnya, sung gass keun teken [ENTER] ⤷ ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')#setelah kelar instalasinya maka pause terlebih dahulu
    # menjalankan program
    elif setupQuest == 'c' or setupQuest == 'C':
        import main
        main()
    # jika yang di masukkan bukan a/b/c maka akan diberitahu kesalahannya
    else:
        print('MOhon masukkan input yang benar dan yang sesuai ❌')