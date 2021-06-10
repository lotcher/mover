import jieba
import pkuseg
import re
from functools import reduce
from operator import add

PKU = 'pku'
JIEBA = 'jieba'
_CUTTER_NAMES = [PKU, JIEBA]
BLOCK_PATTERN = re.compile(r'[\u4e00-\u9fa5]+|[a-zA-Z]{2,}')
CHINESE_PATTERN = re.compile(r'[\u4e00-\u9fa5]')


class Cutter:
    model = None
    name = PKU
    stop_words = None

    @classmethod
    def init(cls, name=PKU):
        from mover.config import Config
        cls.name = name
        with open(Config.WORD_DIR) as f:
            user_dict = [line.strip() for line in f.readlines()]
        with open(Config.STOP_WORD_DIR) as f:
            cls.stop_words = [line.strip() for line in f.readlines()]

        if name == PKU:
            cls.model = pkuseg.pkuseg(user_dict=user_dict)
        elif name == JIEBA:
            jieba.load_userdict(user_dict)
            cls.model = jieba
        else:
            raise ValueError(f'不支持的cutter名。必须为{_CUTTER_NAMES}中的一个')

    @classmethod
    def cut(cls, msg) -> list:
        funcs = {
            PKU: lambda x: cls.model.cut(x),
            JIEBA: lambda x: cls.model.lcut(x)
        }

        blocks = BLOCK_PATTERN.findall(msg)
        if not blocks:
            return []
        return list(filter(lambda s: s not in cls.stop_words, reduce(add, [
            funcs[cls.name](s) if CHINESE_PATTERN.findall(s) else [s]
            for s in blocks
        ])))
