import requests
import csv
from bs4 import BeautifulSoup
from tqdm import trange, notebook


num = 0
intPage = 1

f = open(r'output.csv', 'w', newline='')
w = csv.writer(f)
w.writerow(['song_num', 'song_title', 'song_singer', 'song_lyricist', 'song_writer'])  # 헤더

for num in notebook.tqdm(range(10)):
    while True:
        url = 'http://www.tjmedia.co.kr/tjsong/song_search_list.asp?strType=16&strText=%d&strCond=0&searchOrderItem' \
              '=&searchOrderType=&strSize05=100&intPage=%d' % (
                  num, intPage)

        response = requests.get(url)
        page = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser",from_encoding="iso-8859-1")
            list_song_num = soup.select('#BoardType1 > table > tbody > tr:nth-child(n+1) > td:nth-child(1)')
            list_song_title = soup.select('#BoardType1 > table > tbody > tr:nth-child(n+1) > td:nth-child(2)')
            list_song_singer = soup.select('#BoardType1 > table > tbody > tr:nth-child(n+1) > td:nth-child(3)')
            list_song_lyricist = soup.select('#BoardType1 > table > tbody > tr:nth-child(n+1) > td:nth-child(4)')
            list_song_writer = soup.select('#BoardType1 > table > tbody > tr:nth-child(n+1) > td:nth-child(5)')

            size = len(list_song_num)
            if size == 1:
                break
            for i in notebook.tqdm(range(size)):
                d = [
                    list_song_num[i].get_text(),
                    list_song_title[i].get_text(),
                    list_song_singer[i].get_text(),
                    list_song_lyricist[i].get_text(),
                    list_song_writer[i].get_text()
                ]
                page.append(d)

                w.writerow(d)

            intPage += 1pip install tqdm
            print(intPage)
        else:
            print(response.status_code)
        
    print(num + 1, "/", 10)
f.close()
