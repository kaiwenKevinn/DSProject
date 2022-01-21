import sys

from ltp import LTP
import jieba.analyse


def contain_stop_signs(stop_signs, string):
    for stop_sign in stop_signs:
        try:
            index = string.index(stop_sign)
            return True
        except ValueError:
            pass
    return False


class Extracter:
    def __init__(self):
        self.ltp = LTP()
        self.names = []
        self.ethnicity = []
        self.courts = []
        self.causes = []
        self.birthplace = []
        self.gender = []
        self.ltp.init_dict('dict/ltp/special_words.txt')
        self.ltp.init_dict('dict/ltp/dict.txt')
        self.ltp.init_dict('dict/ltp/dict2.txt')
        self.ltp.init_dict('dict/ltp/ultimate_accusations_dict.txt')
        self.eth_dict = {}
        self.init_ethnicity_dict()
        self.seg = None
        self.hidden = None
        self.pos = None

    def init_ethnicity_dict(self):
        with open('dict/ltp/ethnicity.txt', encoding='utf-8') as file:
            for line in file:
                self.eth_dict[line.replace('\n', '')] = True

    def seg_sentences(self, sentences):
        self.seg, self.hidden = self.ltp.seg(sentences)

    def seg_and_pos(self, sentences):
        self.seg_sentences(sentences)
        self.pos = self.ltp.pos(self.hidden)

    def extract_criminal_basic_info(self, sentences):
        self.seg_and_pos(sentences)
        birth_place_flags = ['出生于', '出生地', '户籍地', '户籍所在地', '住']
        stop_sign = ['，', '。']
        birth_place_flag = ''
        for i in range(3):
            if birth_place_flags[i] in self.seg[0]:
                birth_place_flag = birth_place_flags[i]
                break

        assert birth_place_flag != ''
        has_flag = False
        for i in range(len(self.seg[0])):
            if self.pos[0][i] == 'nh' and self.seg[0][i] not in self.names:
                self.names.append(self.seg[0][i])
            if self.seg[0][i] == '男' or self.seg[0][i] == '女':
                self.gender.append(self.seg[0][i])
            if self.seg[0][i] in self.eth_dict and self.seg[0][i] not in self.ethnicity:
                self.ethnicity.append(self.seg[0][i])
            if birth_place_flag == self.seg[0][i]:
                index = i + 1
                has_flag = True
                birth_place = ''
                while not contain_stop_signs(stop_sign, self.seg[0][index]):
                    birth_place += self.seg[0][index]
                    index += 1
                self.birthplace.append(birth_place)
            if not has_flag and self.pos[0][i] == 'ns' and self.seg[0][i] not in self.birthplace and not self.seg[0][i].endswith('法院'):
                self.birthplace.append(self.seg[0][i])
        self.ltp.add_words(self.names)
        self.gender = list(set(self.gender))

    def extract_principal_crime_info(self, sentences):
        jieba.load_userdict('dict/jieba/courts.txt')
        jieba.load_userdict('dict/jieba/procuratorates.txt')
        jieba.load_userdict('dict/jieba/accusations.txt')
        jieba.analyse.set_idf_path('dict/jieba/idf-dict.txt')
        key = jieba.analyse.extract_tags(sentences, topK=10, withWeight=False, allowPOS=('nz', 'nt'))
        for i in range(len(key)):
            if key[i].endswith('罪'):
                self.causes.append(key[i])
            elif key[i].endswith('法院') and len(key[i]) > 6 and '\n' not in key[i] and '。' not in key[i]:
                self.courts.append(key[i])

    def scan_rest(self, sentence):
        self.seg_and_pos(sentence)
        for i in range(len(self.seg[0])):
            if self.seg[0][i] not in self.names and self.pos[0][i] == 'nh' and not contain_stop_signs(['，', '。', '\n', '（', '）'], self.seg[0][i]) and len(self.seg[0][i]) < 4:
                self.names.append(self.seg[0][i])
            elif self.seg[0][i].endswith('法院') and self.seg[0][i] not in self.courts and not contain_stop_signs(['，', '。', '\n', '（', '）'], self.seg[0][i]):
                self.courts.append(self.seg[0][i])

    """for test usage"""
    def print_out(self):
        print('name: ', self.names)
        print('birthplace: ', self.birthplace)
        print('gender: ', self.gender)
        print('ethnicity: ', self.ethnicity)
        print('courts: ', self.courts)
        print('causes: ', self.causes)
