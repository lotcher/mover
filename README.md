# mover
基于预训练模型的抽取式告警摘要框架，通过有监督模型预测结果与无监督日志模版提取方法结合优化摘要结果。

包含便捷的训练、评估及便捷的服务部署。模型支持增量学习，支持使用GPU或者CPU训练或预测。

<img src="http://lbj.wiki/static/images/6ce9a902-cfe1-11eb-9928-00163e30ead3.png" alt="image-20210618110105425" style="zoom: 25%;" />

## 使用说明

> python版本>=3.7
>
> 安装深度学习框架时根据情况安装对应GPU（和CUDA版本对应）或者CPU版本

1. 进入项目根目录，此时目录应该如下所示

   mover<br>
   ├── conf.d<br>
   ├── mover<br>
   ├── static<br>
   ├── README.md<br>
   └── **requirements.txt**<br>

2. 执行以下命令安装依赖

   ```shell
   pip3 install -r install requirements.txt
   ```

3. 进入代码目录**「cd mover」**，目录如下

   mover<br>
   ├── action<br>
   ├── config<br>
   ├── model<br>
   ├── tools<br>
   ├── init.py<br>
   └── **main.py**<br>

4. 按照需求关联指定的配置文件后执行模式**「python3 main.py --help」**

   > usage: main.py [-h] --config CONFIG [--check_dir CHECK_DIR]
   >                [--mode {service,train,eval}]
   >
   > Mover命令行参数
   >
   > optional arguments:
   >   -h, --help            show this help message and exit
   > 
   >   --config CONFIG, -f CONFIG      默认加载的配置文件路径，格式为json
   > 
   >   --check_dir CHECK_DIR, -c CHECK_DIR      默认加载的模型参数文件路径
   > 
   >   --mode {service,train,eval}, -m {service,train,eval}    运行模式



## 运行模式

### service（web服务）

* 强制参数：check_dir

* 参考配置

  ```json
  {
    "model_name": "ernie",
    "check_dir": "/root/bowaer/logtree/bert-train/model/mark_ernie_seg/",
    "use_gpu": true
  }
  ```

* 运行示例

  ```shell
  python3 main.py -f ../conf.d/ernie.json -m service
  ```

### train（模型训练）

* 强制参数：train_data_dir, eval_data_dir

* 参考配置

  ```json
  {
    "model_name": "ernie",
    "use_gpu": true,
    "train_data_dir": "/root/bowaer/logtree/output/train-ceb-2020_mark_seg.data",
    "eval_data_dir": "/root/bowaer/logtree/output/eval-ceb-2020_mark.data"
  }
  ```

* 运行示例

  ```shell
  python3 main.py -f ../conf.d/ernie.json -m train
  ```

### eval（评估模型）

* 强制参数：train_data_dir, eval_data_dir

* 参考配置

  ```json
  {
    "model_name": "ernie",
    "use_gpu": true,
    "train_data_dir": "/root/bowaer/logtree/output/train-ceb-2020_mark_seg.data",
    "eval_data_dir": "/root/bowaer/logtree/output/eval-ceb-2020_mark.data"
  }
  ```

* 运行示例

  ```shell
  python3 main.py -f ../conf.d/ernie.json -m eval
  ```



## 参数配置

### 公共参数

```python
# 模型名称
MODEL_NAME = 'ernie'

# 模型加载和保存路径，默认使用原始模型安装路径
CHECK_DIR = ''

# 模型参数路径
MODEL_DIR = ''

# 是否使用GPU
USE_GPU = False

# 分词词典
WORD_DIR = f'{BASE_DIR}/../static/words.txt'

# 预训练模型字典
VOCAB_DIR = f'{BASE_DIR}/../static/vocab.txt'

# 停用词文件
STOP_WORD_DIR = f'{BASE_DIR}/../static/stop_words.txt'
```

### 训练参数

```python
# 训练数据路径
TRAIN_DATA_DIR = ''

# 验证集数据路径
EVAL_DATA_DIR = ''

# 学习率
LEARNING_RATE = 5e-5

# epoch数量
EPOCHS = 1

# 每批训练数据量
BATCH_SIZE = 64
```
