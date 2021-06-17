from functools import reduce
from operator import add

from mover.config import TrainerConfig
from .summarizer import Summarizer
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


def evaluate():
    with open(TrainerConfig.EVAL_DATA_DIR) as f:
        eval_data = f.readlines()
    msgs, labels = zip(*[line.strip().split('\t') for line in eval_data])
    labels = list(map(int, reduce(add, [label.split(' ') for label in labels])))
    predicts = [[int(token in predict) for token in msg.lower().split(' ')]
                for predict, msg in zip(Summarizer.summarize(msgs), msgs)]
    predicts = reduce(add, predicts)
    print(
        f'f1_score: {f1_score(labels, predicts)}, acc: {accuracy_score(labels, predicts)}\n'
        f'precision: {precision_score(labels, predicts)}, recall_score: {recall_score(labels, predicts)}'
    )
