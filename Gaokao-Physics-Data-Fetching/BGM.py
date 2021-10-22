import json
import os
import random
import numpy as np
import sys
# category={}
# cate_num={}
# cnt=0
# for root,dirs,files in os.walk(r".\\New_Dataset_5"):
#     for file in files:
#         cnt+=1
#         txt_file=os.path.join(root,file)
#         with open(txt_file,'r',encoding='utf-8') as f1:
#             text_set=f1.readlines()
#             f1.close()
#         if(text_set[1] not in category.keys()):
#             cate_num[text_set[1]]=1
#             category[text_set[1]]=[]
#             category[text_set[1]].append(txt_file)
#         else:
#             cate_num[text_set[1]]+=1
#             category[text_set[1]].append(txt_file)
#         if(cnt%1000==0):
#             print(cnt)
# print(cate_num)
# js=json.dumps(cate_num)
# with open('cate_num.txt','w',encoding='utf-8') as f:
#     f.write(js)
#     f.close()
# with open('cate_num.txt','r',encoding='utf-8') as f:
#     js=f.read()
#     cate_num=json.loads(js)
#     f.close()
# js=json.dumps(category)
# with open('category.txt','w',encoding='utf-8') as f:
#     f.write(js)
#     f.close()
# with open('category.txt','r',encoding='utf-8') as f:
#     js=f.read()
#     category=json.loads(js)
#     f.close()
# b=np.empty(shape=(1,120402))
# valid=[]
# test=[]
# train=[]
# for k in category.keys():
#     tot_num=cate_num[k]
#     for i in range(tot_num):
#         st=category[k][i]
#         temp=random.randint(0,11)
#         if(temp==0):
#             valid.append(st)
#         elif (temp==1):
#             test.append(st)
#         else:
#             train.append(st)
# with open('valid.txt','w',encoding='utf-8') as f:
#     for line in valid:
#         f.write(line+'\n')
#     f.close()
# with open('test.txt','w',encoding='utf-8') as f:
#     for line in test:
#         f.write(line+'\n')
#     f.close()
# with open('train.txt','w',encoding='utf-8') as f:
#     for line in train:
#         f.write(line+'\n')
#     f.close()
# sys.exit()
with open('valid.txt','r',encoding='utf-8') as f:
    valid=f.readlines()
    f.close()
with open('test.txt','r',encoding='utf-8') as f:
    test=f.readlines()
    f.close()
with open('train.txt','r',encoding='utf-8') as f:
    train=f.readlines()
    f.close()
old_path='New_Dataset_5'
valid_path='D\\valid'
l=len(valid)
for i in range(l):
    file=valid[i]
    file=file.replace('\\\\','\\')
    file=file.replace('\n','')
    with open(file,'r',encoding='utf-8') as f:
        content=f.read()
        f.close()
    file=file.replace(old_path,valid_path)
    with open(file,'w',encoding='utf-8') as f:
        f.write(content)
        f.close()
test_path='D\\test'
l=len(test)
for i in range(l):
    file=test[i]
    file=file.replace('\\\\','\\')
    file=file.replace('\n','')
    with open(file,'r',encoding='utf-8') as f:
        content=f.read()
        f.close()
    file=file.replace(old_path,test_path)
    with open(file,'w',encoding='utf-8') as f:
        f.write(content)
        f.close()
train_path='D\\train'
l=len(train)
for i in range(l):
    file=train[i]
    file=file.replace('\\\\','\\')
    file=file.replace('\n','')
    with open(file,'r',encoding='utf-8') as f:
        content=f.read()
        f.close()
    file=file.replace(old_path,train_path)
    with open(file,'w',encoding='utf-8') as f:
        f.write(content)
        f.close()
