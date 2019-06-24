import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "CRM"  # 设置站点标题
    site_footer = "员工管理系统"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)


from .models import StaffInfo
class StaffInfoModelAdmin(object):
    """员工管理类"""
    pass
xadmin.site.register(StaffInfo, StaffInfoModelAdmin)