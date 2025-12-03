import os # Mengimport modul os untuk mengakses terminal Sistem Operasi(windows,macOs, linux, dll)
from colorama import Style #impor fungsi init() dari library colorama untuk mengaktifkan mengatur warna di terminal

def layar():
    os.system('cls' if os.name == 'nt' else 'clear') # jalankan perintah cls jika OS windows, jalankan 'clear' jika OSnya bukan windows

def format_authorsAND(authors):
    if len(authors) == 1: # Jika cuman ada 1 penulis, langsung tulis penulis dengan ada koma nya
        return f"{authors[0]},"
    elif 2 <= len(authors) <= 6: #klo ppenulis lebih besar atau sama dengan 2 sampai 6 semua penulis kecuali penulis terakhir di gabung dan di antara semua penulis, gabungin penulis terakhir dengan , and ....'
        return ", ".join(authors[:-1]) + f", and {authors[-1]},"
    elif len(authors) > 6:
        return f"{authors[0]} et al.," #klo lebih dari 6 maka pakaipemformatan er al.,

def format_IEEE(authors): # fungsi format daftar pustaka Institute of Electrical and Electronics Engineers
    format_awal_inisial = [] # tempat menampung data sementara
    
    for name in authors: #masukan satu persatu data authors ke variiable name
        if "," in name: #jika di temuin ',' di dalem variable name maka format di balik
            nama_split = [bagian.strip() for bagian in name.split(",")] #split yaitu pemisah string entah itu pake ,,- dan lain2, buat variable nama_split dengn tipe data list, yang di dalamnya bikin pemisah string, 1 persatu, lalu hapus spasi depan dan belakang kata
            akhir = nama_split[0] # nama belakang di definisiin index ke 0
            awal = nama_split[1] # nama depan di definisiin index ke 1 (belakang)
            # Memecah nama depan jadi beberapa bagian untuk ambil inisial
            inisial_split = awal.strip().split() #hapus spasi di depan & belakang, pcah nama sesuai spasi
            inisial_format = " ".join([f"{p[0]}." for p in inisial_split]) #list untuk ambil huruf pertama dari tiap kata
            format_awal_inisial.append(f"{inisial_format} {akhir}") # inisial format nama akhir di tambahinke variable format_awal_inisial=[]
        else: #kondisi ini di pake untuk nama gapake koma
            nama_split = name.strip().split() #pecahin nama2, tanpa spasi
            if len(nama_split) > 1: #klo panjang karakter nama lebih besar dari 1 maka ambil akhir kata nama atau nama terakhir
                akhir = nama_split[-1]
                inisial = " ".join([f"{p[0]}." for p in nama_split[:-1]]) # ambil inisial setiap kata, kecuali kata terakhir
                format_awal_inisial.append(f"{inisial} {akhir}") #inisial di gabungin ama nama akhir
            else:
                format_awal_inisial.append(name) # klo cuma 1 kata doang gaperlu di split, langsung be di tanmbahin ke format_awal_inisial

    return format_authorsAND(format_awal_inisial) # output isi variale format_awal_inisial

def editor_IEEE(editors):
    formatted = format_IEEE(editors)
    if not editors:
        return "" #klo gada editors, maka nilai kuncinya editors string kosong
    elif len(editors) == 1:
        return f"{formatted} Ed.," # kalau jumlah penulisnya sama dengan 1 pakai format Ed.,
    else:
        return f"{formatted} Eds.," # selain 1?  pakai Eds.,

def editor_IEEE(editors):
    formatted = format_IEEE(editors)
    if not editors:
        return ""
    elif len(editors) == 1:
        return f"{formatted} Ed.,"
    else:
        return f"{formatted} Eds.,"

def format_et_al(authors):
    if len(authors) == 1:
        return authors[0]
    elif 2 <= len(authors) <= 6:
        return ", ".join(authors[0:])
    elif len(authors) > 6:
        return f"{authors[0]}, et al."

def format_vancouver(authors):
    format_akhir_inisial_tanpakoma = []
    
    for name in authors:
        if "," in name:
            nama_split = [bagian.strip() for bagian in name.split(",")]
            akhir = nama_split[0]
            awal = nama_split[1]
            inisial_split = awal.strip().split()
            inisial_format = "".join([f"{p[0]}" for p in inisial_split])
            format_akhir_inisial_tanpakoma.append(f"{akhir} {inisial_format}")
        else:
            nama_split = name.strip().split()
            if len(nama_split) > 1:
                akhir = nama_split[-1]
                inisial = "".join([f"{p[0]}" for p in nama_split[:-1]])
                format_akhir_inisial_tanpakoma.append(f"{akhir} {inisial}")
            else:
                format_akhir_inisial_tanpakoma.append(name)
    return format_et_al(format_akhir_inisial_tanpakoma)

def editor_vancouver(editors):
    formatted = format_vancouver(editors)
    if not editors:
        return ""
    elif len(editors) == 1:
        return f"{formatted}, editor."
    else:
        return f"{formatted}, editors."

def balik_nama(nama): # membalikkan nama yang belakang jadi di depan, yang di depan jadi di belakang, yang tengah? ya tetep tengah dunn
    nama_split = [bagian.strip() for bagian in nama.split(",")] # pecahin nama jadi list seuai tanda (,)

    if len(nama_split) == 2: #klo panjang splitnya 2 jalannin statement ini
        akhir = nama_split[0] #nama akhir jadi awal
        awal = nama_split[1] # nama awal jadi apa?? ya btul jadi akhir :V
        return f"{awal} {akhir}" #print nama akhir lalu nama awal
    else:
        return nama #klo cuma 1 kata doang namanya ya keluarin itu aja
    
def format_MLA(authors):
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        author2 = balik_nama(authors[1])
        return f"{authors[0]} and {author2}." # kalo format author MLA itu pake kata and, ini klo 2 orang
    else:
        return f"{authors[0]}, et al." #lebih dari 2 orang? paake format et al.

def format_edition(edition):
    if not edition:
        return ""
    try:
        n = int(edition)
    except ValueError: # klo masukin huruf bakal kembaliin nilai edition, program tetep jalan
        return edition

    #ubah angka “edition” menjadi format bahasa Inggris 1st 2nd 3rd -11th(spesial case), 21st,2nd,23rd 24th dst
    if n % 10 == 1 and n % 100 != 11: # misal 21 %10 = sisa 1 maka suffixnya st
        suffix = "st"
    elif n % 10 == 2 and n % 100 != 12:
        suffix = "nd"
    elif n % 10 == 3 and n % 100 != 13:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{n}{suffix} ed.," # sisa 1 tadi suffixnya st, maka n tadi 21 + suffixnya yaitu st jadi 21st

def format_editors_mla(editors):
    tanpa_koma_semua = []
    for nama in editors:
        tanpa_koma_semua.append(balik_nama(nama))
    editors = tanpa_koma_semua 
    if not editors:
        return ""
    elif len(editors) == 1:
        return f"edited by {editors[0]}.,"
    elif len(editors) == 2:
        return f"edited by {editors[0]} and {editors[1]}.,"
    else:
        return f"edited by {editors[0]} et al.,"

def format_HARVARD(authors): # Formart gaya HARVARD
    format_akhir_inisial = []
    for name in authors:
        if "," in name:
            nama_split = [bagian.strip() for bagian in name.split(",")]
            akhir = nama_split[0]
            awal = nama_split[1]
            inisial_split = awal.strip().split()
            inisial_format = " ".join([f"{p[0]}." for p in inisial_split])
            format_akhir_inisial.append(f"{akhir}, {inisial_format}")
        else:
            nama_split = name.strip().split()
            if len(nama_split) > 1:
                akhir = nama_split[-1]
                inisial = " ".join([f"{p[0]}." for p in nama_split[:-1]])
                format_akhir_inisial.append(f"{akhir}, {inisial}")
            else:
                format_akhir_inisial.append(name)
    
    if len(format_akhir_inisial) == 1:
        return format_akhir_inisial[0]
    elif len(format_akhir_inisial) == 2:
        return f"{format_akhir_inisial[0]} & {format_akhir_inisial[1]}"
    elif len(format_akhir_inisial) >= 3:
        return ", ".join(format_akhir_inisial[:-1]) + f", & {format_akhir_inisial[-1]}"

def editor_HARVARD(editors):
    formatted = format_HARVARD(editors)
    if not editors:
        return "" 
    elif len(editors) == 1:
        return f"{formatted}, (Ed.);"
    else:
        return f"{formatted}, (Eds.);"

def format_APA(authors): #format gaya APA
    format_akhir_inisial = []
    for name in authors:
        if "," in name:
            nama_split = [bagian.strip() for bagian in name.split(",")]
            akhir = nama_split[0]
            awal = nama_split[1]
            inisial_split = awal.strip().split()
            inisial_format = " ".join([f"{p[0]}." for p in inisial_split])
            format_akhir_inisial.append(f"{akhir}, {inisial_format}")
        else:
            nama_split = name.strip().split()
            if len(nama_split) > 1:
                akhir = nama_split[-1]
                inisial = " ".join([f"{p[0]}." for p in nama_split[:-1]])
                format_akhir_inisial.append(f"{akhir}, {inisial}")
            else:
                format_akhir_inisial.append(name)
    
    if len(format_akhir_inisial) == 1:
        return format_akhir_inisial[0]
    elif 2 <= len(format_akhir_inisial) <= 20:
        return ", ".join(format_akhir_inisial[:-1]) + f", & {format_akhir_inisial[-1]}"
    elif len(format_akhir_inisial) > 20:
        return ", ".join(format_akhir_inisial[:19]) + f", ..." + format_akhir_inisial[-1]

def editor_APAbook(editors):
    formatted = format_APA(editors)
    if not editors:
        return "" 
    if len(editors) == 1:
        return f"{formatted}, (Ed.);" # klo editornya cuma 1 pake format (Ed.);
    else:
        return f"{formatted}, (Eds.);" # klo lebih? pake yang Eds

def editor_booksectionAPA(editors):
    format_awal_inisial = []
    
    for name in editors:
        if "," in name:
            nama_split = [bagian.strip() for bagian in name.split(",")]
            akhir = nama_split[0]
            awal = nama_split[1]
            inisial_split = awal.strip().split()
            inisial_format = " ".join([f"{p[0]}." for p in inisial_split])
            format_awal_inisial.append(f"{inisial_format} {akhir}")
        else:
            nama_split = name.strip().split()
            if len(nama_split) > 1:
                akhir = nama_split[-1]
                inisial = " ".join([f"{p[0]}." for p in nama_split[:-1]])
                format_awal_inisial.append(f"{inisial} {akhir}")
            else:
                format_awal_inisial.append(name)
    if not format_awal_inisial:
        return "" 
    if len(format_awal_inisial) == 1:
        return f"{format_awal_inisial[0]}, (Ed),"
    elif 2 <= len(format_awal_inisial) <= 20:
        return ", ".join(format_awal_inisial[:-1]) + f", & {format_awal_inisial[-1]}, (Eds.),"
    elif len(format_awal_inisial) > 20:
        return ", ".join(format_awal_inisial[:19]) + f", ...{format_awal_inisial[-1]}, (Eds.),"
