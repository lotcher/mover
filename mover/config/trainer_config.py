import os
from .config import Config

TRAIN_MODE = 'train'


class TrainerConfig(Config):
    _must_params = {'TRAIN_DATA_DIR', 'EVAL_DATA_DIR'}
    MODE = TRAIN_MODE

    @classmethod
    def init(cls, **kwargs):
        super().init(**kwargs)
        if not all([os.path.isfile(getattr(cls, file)) for file in cls._must_params]):
            raise ValueError(f'初始化提供的{cls._must_params}不是合法的文件路径')

    TRAIN_DATA_DIR = ''
    EVAL_DATA_DIR = ''
    LEARNING_RATE = 5e-5
    EPOCHS = 1
    BATCH_SIZE = 64
