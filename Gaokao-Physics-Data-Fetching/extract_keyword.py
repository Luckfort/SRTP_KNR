import os
import docx
import TF_IWF
from knowledge_filter import *
import pickle
import json
import sys

threshold=10
def create_tfiwf():
    all_text=''
    for root,dirs,files in os.walk(r".\\Doc_write"):
        for file in files:
            if (file.find('.txt')==-1):
                continue
            txt_file=os.path.join(root,file)
            with open(txt_file,'r',encoding='utf-8') as f1:
                text_set=f1.readlines()
                f1.close()
            text_set=''.join(text_set)
            all_text=all_text+text_set
    all_text=knowledge_filter(all_text)
    tfiwf=TF_IWF.TF_IWF(all_text,threshold)
    pickle.dump(tfiwf,open("./model/tfiwf.pkl","wb"))
    sys.exit()
#create_tfiwf()
tfiwf=pickle.load(open("./model/tfiwf.pkl","rb"))
cfg={}
for root,dirs,files in os.walk(r".\\Doc_write"):
    for file in files:
        if (file.find('.txt')==-1):
            continue
        node_name=file.replace('.txt','')
        txt_file=os.path.join(root,file)
        with open(txt_file,'r',encoding='utf-8') as f1:
            text_set=f1.readlines()
            f1.close()
        text_set=''.join(text_set)
        text_set=knowledge_filter(text_set)
        result = tfiwf.out_result(text_set)
        if(len(result)==threshold):
            cfg[node_name]=result

js=json.dumps(cfg)
with open('cfg.txt','w',encoding='utf-8') as f:
    f.write(js)
    f.close()
print(cfg)
