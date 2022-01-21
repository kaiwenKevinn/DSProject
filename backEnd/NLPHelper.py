import os

from Extracter import Extracter
from Parser import Parser


class NLPHelper:
    def __init__(self, filename='text.txt'):
        self.parser = Parser(filename)
        self.extracter = Extracter()
        self.info = {}

    def process(self):
        beginning_sentences = self.parser.extract_beginning_part()
        rest_sentences = self.parser.extract_rest()
        with open(self.parser.filename, encoding='utf-8') as file:
            sentences = file.read()
        self.extracter.extract_criminal_basic_info([beginning_sentences])
        self.extracter.extract_principal_crime_info(sentences)
        self.extracter.scan_rest([rest_sentences])
        self.info['name'] = self.extracter.names
        self.info['ethnicity'] = list(set(self.extracter.ethnicity))
        self.info['birthplace'] = self.extracter.birthplace
        self.info['gender'] = self.extracter.gender
        self.info['courts'] = self.extracter.courts
        self.info['causes'] = self.extracter.causes

    """for test usage"""
    def print_out(self):
        self.extracter.print_out()


def main():
    # index = 1
    # files_txt = os.listdir(os.getcwd() + '/file_unzip/txt')
    # for file_txt in files_txt:
    #     print("index : ", index)
    #     nlp = NLPHelper('file_unzip/txt/' + file_txt)
    #     nlp.process()
    #     nlp.print_out()
    #     index += 1
    nlp = NLPHelper('helper_debug/sample1.txt')
    nlp.process()
    nlp.print_out()


if __name__ == '__main__':
    main()
