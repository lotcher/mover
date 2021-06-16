from .config import Config

TRAIN_MODE = 'train'


class TrainerConfig(Config):
    _must_params = {'TRAIN_DATA_DIR', 'EVAL_DATA_DIR'}
    MODE = TRAIN_MODE

    TRAIN_DATA_DIR = ''
    EVAL_DATA_DIR = ''
    LEARNING_RATE = 5e-5
    EPOCHS = 1
    BATCH_SIZE = 64
