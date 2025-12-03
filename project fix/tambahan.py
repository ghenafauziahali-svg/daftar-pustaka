import os

def layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_authorsAND(authors):
    if len(authors) == 1:
        return f"{authors[0]},"
    elif 2 <= len(authors) <= 6:
        return ", ".join(authors[:-1]) + f", and {authors[-1]},"
    elif len(authors) > 6:
        return f"{authors[0]} et al.,"

def format_IEEE(authors):
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

def balik_nama(nama):
    nama_split = [bagian.strip() for bagian in nama.split(",")]

    if len(nama_split) == 2:
        akhir = nama_split[0]
        awal = nama_split[1]
        return f"{awal} {akhir}" 
    else:
        return nama

def format_MLA(authors):
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        author2 = balik_nama(authors[1])
        return f"{authors[0]} and {author2}."
    else:
        return f"{authors[0]}, et al."

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

def format_HARVARD(authors):
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

def format_APA(authors):
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
        return f"{formatted}, (Ed.);"
    else:
        return f"{formatted}, (Eds.);"

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
