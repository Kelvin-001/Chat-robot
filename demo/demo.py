#导入库
from model.model import ChatBot
import torch,warnings,argparse
warnings.filterwarnings("ignore")

#选择哪个模型 ，是否使用gpu
parser = argparse.ArgumentParser()
parser.add_argument('--model', help='The path of your model file.', required=True, type=str)
parser.add_argument('--device', help='Your program running environment, "cpu" or "cuda"', type=str, default='cpu')
args = parser.parse_args()
print(args)
#主程序，打印log，同时对话
if __name__ == "__main__":
    print('Loading the model...')
    chatBot = ChatBot(args.model, device=torch.device(args.device))
    print('Finished...')

    allRandomChoose,showInfo = False, False

    while True:
        inputSeq = input("主人: ")
        if inputSeq=='_crazy_on_':
            allRandomChoose = True
            print('UCAS小天: ','成功开启对话模式...')
        elif inputSeq=='_crazy_off_':
            allRandomChoose = False
            print('UCAS小天: ','成功关闭对话模式...')
        elif inputSeq=='_showInfo_on_':
            showInfo = True
            print('UCAS小天: ','成功开启日志打印...')
        elif inputSeq=='_showInfo_off_':
            showInfo = False
            print('UCAS小天: ','成功关闭日志打印...')
        else:
            outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=allRandomChoose, showInfo=showInfo)
            print('UCAS小天: ',outputSeq)
        print()