import os
import sys


def default_seg_strategy(sentence):
    flags = ['现在押', '现已刑满释放']
    try:
        index = sentence.rindex(flags[0])
    except ValueError:
        try:
            index = sentence.rindex(flags[1])
        except ValueError:
            raise ValueError
    return index


def alternative_seg_strategy(sentence):
    flags = ['现羁押于', '待扩展']
    try:
        index = sentence.rindex(flags[0])
    except ValueError:
        try:
            index = sentence.rindex(flags[1])
        except ValueError:
            raise ValueError
    return index


class Parser:
    def __init__(self, filename='text.txt'):
        self.filename = filename
        self.first_seg = ''
        self.second_seg = ''

    def extract_beginning_part(self, seg_strategy=default_seg_strategy):
        with open(self.filename, encoding='utf-8') as f:
            sentence = f.read()
        try:
            index = seg_strategy(sentence)
        except ValueError:
            print('bad input:'+self.filename)
            sys.exit()
        self.first_seg = sentence[:index]
        self.second_seg = sentence[index:]
        return sentence[:index]

    def extract_rest(self):
        assert self.first_seg != ''
        return self.second_seg


def main():
    with open('test.txt', 'w', encoding='utf-8') as test:
        counter = 0
        for file in os.listdir('data'):
            with open('data/'+file, encoding='utf-8') as f:
                parser = Parser('data/'+file)
                test.write('file '+str(counter)+':\n')
                test.write(parser.extract_beginning_part()+'\n')
                counter += 1


if __name__ == '__main__':
    main()