from django.shortcuts import render
from app01 import models
import requests
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s [%(module)s] %(message)s', level=logging.INFO)
log = logging.getLogger()


def stocks_cn(code="hk00700", name="腾讯控股", start="2020-08-10", end="2020-08-14"):
    """获取 中国A股、港股的历史记录，并写入数据库中"""
    url = "http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?_var=&param=%s,day,%s,%s,640,qfq" % (code, start, end)
    req = requests.get(url)
    js = req.json()
    # print(js)
    content = js["data"][code]["day"][-1]  # end
    content0 = js["data"][code]["day"][-2]  # end before 1 day
    open_price = float(content[1])
    close_price = float(content[2])
    change = float("%.3f" % (close_price - float(content0[2])))
    change_rate = float("%.3f" % ((close_price / float(content0[2]) - 1) * 100.))
    ttime = content[0]

    log.info("\n日期 {} | 股票 {} | 代码 {} | 开盘价 {} | 收盘价 {} | 涨跌 {} | 涨跌幅 {}".format(ttime, name, code, open_price, close_price, change, change_rate))
    stockobj = models.STOCK(
        code=code,
        name=name,
        update_time=ttime,
        open_price=open_price,
        close_price=close_price,
        change=change,
        change_rate=change_rate,
    )
    stockobj.save()
    return change_rate


def stocks_us(code="usBABA"):
    """获取美股最新一个交易日的记录"""
    url = 'http://qt.gtimg.cn/q=%s' % code
    req = requests.get(url)
    response = req.content
    content = response.decode('GBK')

    content = content.split("~")
    name = content[1]
    open_price = float(content[5])  # 5：今开  4：昨收
    close_price = float(content[3])  # 3：现价（实时价、收盘价）
    change = float(content[31])  # 涨跌
    change_rate = float(content[32])  # 32：涨跌幅  33：今日最高价  34：今日最低价  35同3
    ttime = content[30]

    log.info("\n日期 {} | 股票 {} | 代码 {} | 开盘价 {} | 收盘价 {} | 涨跌 {} | 涨跌幅 {}".format(ttime, name, code, open_price, close_price, change, change_rate))
    stockobj = models.STOCK(
        code=code,
        name=name,
        update_time=ttime,
        open_price=open_price,
        close_price=close_price,
        change=change,
        change_rate=change_rate,
    )
    stockobj.save()
    return change_rate




