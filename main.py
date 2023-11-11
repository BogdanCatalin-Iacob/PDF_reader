'''
Extract text from pdf file
'''
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    '''
    Takes a pdf file and return the text content of that file
    '''
    with open(pdf_file, 'rb') as pdf:
        # strict=False allows reading pdf file even if there are some errors
        reader = PdfReader(pdf, strict=False)

        print('Pages: ', len(reader.pages))
        print('-' * 10)  # divider

        # extract the text of each page
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def main():
    '''
    Main function
    '''
    extracted_text: list[str] = extract_text_from_pdf(
        'assets/Free_Test_Data_100KB_PDF.pdf')
    print(extracted_text)


if __name__ == '__main__':
    main()
