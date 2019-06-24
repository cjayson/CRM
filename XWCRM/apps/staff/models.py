from django.db import models
from department.models import Department

# Create your models here.

class StaffInfo(models.Model):
    """
    账号(他的名字),密码,手机号码,个人描述,性别,部门,权限等级str 123
    """
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name="手机号码")
    desc = models.TextField(max_length=256,blank=True,null=True,verbose_name="个人描述")
    gender = models.BooleanField(choices=((0, '女'), (1, '男')), verbose_name='性别',
                              default=1)

    role = models.CharField(max_length=32, verbose_name="职位名称",default="")
    role_power = models.SmallIntegerField(max_length=2,verbose_name="角色权限")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)



    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "staff"
        verbose_name = "员工信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username