import math
import re

import numpy as np
import jieba

"""
进行文本分词并提取关键词
:param : 文件所有文本（str)，所需提取段落（str),提取几个关键词（int)
:return: [str,str,str]
"""

class TF_IWF:

    def __init__(self, lines ,word_number):
        self.iwf = dict()
        self.median_iwf = 0
        self.__build_iwf(lines)
        self.word_number=word_number
        self.tokenlize(lines)

    def tokenlize(self,sentence):

        fileters = ['！', '“', '#', '$', '%', '&', '\（', '\）', '\*', '\+', '，', '——', '-', '\。', '/', '；', '：', '<', '=',
                    '>',
                    '\？', '@', '\【', '\\', '\】', '^', '_', '`', '\{', '\|', '\}', '~', '\t', '\n', '\x97', '\x96', '”',
                    '“', ',']
        # sentence = sentence.lower() #把大写转化为小写
        sentence = re.sub("<br />", " ",sentence )
        sentence = re.sub("|".join(fileters), " ", sentence)
        result = [i.strip() for i in sentence.split(" ") if len(i) > 0]
        result = "".join(result)
        return jieba.lcut(result)

    def __get_tf(self, strs):
        tf_dict = {}
        line_words = self.tokenlize(strs)
        total_word_line = len(line_words)
        for word in line_words:
            if word not in tf_dict:
                tf_dict[word] = 1
            else:
                tf_dict[word] = tf_dict[word] + 1
        for k, v in tf_dict.items():
            tf_dict[k] = v / total_word_line
        return tf_dict

    def __build_iwf(self, lines):

        for line in lines:
            line_words = self.tokenlize(line)
            for word in line_words:
                if word not in self.iwf:
                    self.iwf[word] = 1
                else:
                    self.iwf[word] = self.iwf[word] + 1
        total_word_lines = len(self.iwf.values())
        values = []
        for k, v in self.iwf.items():
            self.iwf[k] = math.log(total_word_lines / v, 10)
            values.append(math.log(total_word_lines / v, 10))
        self.median_iwf = np.median(values)

    def get_tfiwf(self, strs):
        result = dict()
        tf_dict = self.__get_tf(strs)
        line_words = self.tokenlize(strs)
        for word in line_words:
            if word not in self.iwf.keys():
                result[word] = tf_dict[word] * self.median_iwf
            else:
                result[word] = tf_dict[word] * self.iwf[word]
        return result

    def out_result(self,strs) :
        #result0=list(range(self.word_number))
        result0=[]
        unsort_dict=self.get_tfiwf(strs)
        sort_dict=sorted(unsort_dict.items(), key=lambda d:d[1], reverse = True)
        l=len(sort_dict)
        l=min(l,self.word_number)
        for i in range(l):
            result0.append(sort_dict[i][0])
        return result0

if __name__ == "__main__":
    lines = " 二、磁感线及特点1．磁感线在磁场中画出一些曲线，使曲线上每一点的切线方向都跟这点的磁感应强度的方向一致．2．磁感线的特点(1)磁感线上某点的切线方向就是该点的磁场方向．(2)磁感线的疏密定性地表示磁场的强弱，在磁感线较密的地方磁场较强；在磁感线较疏的地方磁场较弱．(3)磁感线是闭合曲线，没有起点和终点．在磁体外部，从N极指向S极；在磁体内部，由S极指向N极．(4)同一磁场的磁感线不中断、不相交、不相切．(5)磁感线是假想的曲线，客观上不存在．3．电流周围的磁场"

    line = "磁感线是闭合曲线，没有起点和终点．在磁体外部，从N极指向S极；在磁体内部，由S极指向N极"
    tfiwf = TF_IWF(lines,4)
    result = tfiwf.out_result(line)
    print(result)
