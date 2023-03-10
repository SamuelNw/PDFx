# Using PyPDF2 to perform major operations on PDF documents.
import PyPDF2
import os


# Give the paths to said PDF docs.
watermark_pdf = "./test_files/wtr.pdf"

# Folders
watermark_source_folder = "./test_files"
watermark_destination_folder = "./worked_on_files/watermark/"

password_source_folder = "./test_files"
password_destination_folder = "./worked_on_files/password/"


class PDFx(object):
    def __init__(self):
        pass

    # Incase the destination folder is not given, a new "watermarked_pdfs/" directory is created.
    def watermark(self, source, watermark, output="watermarked_pdfs/"):
        """
        Info: Adds a watermark to all pages of all the documents form a given source.
        - Create the output directory if it is not given.
        - Loop through the source folder and carry out the following on each doc:
            - Initiate a reader object with the source document.
            - Do the same for the writer object.
            - Get the number of pages to determine the number of iterations.
            - Looping through as many times as the number of pages, merge each page
            with a similar instance of the reader object with the watermark.
            - Add that result to the writer object earlier created.
            - After completion of the loops, use the cumulated writer object to write
            to the output file.
        """
        if output == "watermarked_pdfs/":
            os.makedirs(output)

        for pdf in os.listdir(source):
            # acquire the filename
            filename = os.path.split(pdf)[1]
            filename = os.path.splitext(filename)[0]

            source_reader = PyPDF2.PdfReader(f"{source}/{pdf}")
            num_of_pages = len(source_reader.pages)

            writer = PyPDF2.PdfWriter()

            for index in range(num_of_pages):
                content_page = source_reader.pages[index]

                stamp_reader = PyPDF2.PdfReader(watermark)
                # watermark is on the first page
                watermark_page = stamp_reader.pages[0]

                """
                Important note.
                - The .merge_page() method withholds the page that comes just before the dot
                and overlays the one in brackets over it.
                """
                watermark_page.merge_page(content_page)
                writer.add_page(watermark_page)

            with open(f"{output}{filename}.pdf", "wb") as file:
                writer.write(file)

        print("Done")

    def password_protect(self, pro_source, pro_destination="protected_pdfs/"):
        """
        Info: Works to encrypt all the PDF files in the given source folder
        and stores the resultant password-protected pdfs in a new directory.
        - Create a folder for the resulting files if one is not given.
        - Get the password to be used from the user.
        - Loop through all docs in the source folder and do the following to each:
            - Create a reader object with the target document.
            - Initiate a writer object.
            - Add each page of the target document to the writer.
            - Encrypt the writer.
            - Write it all to the new file
        """
        if pro_destination == "protected_pdfs/":
            os.makedirs(pro_destination)

        password = input("Enter the password to use on this document: ")

        for pdf in os.listdir(pro_source):
            # Separate and store the filename
            filename = os.path.split(pdf)[1]
            filename = os.path.splitext(filename)[0]

            reader = PyPDF2.PdfReader(f"{pro_source}/{pdf}")
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            with open(f"{pro_destination}{filename}.pdf", "wb") as file:
                writer.write(file)

        print("Done")


# Instantiate the class.
work = PDFx()

# Watermarks all the documents in the source folder and store them in the destination folder.
# work.watermark(watermark_source_folder, watermark_pdf)

# Encrypts the files in the source folder with the password a user gives, creates the destination
# folder and stores them there.
# work.password_protect(password_source_folder)
