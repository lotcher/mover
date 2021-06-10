import argparse
import json

from .config import Config

_MODEL_FILE, _CONFIG_FILE = ('model_dir', 'config')


class CLI:
    @classmethod
    def parse(cls):
        parser = argparse.ArgumentParser(description='Hill命令行参数')
        parser.add_argument(
            '--config', '-f', dest=_CONFIG_FILE, required=True,
            help='默认加载的配置文件路径，格式为json'
        )
        parser.add_argument(
            '--model-file', '-m', dest=_MODEL_FILE, required=False,
            help='默认加载的模型参数文件路径'
        )

        return parser.parse_args()

    @classmethod
    def init(cls):
        args = CLI.parse()
        configs = {
            # 命令行参数的优先级高于配置文件
            **json.loads(open(getattr(args, _CONFIG_FILE)).read()),
            **{k: getattr(args, k) for k in [_MODEL_FILE] if getattr(args, k)},
        }

        Config.init(**configs)
