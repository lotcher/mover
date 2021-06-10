import paddlehub as hub


class Model:
    labels = ['0', '1', 'O']
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
        return cls.model.predict([[msg] for msg in msgs], use_gpu=True)