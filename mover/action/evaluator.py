from functools import reduce
from operator import add
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

from mover.config import TrainerConfig
from .summarizer import Summarizer
from mover.tools import Logger


def evaluate():
    with open(TrainerConfig.EVAL_DATA_DIR) as f:
        eval_data = f.readlines()
    msgs, labels = zip(*[line.strip().split('\t') for line in eval_data])
    labels = list(map(int, reduce(add, [label.split(' ') for label in labels])))
    predicts = [[int(token in predict) for token in msg.lower().split(' ')]
                for predict, msg in zip(Summarizer.summarize(msgs), msgs)]
    predicts = reduce(add, predicts)
    Logger.info(
        f'f1_score: {f1_score(labels, predicts):.4f}, acc: {accuracy_score(labels, predicts):.4f}, '
        f'precision: {precision_score(labels, predicts):.4f}, recall: {recall_score(labels, predicts):.4f}'
    )
