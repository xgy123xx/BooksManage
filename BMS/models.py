from django.db import models

# Create your models here.
class Book(models.Model):
    nid = models.AutoField(primary_key=True)    #AutoField有序整形 IntegerField整形
    title = models.CharField(max_length=32)    #CharField字符
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)
    publishDate = models.DateField()    #DateField日期类型
    price = models.DecimalField(max_digits=5, decimal_places=2)    #DecimalField浮点型也可以用FloatField
