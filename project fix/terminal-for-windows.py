import os #mengimport modul os(sistem operasi) mengakses terminal, nama os, dll
'''bikin variable setup_path untuk membungkus nilai dan akan di buka(dikeluarkan nilainya) di line 4 kolom 47,
panggil fungsi untuk mengembalikan path file(entah itu file ataupun folder) itu berada di folder mana
submodul path disini untuk menghandle lokasi yang mana di dalem submodul path itu sendiri terdapat banyak fungsi, salah satunya .join(). parameter join yaitu join(path, *path).
apa maksudnya *, ini bisa di sebut sebagai variadic arguments(menambahkan path file sebanyak mungkin)''' #ini adalah komentar multibaris
setup_path = os.path.join(f"{os.path.dirname(__file__)}", "setup.py") 
startTerminal = os.system(f'start /MAX wt py "{setup_path}"')# buka terminal dari microsoft, kalau sistem operasinya macos atau linux ,dll maka lewatkan
if startTerminal != 0: #jika nilai dari start terminal bukan 0 maka akan menuju ke website microsoft untuk mendownload terminal dari mcrisorf
    os.system(r'start "C:\Program Files\Google\Chrome\Application\chrome.exe" https://apps.microsoft.com/detail/9n0dx20hk701' if os.name == 'nt' else '') #r'' adalah raw-string, fungsinya dia tidak akan membaca karakter back-slash(\)