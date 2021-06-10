from paddlenlp.transformers import WordpieceTokenizer, PretrainedTokenizer
from mover.model import Model

UNK_TOKEN = '[UNK]'
SEP_TOKEN = 'O'
SUB_TOKEN = '##'


class Summarizer:
    wt = None
    vocab = None

    @classmethod
    def init(cls):
        from mover.config import Config
        cls.vocab = PretrainedTokenizer.load_vocabulary(
            Config.VOCAB_DIR,
            UNK_TOKEN
        )
        cls.wt = WordpieceTokenizer(cls.vocab, UNK_TOKEN)

    @classmethod
    def summarize(cls, msgs):
        if isinstance(msgs, str):
            msgs = [msgs]

        from mover.model import Cutter
        msgs_by_cut = [' '.join(Cutter.cut(msg)).lower() for msg in msgs]
        predicts = Model.predict(msgs)
        return [cls.postprocess(msg, predict) for msg, predict in zip(msgs_by_cut, predicts)]

    @classmethod
    def postprocess(cls, msg: str, predict: list):
        predict = predict[1:predict.index(SEP_TOKEN, 1)]
        tokens = cls.wt.tokenize(msg)

        s, summary = '', []
        for t, p in zip(tokens + ['end'], predict + ['0']):
            if not t.startswith(SUB_TOKEN):
                if s.startswith(SEP_TOKEN) and s[1:] not in summary:
                    summary.append(s[1:])
                s = f'{SEP_TOKEN}{t}' if str(p) == '1' else ''
            else:
                s += t.strip(SUB_TOKEN)
        return summary
