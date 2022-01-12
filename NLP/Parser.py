from Extracter import Extracter


class Parser:
    def __init__(self, path):
        self.path = path
        self.basic_info = []
        self.crime_info = []
        self.rest = []

    def parse_content(self):
        with open(self.path, encoding='utf-8') as file:
            sentences = file.read()
        first_flag = '现在押'
        first_flag_alternative = '现已刑满释放'
        second_flag = '经复核确认'
        try:
            first_seg_end = sentences.index(first_flag) + len(first_flag)
        except ValueError:
            first_seg_end = sentences.index(first_flag_alternative) + len(first_flag_alternative)
        second_seg_end = sentences.index(second_flag)
        self.basic_info.append(sentences[0:first_seg_end])
        self.crime_info.append(sentences[first_seg_end:second_seg_end])
        self.rest.append(sentences[second_seg_end:])
