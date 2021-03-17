# Chat-robot
运行环境：
python3.7
pytorch 1.1/1.2
Windows/Linux
Anaconda

使用方法：
前提：已安装好python3.7。
#### 1. 安装Anaconda并下载实验需要的python包：jieba/sklearn/nltk/pytorch...（也可在cmd或linux终端中下载python包并运行）
① 进入Anaconda Prompt(anaconda3)终端界面

② 输入命令

 > pip install <python包>

##### 2. 模型训练
① 进入项目文件夹下

② 输入命令

 > python train.py --model model.pkl

③ 训练好的模型保存在.pkl文件中

#### 3. 运行demo
 > python demo.py --model model.pkl --device cuda
