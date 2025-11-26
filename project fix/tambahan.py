import os

def layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_authors(authors):
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    else:
        return ", ".join(authors[:-1]) + f", & {authors[-1]}"

def format_authorsAND(authors):
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    else:
        return ", ".join(authors[:-1]) + f", and {authors[-1]}"

def format_akhir_awalinisial(authors):
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

    return format_authors(format_akhir_inisial)

def format_awalinisial_akhir(authors):
    format_awal_inisial = []
    
    for name in authors:
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

    return format_authorsAND(format_awal_inisial)


def format_et_al(authors):
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}."
    else:
        return f"{authors[0]}, et al."

def format_akhir_awalinisial_tanpakoma(authors):
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

    return format_authors(format_akhir_inisial_tanpakoma)

def tanpa_koma(nama):
    nama_split = [bagian.strip() for bagian in nama.split(",")]

    if len(nama_split) == 2:
        akhir = nama_split[0]
        awal = nama_split[1]
        return f"{akhir} {awal}" 
    else:
        return nama

def format_tanpakoma_semua(authors):
    tanpa_koma_semua = []
    for nama in authors:
        tanpa_koma_semua.append(tanpa_koma(nama))
    penulis = tanpa_koma_semua 
    if len(penulis) == 1:
        return penulis[0]       
    elif len(penulis) == 2:
        return f"{penulis[0]} & {penulis[1]}"
    else:
        semua_kecuali_terakhir = ", ".join(penulis[:-1])
        return semua_kecuali_terakhir + f", & {penulis[-1]}"

def format_tanpakoma_semuaeditor(editors):
    tanpa_koma_semua = []
    for nama in editors:
        tanpa_koma_semua.append(tanpa_koma(nama))
    editor = tanpa_koma_semua 
    if len(editor) == 1:
        return editor[0] + f", Ed."       
    else:
        semua_kecuali_terakhir = ", ".join(editor[:-1])
        return semua_kecuali_terakhir + f", & {editor[-1]}, Eds."

def balik_nama(nama):
    nama_split = [bagian.strip() for bagian in nama.split(",")]

    if len(nama_split) == 2:
        akhir = nama_split[0]
        awal = nama_split[1]
        return f"{awal} {akhir}" 
    else:
        return nama

# def balik_semua_nama(authors):
#     hasil = []
#     for nama in authors:
#         hasil.append(balik_nama(nama))
#     penulis = hasil 
#     if len(penulis) == 1:
#         return penulis[0]       
#     elif len(penulis) == 2:
#         return f"{penulis[0]} and {penulis[1]}"
#     else:
#         semua_kecuali_terakhir = ", ".join(penulis[:-1])
#         return semua_kecuali_terakhir + f", and {penulis[-1]}"

def format_edition(edition):
    if not edition:
        return ""
    try:
        n = int(edition)
    except ValueError:
        return edition

    if n % 10 == 1 and n % 100 != 11:
        suffix = "st"
    elif n % 10 == 2 and n % 100 != 12:
        suffix = "nd"
    elif n % 10 == 3 and n % 100 != 13:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{n}{suffix} ed.,"

def format_editors_et_al(editors):
    tanpa_koma_semua = []
    for nama in editors:
        tanpa_koma_semua.append(balik_nama(nama))
    editors = tanpa_koma_semua 
    if not editors:
        return ""
    if len(editors) == 1:
        return f"Edited by {editors[0]}.,"
    elif len(editors) == 2:
        return f"Edited by {editors[0]} & {editors[1]}.,"
    else:
        return f"Edited by {editors[0]} et al.,"

def format_editors_and(editors):
    tanpa_koma_semua = []
    for nama in editors:
        tanpa_koma_semua.append(balik_nama(nama))
    editors = tanpa_koma_semua 
    if not editors:
        return ""
    if len(editors) == 1:
        return f"Edited by {editors[0]}.,"
    elif len(editors) == 2:
        return f"Edited by {editors[0]} & {editors[1]}.,"
    else:
        return f"Edited by {", ".join(editors[:-1])}" + f", and {editors[-1]}."

def balik_semua_namaeditors(editors):
    hasil = []
    for nama in editors:
        hasil.append(balik_nama(nama))
    editors = hasil 
    if len(editors) == 1:
        return f"{editors[0]}, Ed."
    else:
        semua_kecuali_terakhir = ", ".join(editors[:-1])
        return semua_kecuali_terakhir + f", & {editors[-1]}, Eds."

def format_et_al_lebihdari3(authors):
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
        return f"{format_akhir_inisial[0]} & {format_akhir_inisial[1]}."
    elif len(format_akhir_inisial) == 3:
        return f"{format_akhir_inisial[0]}, {format_akhir_inisial[1]} & {format_akhir_inisial[2]}."
    else:
        return f"{format_akhir_inisial[0]}, et al."

    return format_et_al_lebihdari3(format_akhir_inisial)