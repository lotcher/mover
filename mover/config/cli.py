import argparse
import json

from .config import Config
from .trainer_config import TrainerConfig

_CONFIG_FILE, _CHECK_DIR, _MODE = ('config', 'check_dir', 'mode')


class CLI:
    @classmethod
    def parse(cls):
        parser = argparse.ArgumentParser(description='Hill命令行参数')
        parser.add_argument(
            '--config', '-f', dest=_CONFIG_FILE, required=True,
            help='默认加载的配置文件路径，格式为json'
        )
        parser.add_argument(
            '--check_dir', '-c', dest=_CHECK_DIR, required=False,
            help='默认加载的模型参数文件路径'
        )
        parser.add_argument(
            '--mode', '-m', dest=_MODE, required=False,
            help='运行模式', choices=[Config.MODE, TrainerConfig.MODE]
        )

        return parser.parse_args()

    @classmethod
    def init(cls):
        args = CLI.parse()
        configs = {
            # 命令行参数的优先级高于配置文件
            **json.loads(open(getattr(args, _CONFIG_FILE)).read()),
            **{k: getattr(args, k) for k in [_CHECK_DIR, _MODE] if getattr(args, k)},
        }

        Config.init(**configs)
        if getattr(args, _MODE) == TrainerConfig.MODE:
            TrainerConfig.init(**configs)
