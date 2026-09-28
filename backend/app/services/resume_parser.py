import pymupdf

def extract_text_from_pdf(file_path):
    document = pymupdf.open(file_path)

    text = ""

    for page in document:
        blocks = page.get_text("blocks", sort=True)

        for block in blocks:
            text += block[4] + "\n"

    document.close()

    return text