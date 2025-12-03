from tambahan import (
    format_vancouver,
    editor_vancouver,
    format_edition,
    format_editors_mla,
    format_IEEE,
    editor_IEEE,
    format_APA,
    format_MLA,
    format_HARVARD,
    editor_HARVARD,
    editor_APAbook,
    editor_booksectionAPA
)

def format_styles(data):
    tipe_styles = data['style']
    referensi = data['referensi']

    issue_formatkurung = f"({data['issue']})" if data['issue'] else ""
    issue_formatNO = f"no. {data['issue']}," if data['issue'] else ""
    if data['volume']:
        volume_format = f"vol. {data['volume']},"
    else:
        volume_format = ""
        
    if data['city']:
        city_format = f"{data['city']}:"
    else:
        city_format = ""
    
    if data['halaman']:
        hal_formatPP = f"pp. {data['halaman']}"
    else:
        hal_formatPP = ""

    if data['halaman']:
        hal_formatP = f"p. {data['halaman']}"
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
    else:
        chap_format = ""


    edition_format = format_edition(data['edition'])

    if referensi == "Journal/Article":
        if tipe_styles == "APA":
            return f"{format_APA(data['authors'])} {format_tahunkurung} {data['judul']}. \x1B[3m{data['jurnal']}\x1B[0m, {data['volume']}{issue_formatkurung}, {data['halaman']}. {data['link']}"
        elif tipe_styles == "IEEE":
            return f"{format_IEEE(data['authors'])} \"{data['judul']},\" \x1B[3m{data['jurnal']}\x1B[0m, {volume_format}{issue_formatNO}{hal_formatPP}, {data['tahun']}. {data['link']}"
        elif tipe_styles == "MLA":
            return f"{format_MLA(data['authors'])} \"{data['judul']}.\" \x1B[3m{data['jurnal']}\x1B[0m, {volume_format}{issue_formatNO}{data['tahun']}, {hal_formatPP}. {data['link']}"
        elif tipe_styles == "Harvard":
            return f"{format_HARVARD(data['authors'])} {format_tahunkurung} {data['judul']}, \x1B[3m{data['jurnal']}\x1B[0m, {data['volume']}{issue_formatkurung} {data['halaman']}. {data['link']}"
        else:
            return f"{format_vancouver(data['authors'])}. {data['judul']}. {data['jurnal']}. {data['tahun']};{data['volume']}{issue_formatkurung}:{data['halaman']}. {data['link']}"

    elif referensi == "Book":
        if tipe_styles == "APA":
            return f"{format_APA(data['authors'])} {format_tahunkurung} \x1B[3m{data['judul']}\x1B[0m ({editor_APAbook(data['editors'])}{edition_format} {volume_format}). {data['publisher']}. {data['link']}"
        elif tipe_styles == "IEEE":
            return f"{format_IEEE(data['authors'])} \"{data['judul']},\" {editor_IEEE(data['editors'])}{edition_format}{volume_format}. {city_format} {data['publisher']}, {data['tahun']}. {data['link']}"
        elif tipe_styles == "MLA":
            return f"{format_MLA(data['authors'])} \x1B[3m{data['judul']}\x1B[0m. {format_editors_mla(data['editors'])} {edition_format}{volume_format}{city_format} {data['publisher']}, {data['tahun']}. {data['link']}"
        elif tipe_styles == "Harvard":
            return f"{format_HARVARD(data['authors'])} {format_tahunkurung} \x1B[3m{data['judul']}\x1B[0m. {edition_format} {editor_HARVARD(data['editors'])} {city_format} {data['publisher']}. {data['link']}"
        else:
            return f"{format_vancouver(data['authors'])} {data['judul']}. {edition_format} {editor_vancouver(data['editors'])} {volume_format} {city_format} {data['publisher']}; {data['tahun']}. {hal_formatP} {data['link']}"

    else:
        if tipe_styles == "APA":
            return f"{format_APA(data['authors'])} {format_tahunkurung} {data['judul']}. In {editor_booksectionAPA(data['editors'])} \x1B[3m{data['book']}\x1B[0m ({edition_format} {volume_format} {hal_formatPP}). {data['publisher']}. {data['link']}"
        elif tipe_styles == "IEEE":
            return f"{format_IEEE(data['authors'])} \"{data['judul']},\" in \x1B[3m{data['book']}\x1B[0m, {edition_format}{volume_format}{editor_IEEE(data['editors'])} {city_format} {data['publisher']}, {data['tahun']}, {chap_format} {hal_formatPP}. {data['link']}"
        elif tipe_styles == "MLA":
            return f"{format_MLA(data['authors'])} \"{data['judul']}.\" \x1B[3m{data['book']}\x1B[0m, {format_editors_mla(data['editors'])} {edition_format} {volume_format} {data['publisher']}, {data['tahun']}, {hal_formatPP}. {data['link']}"
        elif tipe_styles == "Harvard":
            return f"{format_HARVARD(data['authors'])} {format_tahunkurung} \"{data['judul']},\" in {editor_HARVARD(data['editors'])} {data['book']}. {edition_format} {city_format} {data['publisher']}, {hal_formatPP}. {data['link']}"
        else:
            return f"{format_vancouver(data['authors'])}. {data['judul']}. In: {editor_vancouver(data['editors'])} {data['book']}. {edition_format} {city_format} {data['publisher']}; {data['tahun']}. {hal_formatP}. {data['link']}"

