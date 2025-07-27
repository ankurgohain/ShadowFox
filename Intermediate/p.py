import fitz  # PyMuPDF

def extract_links_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_links = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        links = page.get_links()

        for link in links:
            if "uri" in link:
                all_links.append({
                    "page": page_num + 1,
                    "uri": link["uri"],
                    "rect": link["from"],  # the rectangle area of the link
                })

    return all_links

# Example usage
pdf_file = "C:/Users/Asus/ShadowFox/Intermediate/links.pdf"
links = extract_links_from_pdf(pdf_file)

for link in links:
    print(f"Page {link['page']}: {link['uri']} (rect: {link['rect']})")
