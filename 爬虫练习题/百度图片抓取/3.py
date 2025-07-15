# -*- coding=utf-8 -*-
import requests
import json

api_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9304120940737778532&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1708998004363="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
response = requests.get(api_url, headers=headers)
print(response.text)

img_list = json.loads(response.text)
# 根据索引值作为保存图片文件名
for index, img in enumerate(img_list['data']):
    try:
        img_data = requests.get(img['middleURL'], headers=headers)
    except Exception as e:
        print(e)
        print("抓取失败")
    else:
        # 注意这里wb参数 - 图片数据是字节数据
        with open(f"index_{index}.jpg", "wb") as f:
            # 注意这里是content，而不是text
            f.write(img_data.content)
