import time

import requests
from bs4 import BeautifulSoup
import threading

# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36

headers = {
 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

}
for start_num in range(0,250,25) :
    # request = requests.get("https://www.bilibili.com/video/BV1d54y1g7db?p=5&spm_id_from=pageDriver&vd_source=e360046db38dff72e0b07eb9fcb4a21d")
    request = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    # print(request.status_code)    418

    html =request.text
    soup = BeautifulSoup(html,"html.parser")
    all_titles = soup.findAll("span",attrs={"class":"title"})



    for title in all_titles:
        t = title.string
        if "/" not in t:
         print(t)

        # time.sleep(0.1)


exit()

if request.ok:
    print(request.text)
else:
    print("error")
