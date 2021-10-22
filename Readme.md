## 这个项目供SRTP学习使用。
初始模型出自：https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch

## 如何运行
### Gaokao-Physics-Classification
初始模型。
数据集已经放进了Phycics文件夹里。
每次运行，原本在powershell终端运行python run.py --model bert
鉴于现在已经将模型强制修改为只用bert模型，所以直接运行也可以。
<img src = "img\1.png" width = 100%>
如果改为原版，只用将注释的那行取消掉注释，model_name='bert'删除。
utils和构建所有爬虫文本的词向量有关。
train_eval，顾名思义，训练和评估。

## Gaokao-Physics-Data-Fetching
数据集的获取。可能程序尚未完全上传。
① Scrapy_bd.py 顾名思义，百度网络爬虫。
② extract_keyword.py 对专业文档建立一个关键字的TF-IWF模型，并生成一个针对每个知识点的关键字序列的字典。
③ Tagging 给各个数据点贴标签。
④ knowledge_filter 把杂的字符过滤掉。
⑤ Path_Walk 解析文本
⑥ BGM Sort the data in valid(dev)/test/train set
