'''
Extract text from pdf file
'''
import re
from collections import Counter
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


def count_words(text_list: list[str]) -> Counter:
    '''
    Counts the most used words
    '''
    all_words: list[str] = []
    for text in text_list:
        # re expr removes symbols if they are contained by words
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        print(split_text)

        # exclude empty strings
        all_words += [word for word in split_text if word]

    return Counter(all_words)


def main():
    '''
    Main function
    '''
    extracted_text: list[str] = extract_text_from_pdf(
        'assets/Free_Test_Data_100KB_PDF.pdf')
    for page in extracted_text:
        print(page)
    counter: Counter = count_words(text_list=extracted_text)

    # top 5 words
    for word, mentions in counter.most_common(5):
        # give the word block 10 spaces length for easier reading
        print(f'{word:10}: {mentions} times')


if __name__ == '__main__':
    main()
