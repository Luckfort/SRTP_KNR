import os
import sys

def create_sample(file_cnt,temp_st):
    filename='./New_Dataset_2/'+str(file_cnt)+'.txt'
    temp_st=temp_st.replace('\n','')
    with open(filename,'w',encoding='utf-8') as f:
        f.write(temp_st)
        f.close()

def Sampling(string_set,total_len):
    global file_cnt
    threshold=100
    cum_len=0
    temp_st=''
    p=0
    for st in string_set:
        l1=len(st)
        cum_len+=l1
        temp_st=temp_st+st+'。'
        total_len-=l1
        if(total_len<threshold):
            p=1
            break
        if(cum_len>=threshold):
            file_cnt+=1
            create_sample(file_cnt,temp_st)
            temp_st=''
            cum_len=0
    if(p or temp_st!=''):
        file_cnt+=1
        create_sample(file_cnt,temp_st)

file_cnt=0
#共128939个Sample
wk=0
for root,dirs,files in os.walk(r"./After_scrapy_data"):
    for file in files:
        file_path=os.path.join(root,file)
        with open(file_path,'r',encoding='utf-8') as f:
            stext=f.readlines()
            f.close()
        stext=''.join(stext)
        total_len=len(stext)
        stext_seperate=stext.split('。')
        
        Sampling(stext_seperate,total_len)