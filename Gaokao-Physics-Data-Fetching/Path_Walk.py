import os
import docx

def Docx_Txt(Docx_file,txt_file):
    try:
        document=docx.Document(Docx_file)
    except:
        print("获取失败")
        return
    f=open(txt_file,"w",encoding='utf-8')
    title=''
    for paragraph in list(document.paragraphs):
        len1=len(paragraph.runs)
        if len1==0:
            continue
        string_list=[]
        for i in range(0,len1):
            string_list.append(paragraph.runs[i].text)
        string=''.join(string_list)+'\n'
        if(string!='\n'):
            f.write(string)
    f.close()

for root,dirs,files in os.walk(r"./Doc_write"):
    for file in files:
        if (file.find('.txt')!=-1):
            continue
        #获取文件所属目录
        #print(root)
        #获取文件路径
        docx_file=os.path.join(root,file)
        txt_file=docx_file.replace(".docx",".txt")
        #print(docx_file)
        Docx_Txt(docx_file,txt_file)
        with open(txt_file,'r',encoding='utf-8') as f1:
            text_set=f1.readlines()
            f1.close()
