import os.path
import time
import requests
from openpyxl import Workbook
import openpyxl

FILE_PATH = "movie.xlsx"

if not os.path.exists(FILE_PATH):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "phb"
    sheet.append(["序号", "电影名称", "评分", "图片url"])
else:
    wb = openpyxl.load_workbook(FILE_PATH)
    sheet = wb["phb"]


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
}

page = 1
while True:
    print(f"-------------------------- 采集第{page}页 --------------------------")
    params = {
        'type': '30',
        'interval_id': '100:90',
        'action': '',
        'start': f'{(page-1) * 20}',
        'limit': '20',
    }
    response = requests.get('https://movie.douban.com/j/chart/top_list', params=params, headers=headers)

    if not response.json():
        print("数据采集完成")
        break

    for item in response.json():
        data = [item['rank'], item['title'], item['score'], item['cover_url']]
        print(data)
        sheet.append(data)

    page += 1
    time.sleep(2)

wb.save(FILE_PATH)