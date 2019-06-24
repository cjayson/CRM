import xadmin

from .models import Customer
class CustomerModelAdmin(object):
    """员工管理类"""
    pass
xadmin.site.register(Customer, CustomerModelAdmin)