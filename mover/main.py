import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mover.model import Cutter, Model
from mover.action import Summarizer, train, evaluate
from mover.tools import Logger
from mover.config import CLI, Config
from mover.config.config import SERVICE_MODE
from mover.config.trainer_config import TRAIN_MODE, EVAL_MODE

from flask import Flask, request

app = Flask(__name__)

BASE_URL = '/api'
MSGS = 'msgs'
PARAMS = {MSGS}


@app.route(f'{BASE_URL}/summarize/', methods=['POST'])
def summarize():
    data = json.loads(request.get_data())
    if not PARAMS.issubset(set(data.keys())):
        return {
            'code': -1,
            'msg': f'参数传递错误，必须包含{"、".join(PARAMS)}'
        }
    return {
        'code': 0,
        'msg': '成功',
        'summaries': Summarizer.summarize(data[MSGS])
    }


def run_service():
    from gevent import monkey
    from gevent.pywsgi import WSGIServer

    monkey.patch_all()
    print('--------------------Mover告警摘要 启动成功--------------------')
    WSGIServer(('0.0.0.0', 10000), app).serve_forever()


if __name__ == '__main__':
    for cls in [Logger, CLI, Cutter, Model, Summarizer]:
        cls.init()

    {
        SERVICE_MODE: run_service,
        TRAIN_MODE: train,
        EVAL_MODE: evaluate
    }[Config.MODE]()
