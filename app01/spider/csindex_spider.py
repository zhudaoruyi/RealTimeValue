from bs4 import BeautifulSoup
import requests
import re


class SPIDER(object):
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.parse()

    def parse(self):
        res = requests.get(self.url)
        self.soup = BeautifulSoup(res.content, "html.parser")
        return 0

    def time(self):
        for s in self.soup.find_all('p', class_='more'):
            if re.match("截止日期", s.text):
                return s.text[5:]

    def weight_stock(self):
        ws = list()
        s = self.soup.find('table', class_='table table-even table-bg p_table tc').find('tbody')
        for tr in s.find_all('tr'):
            code = tr.find_all('td')[0].text
            name = tr.find_all('td')[1].text
            weight = float(tr.find_all('td')[3].text)
            if code.isalpha():
                code = "us" + code
            else:
                code = "hk" + "0" * (5-len(code)) + code
            ws.append({"code": code, "name": name, "weight": weight})
        return ws


def main():
    # res = requests.get("http://www.csindex.com.cn/zh-CN/indices/index-detail/H11136")
    # res = requests.get("http://www.csindex.com.cn/zh-CN/indices/index-detail/H30533")
    # s = BeautifulSoup(res.content, "html.parser")
    # s1 = s.find_all('h2', class_="t_3 mb-10 pr")
    # print("s1\n", s1)
    # # print(s.find_all('h2', class_="t_3 mb-10 pr"))
    # s2 = s.find_all('p', class_='more')
    # # s2 = s.find_all(src=re.compile("截止日期*"))
    # print("\ns2\n", s2)
    # s3 = s.find_all('table', class_="table table-even table-bg p_table tc")
    # print("\ns3\n", s3)
    spi = SPIDER("http://www.csindex.com.cn/zh-CN/indices/index-detail/H30533")
    t = spi.time()
    print(t)
    wes = spi.weight_stock()
    print(wes)
    return 0


if __name__ == '__main__':
    main()
