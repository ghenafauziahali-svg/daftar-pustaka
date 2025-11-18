from tambahan import format_authors, format_akhir_awalinisial, format_awalinisial_akhir, format_et_al, format_akhir_awalinisial_tanpakoma, format_tanpakoma_semua, balik_semua_nama, format_edition, format_editors_et_al

def format_styles(data):
    tipe_styles = data['style']
    referensi = data['referensi']

    issue_formatkurung = f" ({data['issue']})" if data['issue'] else ""
    issue_formatNO = f" no. {data['issue']}," if data['issue'] else ""
    if data['volume']:
        volume_format = f", vol. {data['volume']},"
    else:
        volume_format = ""

    if data['link']:
        link_format = f", {data['link']}"
    else:
        link_format = ""

    if data['editors']:
        editors_str = ", ".join(data['editors'])
        if len(data['editors']) > 1:
            editors_format = f"{editors_str}, Eds."
        else:
            editors_format = f"{editors_str}, Ed."
    else:
        editors_format = ""
        
    if data['city']:
        city_format = f"{data['city']}:"
    else:
        city_format = ""

    edition_format = format_edition(data['edition'])

    if referensi == "Journal/Article":
        if tipe_styles == "APA":
            return f"{format_akhir_awalinisial(data['authors'])}. ({data['tahun']}). {data['judul']}. {data['jurnal']} {data['volume']}{issue_formatkurung}{data['halaman']}{link_format}."
        elif tipe_styles == "IEEE":
            return f"{format_awalinisial_akhir(data['authors'])}, \"{data['judul']},\" {data['jurnal']}{volume_format}{issue_formatNO} pp. {data['halaman']}, {data['tahun']}{link_format}."
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])}. \"{data['judul']}.\" {data['jurnal']}{volume_format}{issue_formatNO} {data['tahun']}, pp. {data['halaman']}{link_format}."
        elif tipe_styles == "Harvard":
            return f"{format_akhir_awalinisial(data['authors'])} {data['tahun']}, '{data['judul']}', {data['jurnal']}, {volume_format}{issue_formatNO}, hh. {data['halaman']}{link_format}"
        else:
            return f"{format_akhir_awalinisial_tanpakoma(data['authors'])}. {data['judul']}. {data['jurnal']}. {data['tahun']};{data['volume']}{issue_formatkurung}:{data['halaman']}{link_format}"

    elif referensi == "Book":
        if tipe_styles == "APA":
                return f"{format_authors(data['authors'])}. ({data['tahun']}). {data['judul']} ({editors_format};{edition_format}{volume_format}). {data['publisher']}{link_format}"
        elif tipe_styles == "IEEE":
            return f"{balik_semua_nama(data['authors'])}, {data['judul']}, {edition_format}{volume_format}. {city_format} {data['publisher']}, {data['tahun']}{link_format}"
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])}. {data['judul']}. {format_editors_et_al(data['editors'])} {edition_format}{volume_format} {city_format} {data['publisher']}, {data['tahun']}{link_format}"
        elif tipe_styles == "Harvard":
            return f"{format_authors(data['authors'])}. ({data['tahun']}) {data['judul']}. {edition_format} {editors_format} {city_format} {data['publisher']}{link_format}"
        else:
            return f"{format_tanpakoma_semua(data['authors'])}. {data['judul']}. {edition_format} {editors_format} {volume_format}. {city_format} {data['publisher']}; {data['tahun']}. {data['halaman']} p.{link_format}"

    else:
        if tipe_styles == "APA":
            return f"{format_authors(data['authors'])}. ({data['tahun']}). {data['judul']}. In {editors_format}, {data['book']} ({edition_format}, {volume_format} pp. {data['halaman']}). {data['publisher']}{link_format}"
        elif tipe_styles == "IEEE":
            return f"{balik_semua_nama(data['authors'])}, \"{data['judul']}\", in {data['book']}, {edition_format}, {volume_format}, {editors_format}., {city_format} {data['publisher']}, {data['tahun']}, ch. {data['chapter']}, pp. {data['halaman']}{link_format}."
        elif tipe_styles == "MLA":
            return f"{format_et_al(data['authors'])}. \"{data['judul']}.\" {data['book']}, {format_editors_et_al(data['editors'])}., {edition_format}, {volume_format}, {data['publisher']}, {data['tahun']}, pp. {data['halaman']}{link_format}"
        elif tipe_styles == "Harvard":
            return f"{format_et_al(data['authors'])}. ({data['tahun']}) \"{data['judul']}\",in {editors_format} {data['book']}. {edition_format} {city_format} {data['publisher']}, pp. {data['halaman']}{link_format}."
        else:
            return f"{format_tanpakoma_semua(data['authors'])}. {data['judul']}. In: {editors_format}. {data['book']}. {edition_format} {city_format} {data['publisher']}; {data['tahun']}. p. {data['halaman']}{link_format}."

