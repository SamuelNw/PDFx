# Using PyPDF2 to perform major operations on PDF documents.
import PyPDF2


# Give the paths to said PDF docs.
pdf_to_watermark = ""
watermark_pdf = ""
watermark_output_pdf = ""
encryption_target = ""
encryption_output = ""


class PDFx(object):
    def __init__(self):
        pass

    def watermark(self, source, watermark, output):
        """
        Info: Adds a watermark to all pages of given source.
        - Initiate a reader object with the source document.
        - Do the same for the writer object.
        - Get the number of pages to determine the number of iterations.
        - Looping through as many times as the number of pages, merge each page
        with a similar instance of the reader object with the watermark.
        - Add that result to the writer object earlier created.
        - After completion of the loops, use the cumulated writer object to write
        to the output file.
        """
        source_reader = PyPDF2.PdfReader(source)
        num_of_pages = len(source_reader.pages)

        stamp_reader = PyPDF2.PdfReader(watermark)

        writer = PyPDF2.PdfWriter()

        for index in range(num_of_pages):
            content_page = source_reader.pages[index]
            # watermark is on the first page
            watermark_page = stamp_reader.pages[0]

            content_page.merge_page(watermark_page)
            writer.add_page(content_page)

        with open(output, "wb") as file:
            writer.write(file)

        print("Done")

    def password_protect(self, doc_to_encrypt, encrypted_doc):
        """
        Info: Works to encrypt a PDF file.
        - Create a reader object with the target document.
        - Initiate a writer object.
        - Add each page of the target document to the writer.
        - Encrypt the writer.
        - Write it all to the new file
        """
        reader = PyPDF2.PdfReader(doc_to_encrypt)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        password = input("Enter the password to use on this document: ")
        writer.encrypt(password)

        with open(encrypted_doc, "wb") as file:
            writer.write(file)

        print("Done")
