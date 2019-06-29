from django.db import models
from staff.models import StaffInfo


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    age = models.SmallIntegerField(max_length=4,verbose_name="年龄")
    desc = models.TextField(max_length=256, verbose_name="描述")

    owner = models.ForeignKey(StaffInfo,null=True, related_name='customers', on_delete=models.DO_NOTHING, verbose_name="对接人员")
    status = models.BooleanField(choices=((0, "未成交"), (1, "成交")), max_length=16, default=0, help_text="状态")

    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "customer"
        verbose_name = "客户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name