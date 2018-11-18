from django.db import models


# Create your models here.

class noteInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name=u"姓名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=255, verbose_name=u"联系地址")
    leave_msg = models.CharField(max_length=1000, verbose_name=u"留言")
    update_time = models.DateField(auto_now=True)
    # 创建列的verbose_name信息，该信息在后台管理系统中显示

    # 创建该表格的Meta信息，该信息在后台管理系统中显示
    class Meta:
        verbose_name = u"用户留言信息"
