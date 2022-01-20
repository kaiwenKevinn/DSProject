from Extracter import Extracter
from Parser import Parser


class NLPHelper:
    def __init__(self, filename='text.txt'):
        self.parser = Parser(filename)
        self.extracter = Extracter()
        self.info = {}

    def process(self):
        self.parser.parse_content()
        self.extracter = Extracter()
        self.extracter.extract_criminal_basic_info(self.parser.basic_info)
        self.extracter.extract_principal_crime_info(self.parser.crime_info)
        self.extracter.scan_rest_sentences(self.parser.rest)
        self.extracter.extract_by_tfidf(self.parser.raw_content)

        self.info['name'] = self.extracter.names
        self.info['ethnicity'] = self.extracter.ethnicity
        self.info['birthplace'] = self.extracter.birthplace
        self.info['gender'] = self.extracter.gender
        self.info['courts'] = self.extracter.courts_concerned
        self.info['causes'] = self.extracter.causes

    """for test usage"""
    def print_out(self):
        self.extracter.print_out()


def main():
    nlp = NLPHelper()
    nlp.process()
    nlp.print_out()


if __name__ == '__main__':
    main()
