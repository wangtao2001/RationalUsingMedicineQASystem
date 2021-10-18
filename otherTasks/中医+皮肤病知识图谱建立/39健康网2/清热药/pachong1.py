# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 22:22:05 2021

@author: 宋小兰
"""
import requests
from bs4 import BeautifulSoup
import bs4


headers = {'user-agent':'Chrome/6.0'}

url_list=[]
start_url='http://ypk.39.net/tcm/875/'
for i in range(1,88):
    url=start_url+str(i)+'.shtml'
    r=requests.get(url,timeout=30,headers=headers,verify=False)
    soup=BeautifulSoup(r.content,'html.parser')
    ul=soup.find('ul',attrs={'class':'medicine-drug-list'})
    for li in ul:
        if isinstance(li,bs4.element.Tag):
            '''
            p_all=li('p')
            for p in p_all[0:1]:
                for a in p:
                    if isinstance(a,bs4.element.Tag):
                        for img in a:
                            if isinstance(img,bs4.element.Tag):
                         
                                img_url=img.get('src')
                                with open('活血化瘀药图片地址.csv','a',encoding='utf-8') as f:
                                    f.write(str(img_url)+'\n')
                                f.close()'''

            for div in li:
                if isinstance(div,bs4.element.Tag):
                    p_all=div('p')
                    for p in p_all[0:1]:
                        for a in p:
                            if isinstance(a,bs4.element.Tag):
                                '''
                                name2=a.string
                                print(name2)#药物名称及异名
                                with open("活血化瘀药药物名称.csv","a",encoding="utf-8") as f:
                                    f.write(str(name2)+'\n')
                                f.close()'''
                                
                                drug_url=a.get('href')
                                url_list.append(drug_url)
druguse_url_list=[]
for j in url_list:
    infoDict1={}
    infoDict= {}
    r1=requests.get(j,timeout=30,headers=headers,verify=False)
    soup1=BeautifulSoup(r1.content,'html.parser')
       
    #基本属性的爬取
    
    druginfo=soup1.find('div',attrs={'class':'main-box'})
    if isinstance(druginfo,bs4.element.Tag):
        p_all=druginfo('p')
        for p in p_all[0:1]:
            jieshao=p.string
            print(jieshao)
            keyList=druginfo.find_all('dt')
            valueList=druginfo.find_all('dd')
            for k in range(len(keyList)):
                key=keyList[k].text
                val=valueList[k].text
                infoDict1[key]=val
            print(str(infoDict1))
            with open('清热药基本属性_end.txt','a',encoding='utf-8') as f:
                f.write(str(infoDict1)+'\n')
            f.close()

    div=soup1.find('div',attrs={'class':'no-padding margin-bottom'})
    if isinstance(div,bs4.element.Tag):
        for ul in div:
            if isinstance(ul,bs4.element.Tag):
                li_all=ul('li')
                #常用药方
                #for li in li_all[1:2]:
                #入药方剂
                for li in li_all[2:3]:
                    for a in li:
                        if isinstance(a,bs4.element.Tag):
                            druguse_url=a.get('href')
                            #print(druguse_url)
                            druguse_url_list.append(druguse_url)
for k in druguse_url_list:
    #print(k)
    r2=requests.get(k,timeout=30,headers=headers,verify=False)
    soup2=BeautifulSoup(r2.content,'html.parser')
   


    
    drug_name=soup2.find('div',attrs={'class':'medicine-overview-r'})
    if isinstance(drug_name,bs4.element.Tag):
        h1_all=drug_name('h1')
        for h1 in h1_all[0:1]:
            if isinstance(h1,bs4.element.Tag):
                name=h1.string
                name1=str(name)+"{"
    with open('清热药药名_方剂.txt','a',encoding='utf-8') as f:
        f.write(str(name1)+'\n')
    f.close()
    
    ul=soup2.find('ul',attrs={'class':'prescription-ul'})
    if isinstance(ul,bs4.element.Tag):
        for li in ul:
            if isinstance(li,bs4.element.Tag):
                p_all=li('p')
                for p in p_all[0:1]:
                    if isinstance(p,bs4.element.Tag):
                        for a in p:
                            if isinstance(a,bs4.element.Tag):
                                yaoji_url=a.get('href')#方剂详细信息的网址
                                r3=requests.get(yaoji_url,timeout=30,headers=headers,verify=False)
                                soup3=BeautifulSoup(r3.content,'html.parser')
                                
                                yaoji_name=soup3.find('div',attrs={'class':'padding-box'})
                                if isinstance(yaoji_name,bs4.element.Tag):
                                    for h1 in yaoji_name:
                                        if isinstance(h1,bs4.element.Tag):
                                            yaoji_name=h1.string
                                            print(yaoji_name)
                                with open('清热药药名_方剂.txt','a',encoding='utf-8') as f:
                                    f.write(str(yaoji_name)+'\n')
                                f.close()
                                
                                druguseinfo=soup3.find('div',attrs={'class':'screen-sort-content summary-box'})
                                keyList=druguseinfo.find_all('dt')
                                valueList=druguseinfo.find_all('dd')
                                for item in range(len(keyList)):
                                    key=keyList[item].text
                                    val=valueList[item].text
                                    infoDict[key]=val
                                print(str(infoDict))
                                with open('清热药入药方剂_end.txt','a',encoding='utf-8') as f:
                                    f.write(str(infoDict)+'\n')
                                f.close()
                                 
                                
   
   
                            
   
            
                