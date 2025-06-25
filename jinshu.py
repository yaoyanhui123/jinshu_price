import requests
from bs4 import BeautifulSoup
import json

# 目标网页 URL
url = "https://www.ccmn.cn/history_data/cjysw.html"

# 发起 HTTP 请求
response = requests.get(url)
html = response.text

# 解析 HTML
soup = BeautifulSoup(html, 'html.parser')

# 定位到 tbody 中的所有数据行（排除表头）
rows = soup.select('tbody tr')[1:]  # 跳过表头第一个 <tr>
columns = ["序号", "品名", "最低价", "最高价", "均价", "涨跌", "日期", "备注"]
all_data = []
# 遍历每一行，提取每个单元格
for row in rows:
    cols = row.find_all('td')
    data = [col.get_text(strip=True) for col in cols]
    result = dict(zip(columns, data))
    # if len(data) >= 2 and (data[1] == "1#铜" or data[1] == "A00铝" or data[1] == "1#锌"):
    #     td = {"name": data[1][-1], "price": data[4]if len(data) > 4 else 0}
    all_data.append(result)


with open("all_data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)