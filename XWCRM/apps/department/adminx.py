import xadmin

from .models import Department
class DepartmentModelAdmin(object):
    """员工管理类"""
    pass
xadmin.site.register(Department, DepartmentModelAdmin)