import paddlehub as hub
import paddle
from paddlehub.datasets.base_nlp_dataset import SeqLabelingDataset
from os.path import dirname, basename


def train():
    from mover.model import Model
    from mover.config import TrainerConfig
    train_data = SeqLabelingDataset(
        base_path=dirname(TrainerConfig.TRAIN_DATA_DIR), data_file=basename(TrainerConfig.TRAIN_DATA_DIR),
        tokenizer=Model.get_tokenizer(), label_list=Model.labels, mode='train', split_char=' '
    )

    eval_data = SeqLabelingDataset(
        base_path=dirname(TrainerConfig.EVAL_DATA_DIR), data_file=basename(TrainerConfig.EVAL_DATA_DIR),
        tokenizer=Model.get_tokenizer(), label_list=Model.labels, mode='dev', split_char=' '
    )

    optimizer = paddle.optimizer.Adam(learning_rate=5e-5, parameters=Model.parameters())
    trainer = hub.Trainer(Model.model, optimizer, checkpoint_dir=TrainerConfig.CHECK_DIR, use_gpu=TrainerConfig.USE_GPU)

    trainer.train(train_data, epochs=TrainerConfig.EPOCHS, batch_size=TrainerConfig.BATCH_SIZE, eval_dataset=eval_data)

    trainer.save_model(TrainerConfig.CHECK_DIR)
