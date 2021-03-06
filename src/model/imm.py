
class IMM(object):
    def __init__(self,dic_path):
        self.dictionary = set()
        self.maximum = 0
        #读取词典
        with open(dic_path,'r',encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)

    def cut(self,text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum,0,-1):
                if index - size < 0:
                    continue
                piece = text[(index-size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]

class MM(object):
    def __init__(self,dic_path):
        self.dictionary = set()
        self.maximum = 0
        #读取词典
        with open(dic_path,'r',encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line)>self.maximum:
                    self.maximum = len(line)

    def cut(self,text):
        index = len(text)
        result = []
        i = 0
        while i<index:
            word = None
            for size in range(self.maximum,0,-1):
                if (index-i)<size:
                    continue
                piece = text[i:(i+size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    i += size
                    break
            if word is None:
                i += 1
        return result