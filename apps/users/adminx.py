import xadmin
from xadmin import views

from users.models import UserProfile

# Register your models here.


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    site_title = "DjangoOA"
    site_footer = "DjangoOA"
    # menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSettings)



