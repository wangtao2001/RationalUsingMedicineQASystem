import requests

headers = {"user-agent":"Mozilla\5.0"}

with open(r".\图片地址.csv", "r",encoding='utf-8') as url_f:
    url_list = url_f.readlines()
url_list = [url[:-1] for url in url_list]  # 去掉\n

with open(r".\药物名称.csv","r",encoding='utf-8') as drug_f:
    name_list = drug_f.readlines()
name_list = [name.split("(")[0].strip() for name in name_list]

for index in range(len(url_list)):
    r = requests.get(url_list[index],headers=headers,timeout=15)
    f = open(rf".\{name_list[index]}.jpg","wb")
    f.write(r.content)
    f.close()
    print(index)
