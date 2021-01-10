from django.db import models


# 权重股的涨跌
class STOCK(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    change = models.FloatField()
    change_rate = models.FloatField()


# 权重股在基金中的权重
class WEIGHT(models.Model):
    fund_code = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    weight = models.FloatField()
    update_time = models.DateTimeField(auto_now_add=True)


# 场内实时价格
class FUNDIN(models.Model):
    fund_code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    update_time = models.DateTimeField(auto_now_add=True)
    open_price = models.FloatField()
    close_price = models.FloatField()
    change = models.FloatField()
    change_rate = models.FloatField()


# 场外价格（基金的净值），一天一更新
class FUNDOUT(models.Model):
    fund_code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, unique=True)
    update_time = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    change_rate = models.FloatField()
