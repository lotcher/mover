import os

SERVICE_MODE = 'service'


class Config:
    _must_params = {'CHECK_DIR'}
    MODE = SERVICE_MODE

    @classmethod
    def init(cls, **kwargs):
        kwargs = {k.upper(): v for k, v in kwargs.items()}

        if not cls._must_params.issubset(kwargs.keys()):
            raise ValueError(f'初始化{cls.__name__}必须包含以下参数：{cls._must_params - kwargs.keys()}')

        for k, v in kwargs.items():
            if k in cls.__dict__:
                setattr(cls, k, v)
        cls.MODEL_DIR = f'{cls.CHECK_DIR}/model.pdparams'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_NAME = 'ernie'
    CHECK_DIR = ''
    MODEL_DIR = ''
    USE_GPU = False

    WORD_DIR = f'{BASE_DIR}/../static/words.txt'
    VOCAB_DIR = f'{BASE_DIR}/../static/vocab.txt'
    STOP_WORD_DIR = f'{BASE_DIR}/../static/stop_words.txt'
