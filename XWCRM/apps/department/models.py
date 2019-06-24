from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=32, unique=True,verbose_name="部门名称")
    desc = models.TextField(max_length=256,blank=True,null=True,verbose_name="部门描述")


    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "deparment"
        verbose_name = "部门表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name