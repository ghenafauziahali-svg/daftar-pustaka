from tambahan import format_authors, format_authorsAND, format_akhir_awalinisial, format_awalinisial_akhir, format_et_al, format_akhir_awalinisial_tanpakoma, format_tanpakoma_semua, balik_semua_nama, format_edition, format_editors_et_al, format_tanpakoma_semuaeditor, format_editors_and, balik_semua_namaeditors

def format_styles(data):
    tipe_styles = data['style']
    referensi = data['referensi']

    issue_formatkurung = f"({data['issue']})" if data['issue'] else ""
    issue_formatNO = f"no. {data['issue']}," if data['issue'] else ""
    if data['volume']:
        volume_format = f"vol. {data['volume']},"
    else:
        volume_format = ""

    if data['link']:
        link_format = f", {data['link']}"
    else:
        link_format = ""
        
    if data['city']:
        city_format = f"{data['city']}:"
    else:
        city_format = ""
    
    if data['halaman']:
        hal_formatPP = f"pp. {data['halaman']}"
    else:
        hal_formatPP = ""

    if data['halaman']:
        hal_formatP = f"{data['halaman']} p."
    else:
        hal_formatP = ""

    if data['halaman']:
        hal_formatHH = f"hh. {data['halaman']}"
    else:
        hal_formatHH = ""

    if data['tahun']:
        format_tahunkurung = f"({data['tahun']})."
    else:
        format_tahunkurung = ""

    if data['chapter']:
        chap_format = f"ch. {data['chapter']},"

    edition_format = format_edition(data['edition'])

    if referensi == "Journal/Article":
        if tipe_styles == "APA":
            return f"{format_akhir_awalinisial(data['authors'])}. {format_tahunkurung} {data['judul']}. {data['jurnal']}, {data['volume']}{issue_formatkurung} {data['halaman']}{link_format}."
        elif tipe_styles == "IEEE":
            return f"{format_awalinisial_akhir(data['authors'])}, \"{data['judul']},\" {data['jurnal']}, {volume_format}{issue_formatNO}{hal_formatPP} {data['tahun']}{link_format}."
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])} \"{data['judul']}.\" {data['jurnal']}, {volume_format}{issue_formatNO}{data['tahun']}, {hal_formatPP}{link_format}."
        elif tipe_styles == "Harvard":
            return f"{format_akhir_awalinisial(data['authors'])} {data['tahun']}, '{data['judul']}', \x1B[3m{data['jurnal']}\x1B[0m,{volume_format} {issue_formatNO} {hal_formatHH}{link_format}."
        else:
            return f"{format_akhir_awalinisial_tanpakoma(data['authors'])}. {data['judul']}. {data['jurnal']}. {data['tahun']};{data['volume']}{issue_formatkurung}:{data['halaman']}{link_format}."

    elif referensi == "Book":
        if tipe_styles == "APA":
            return f"{format_authors(data['authors'])}. {format_tahunkurung} {data['judul']} ({balik_semua_namaeditors(data['editors'])};{edition_format} {volume_format}). {data['publisher']}{link_format}."
        elif tipe_styles == "IEEE":
            return f"{balik_semua_nama(data['authors'])}, {data['judul']}, {edition_format}{volume_format}. {city_format} {data['publisher']} {data['tahun']}{link_format}."
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])} {data['judul']}. {format_editors_et_al(data['editors'])} {edition_format}{volume_format}{city_format} {data['publisher']}, {data['tahun']}{link_format}."
        elif tipe_styles == "Harvard":
            return f"{format_authorsAND(data['authors'])} {format_tahunkurung} {data['judul']}. {edition_format} {format_editors_and(data['editors'])} {city_format} {data['publisher']}{link_format}."
        else:
            return f"{format_tanpakoma_semua(data['authors'])}. {data['judul']}. {edition_format} {format_tanpakoma_semuaeditor(data['editors'])} {volume_format} {city_format} {data['publisher']}; {data['tahun']}. {hal_formatP}{link_format}"

    else:
        if tipe_styles == "APA":
            return f"{format_authors(data['authors'])}. {format_tahunkurung} {data['judul']}. In {balik_semua_namaeditors(data['editors'])} {data['book']} ({edition_format} {volume_format} {hal_formatPP}). {data['publisher']}{link_format}"
        elif tipe_styles == "IEEE":
            return f"{balik_semua_nama(data['authors'])}, \"{data['judul']},\" in {data['book']}, {edition_format}{volume_format}{balik_semua_namaeditors(data['editors'])} {city_format} {data['publisher']}, {data['tahun']}, {chap_format} {hal_formatPP}{link_format}."
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])} \"{data['judul']}.\" {data['book']}, {format_editors_et_al(data['editors'])} {edition_format} {volume_format} {data['publisher']}, {data['tahun']}, {hal_formatPP}{link_format}."
        elif tipe_styles == "Harvard":
            return f"{format_et_al(data['authors'])} {format_tahunkurung} \"{data['judul']},\" in {balik_semua_namaeditors(data['editors'])} {data['book']}. {edition_format} {city_format} {data['publisher']}, {hal_formatPP}{link_format}."
        else:
            return f"{format_tanpakoma_semua(data['authors'])}. {data['judul']}. In: {format_tanpakoma_semuaeditor(data['editors'])} {data['book']}. {edition_format} {city_format} {data['publisher']}; {data['tahun']}. {hal_formatP}{link_format}."

