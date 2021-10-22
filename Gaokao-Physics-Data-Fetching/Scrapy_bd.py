# 此爬虫框架出自https://github.com/Alex-gousheng/BaiduWenkuSpider
#
#
import requests
import re
import json
import os

# WkInfo.docType = {
#             '1': 'doc',
#             '2': 'xls',
#             '3': 'ppt',
#             '4': 'docx',
#             '5': 'xlsx',
#             '6': 'pptx',
#             '7': 'pdf',
#             '8': 'txt',

#         };

url=""
headers={"User-Agent":"ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45"}
def Test_():
    matched=re.findall(r'https://wenku.baidu.com/view/.*.html.*',url)
    
    if(matched.__len__()==0):
        return 0
    else:
        return 1
def getID(url):
    if(Test_()==0):
        print("此链接不是有效的百度文库地址链接！")
        return
    else:
        doc_id1=re.findall(r'view/.*.html',url)
        doc_id2=re.sub(r'view/','',doc_id1[0])
        doc_id=re.sub(r'.html','',doc_id2)
        return doc_id
def WkInfo(docID):
    doc_id=docID
    url_1="https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id="
    url_=url_1+doc_id
    url=requests.get(url_,headers)
    return url.text
    

def Doc(texts,url):

    img_lists=[]
    zoom_=re.findall(r'zoom":".*?"',texts)
    zoom=""
    
    for imgs in range(zoom_.__len__()):
        zoom=re.sub(r'zoom":"','',zoom_[imgs])
        zoom=re.sub(r'"','',zoom)
        img_lists.append(zoom)
        
    
    md5sum_1=re.findall(r'"&md5sum=.*?"',texts)
    md5sum_2=re.sub(r'"',"",md5sum_1[0])
    md5sum_=re.split(r'&',md5sum_2)
    rsign_1=re.findall(r'rsign":".*?"',texts)
    rsign_2=re.sub(r'"','',rsign_1[0])
    rsign=re.sub(r':','=',rsign_2)
    pn_1=re.findall(r'totalPageNum":".*?"',texts)
    pn_2=re.sub(r'totalPageNum":"','',pn_1[0])
    pn=re.sub(r'"','',pn_2)
    doc_title_1=re.findall(r'docTitle":".*?"',texts)
    doc_title_2=re.sub(r'"','',doc_title_1[0])
    doc_title=re.sub(r'docTitle:','',doc_title_2)
    doc_title=doc_title.encode('utf-8').decode('unicode_escape')
    page_num=re.findall(r'freepagenum":.*?,',texts)
    page_num=re.sub(r'freepagenum":','',page_num[0])
    page_num=re.sub(r',','',page_num)
    page_num=page_num.strip()
    if(page_num=="null"):
        print('(此文档为普通文档，可以全部爬取！)')
        final_url="https://wkretype.bdimg.com/retype/text/"+getID(url)+"?"+md5sum_[1]+"&"+md5sum_[2]+"&callback=cb"+"&callback=cb"+"&pn=1"+"&rn="+pn+"&type=txt"+"&"+rsign
    else:
        print('(此文档为vip文档，只能获取部分数据！)')
        final_url="https://wkretype.bdimg.com/retype/text/"+getID(url)+"?"+md5sum_[1]+"&"+md5sum_[2]+"&callback=cb"+"&callback=cb"+"&pn=1"+"&rn="+page_num+"&type=txt"+"&"+rsign
    if(len(zoom)>0):
        img_nums=0
        for n in range(img_lists.__len__()):
            img_nums+=1
            img_url="https://wkretype.bdimg.com/retype/zoom/"+getID(url)+"?"+"o=png_6_0_0_0_0_0_0"+"&type=pic&md5sum="+"&"+md5sum_[1]+"&"+md5sum_[2]+img_lists[n]
            img_res=requests.get(img_url,headers).content
            
            if(not os.path.isdir('IMG')):
                os.mkdir('IMG')
            if(not os.path.isdir('IMG\\'+doc_title+getID(url))):
                os.mkdir('IMG\\'+doc_title+getID(url))
            with open("IMG\\"+doc_title+getID(url)+"\\"+'('+str(img_nums)+')'+'.png','wb') as m:
                for nums in range(img_lists.__len__()):
                    m.write(img_res)
    res_=requests.get(final_url,headers)
    # 通过json来分割数据：
    res=res_.text
    datas_=re.findall('\[.*\]',res,re.DOTALL) 
    datas=json.loads(datas_[0])
    real_page=datas[0]['tn']

    if(not page_num=="null"):
        real_page=page_num
    json_lists_=[]
    if(not os.path.isdir('TXT')):
            os.mkdir('TXT')
    if(not os.path.isdir('TXT\\'+doc_title+getID(url))):
            os.mkdir('TXT\\'+doc_title+getID(url))
    filename="TXT\\"+doc_title+getID(url)+"\\"+doc_title+getID(url)+".txt"
    try:
        for nums in range(int(real_page)):
            json_lists_.append(datas[nums]['parags'][0]['c'])
    except IndexError:
        print('网页的tn存在问题,已尽量爬取数据')

    finally:
        try:
            with open(filename,'w',encoding="utf-8") as f:
                for strs in range(int(real_page)):
                    f.write(json_lists_[strs])
        except IndexError:
            f.close()


    print('获取成功！\n')
    print('文字信息已生成在TXT文件夹中，图片信息已生成于IMG文件夹中。\n')
    print('\n')
    print('\n')


    # 通过正则表达式来分割数据：

    # res=res_.content.decode('unicode_escape')#
    # str_c=re.findall(r'c":".*?"',res,re.DOTALL)
    # for c in range(str_c.__len__()):
    #     str_c[c]=re.sub(r'"',"",str_c[c])
    #     str_c[c]=re.sub(r':',"",str_c[c])
    #     str_c[c]=re.sub(r'c',"",str_c[c])
    #     print(str_c[c])

    
def PPT(texts,url):
    pn_1=re.findall(r'totalPageNum":".*?"',texts)
    pn_2=re.sub(r'totalPageNum":"','',pn_1[0])
    pn=re.sub(r'"','',pn_2)
    doc_title_1=re.findall(r'docTitle":".*?"',texts)
    doc_title_2=re.sub(r'"','',doc_title_1[0])
    doc_title=re.sub(r'docTitle:','',doc_title_2)
    doc_title=doc_title.encode('utf-8').decode('unicode_escape')

    url_="https://wenku.baidu.com/browse/getbcsurl?doc_id="+getID(url)+"&pn=1&rn=99999&type=ppt&callback=jQuery"
    res=requests.get(url_,headers)
    re_data=re.findall('\{.*\}',res.text)
    free_data=json.loads(re_data[0])
    free=free_data['free']
    
    datas=free_data
    
    json_lists=[]
    img_nums=0
    for nums in range(int(free)):
        json_lists.append(datas['list'][nums]['zoom'])
        img_res=requests.get(json_lists[nums],headers).content
        img_nums+=1
        if(not os.path.isdir('IMG')):
            os.mkdir('IMG')
        if(not os.path.isdir('IMG\\'+doc_title+getID(url))):
            os.mkdir('IMG\\'+doc_title+getID(url))

        with open("IMG\\"+doc_title+getID(url)+"\\"+'('+str(img_nums)+')'+'.jpg','wb') as m:
            for nums in range(int(free)):
                m.write(img_res)


    print('获取成功！\n')
    print('(温馨提示：如果获取的图片数量不够，说明此文档属于vip文档，请检查~)')
    print('文字信息已生成在TXT文件夹中，图片信息已生成于IMG文件夹中。\n')
    print('\n')
    print('\n')
def TYPE(docID,urls):
    if(Test_()==0):
        return
    print('正在生成文件。。。。')
    url=WkInfo(docID)
    strs_1=re.findall(r'docType":".?',url)
    doc_type=re.sub('docType":"',"",strs_1[0])
    
    if(int(doc_type)==1 or int(doc_type)==8 or int(doc_type)==4 or int(doc_type)==7 or int(doc_type)==2 or int(doc_type)==5):
        Doc(url,urls)

    elif(int(doc_type)==3 or int(doc_type)==6):
        PPT(url,urls)
    else:
        print("TYPE:Error（文档类型错误！）")

    return doc_type


###################################################
#执行总入口：
###################################################


url=input('请输入想要获取数据的地址(例如：https://wenku.baidu.com/view/d69ca642fbd6195f312b3169a45177232f60e498.html)：\n')

TYPE(getID(url),url)

#input("\n请按任意键来结束程序~")