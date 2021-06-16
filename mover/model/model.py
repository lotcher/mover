import paddlehub as hub

UNK_TOKEN = '[UNK]'
SEP_TOKEN = 'O'
SUB_TOKEN = '##'


class Model:
    labels = ['0', '1', SEP_TOKEN]
    model = None

    @classmethod
    def init(cls):
        from mover.config import Config
        cls.model = hub.Module(
            name=Config.MODEL_NAME,
            task='token-cls',
            label_map={i: label for i, label in enumerate(cls.labels)},
            load_checkpoint=Config.MODEL_DIR
        )

    @classmethod
    def predict(cls, msgs: list):
        from mover.config import Config
        return [
            p[1:p.index(SEP_TOKEN, 1)]
            for p in cls.model.predict([[msg] for msg in msgs], use_gpu=Config.USE_GPU)
        ]

    @classmethod
    def get_tokenizer(cls):
        return cls.model.get_tokenizer()

    @classmethod
    def parameters(cls):
        return cls.model.parameters()
