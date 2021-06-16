from .config import Config


class TrainerConfig(Config):
    _must_params = {'TRAIN_DATA_DIR', 'EVAL_DATA_DIR'}

    TRAIN_DATA_DIR = ''
    EVAL_DATA_DIR = ''
