from ltp import LTP


class Extracter:
    def __init__(self):
        self.ltp = LTP()
        self.ltp.init_dict('dict.txt')
        self.ltp.init_dict('dict2.txt')
        self.ltp.init_dict('ultimate_accusations_dict.txt')
        self.eth_dict = {}
        self.init_ethnicity_dict()
        self.seg = None
        self.hidden = None
        self.pos = None
        self.srl = None
        self.names = []
        self.birthplace = []
        self.ethnicity = []
        self.gender = []
        self.causes = []
        self.courts_concerned = []

    def init_ethnicity_dict(self):
        with open('ethnicity.txt', encoding='utf-8') as file:
            for line in file:
                self.eth_dict[line.replace('\n', '')] = True

    def seg_sentences(self, sentences):
        self.seg, self.hidden = self.ltp.seg(sentences)

    def seg_and_pos(self, sentences):
        self.seg_sentences(sentences)
        self.pos = self.ltp.pos(self.hidden)

    def seg_pos_srl(self, sentences):
        self.seg_and_pos(sentences)
        self.srl = self.ltp.srl(self.hidden, keep_empty=False)

    def extract_criminal_basic_info(self, sentences):
        self.seg_and_pos(sentences)
        for i in range(len(self.seg[0])):
            if self.pos[0][i] == 'nh':
                self.names.append(self.seg[0][i])
            if self.seg[0][i] == '男' or self.seg[0][i] == '女':
                self.gender.append(self.seg[0][i])
            if self.pos[0][i] == 'ns':
                self.birthplace.append(self.seg[0][i])
            if self.seg[0][i] in self.eth_dict:
                self.ethnicity.append(self.seg[0][i])
        self.ltp.add_words(self.names)

    def extract_principal_crime_info(self, sentences):
        self.seg_pos_srl(sentences)
        for i in range(len(self.seg[0])):
            if (self.pos[0][i] == 'ns' or self.pos[0][i] == 'ni') and ('法院' in self.seg[0][i]):
                self.courts_concerned.append(self.seg[0][i])
        for item in self.srl[0]:
            index, args = item
            if self.seg[0][index] == '犯':
                cur = index + 1
                while cur < len(self.seg[0]):
                    if '罪' in self.seg[0][cur]:
                        self.causes.append(self.seg[0][cur])
                    cur += 1
        self.causes = set(self.causes)

    def scan_rest_sentences(self, sentences):
        self.seg_and_pos(sentences)
        for i in range(len(self.seg)):
            for j in range(len(self.seg[i])):
                if (self.pos[i][j] == 'ns' or self.pos[i][j] == 'ni') and '法院' in self.seg[i][j]:
                    self.courts_concerned.append(self.seg[i][j])

    """for test usage"""
    def print_out(self):
        print('name: ', self.names)
        print('birthplace: ', self.birthplace)
        print('gender: ', self.gender)
        print('ethnicity: ', self.ethnicity)
        print('courts: ', self.courts_concerned)
        print('causes: ', self.causes)

