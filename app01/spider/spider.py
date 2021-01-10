from bs4 import BeautifulSoup
import requests


def main():
    # res = requests.get("http://www.csindex.com.cn/zh-CN/indices/index-detail/H11136")
    res = requests.get("http://www.csindex.com.cn/zh-CN/indices/index-detail/H30533")
    s = BeautifulSoup(res.content, "html.parser")
    s1 = s.find_all('h2', class_="t_3 mb-10 pr")
    print("s1\n", s1)
    s2 = s.find_all('p', class_='more')
    print("\ns2\n", s2)
    s3 = s.find_all('table', class_="table table-even table-bg p_table tc")
    print("\ns3\n", s3)
    return 0


if __name__ == '__main__':
    main()
