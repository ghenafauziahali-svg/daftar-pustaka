import os #mengimport modul os(sistem operasi) mengakses terminal, nama os, dll

while True:
    os.system('cls') #bersihkan layar
    # konfigurasi setup
    print(r'''
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
    headerStp = '█' * 72 #bikin header dengan f-string
    # list konfigurasi yang tersedia
    print(f'''{headerStp}
██ {'Mengecek . . .':^66} ██
{headerStp}
██ ⮞ [A] Python                   █ Cek versi python berapa 🤔        ██
██ ⮞ [B] Install Modul Colorama   █ Penting 🛠                         ██
██ ⮞ [C] Main                     █ Mulai Program                     ██
{headerStp}''') #len(headerstp) yaitu mengecek panjang element di tambah 1 agar bisa sejajar dengan len yang atas(headerStp)
    # konfirmasi
    setupQuest = input('''  ╭───────────────────────────────────────────────────────╮
┏━┥  Tekan [ENTER ⤷] untuk mengecek apakah ada trouble ?  │
┃ ╰───────────────────────────────────────────────────────╯
┗━━━━━➤  ''')
    try:
        # mengecek versi python
        os.system('python --version')
        input('''┏━━━━━━━━━━━━━━━━━┓
┃ teken [ENTER] ⤷ ┃
┗━━━━━━━━━━━━━━━━━┛''')
    except:
        print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
▌ ADA TROUBLE NI!❌, COBA UNINSTALL ULANG PYTHON, JANGAN LUPA CENTANG OPSI "ADD PYTHON TO PATH" ▌
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    # instalasi modul colorama untuk memformat(style dan warna) text dan background
    print('''▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜
▌ SEBENTAR YAAK INSTALL MODUL COLORAMA DLU BIAR PRGRAMNYA GA ERROR 😋 ▐
▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟''')
    os.system('pip install colorama') # instalasi colorama
    input('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Wih kelar ni instal modulnya, sung gass keun teken [ENTER] ⤷ ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')#setelah kelar instalasinya maka pause terlebih dahulu
    
    # menjalankan program
    try:
        from colorama import Fore, Back, Style, init #memanggil fungsi pengubah warna text, warna background, gaya text, serta inisialisasi colorama
        init(autoreset=True) # inisialisasi colorama
        import main #seelah cek modul colorama berhasil di install maka jalankan line code 53 yaitu import modul main danjalankan modulnya
        main()
    except ModuleNotFoundError: #kalao ada modul yang belom terinstall, maka program tetap jalan dan memberi tahu kesalahan user
        input('SORY ADA TROBEL NI, COBA JALANIN LANGKAH B DLU, JANGAN LANGSUNG KE C !! [ENTER ⤷]')
        os.system('py terminal_for_windows.py') #jalanin ulang modul terminalforwindiws
        exit() #keluar dari terminal yang sebelumnya