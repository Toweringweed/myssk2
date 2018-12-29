from django.db import models
from users.models import User


class UserInfo(models.Model):
    class Meta:
        verbose_name = '个人资料'
        verbose_name_plural = '个人资料'
    user = models.OneToOneField(User, unique=True, verbose_name='用户')
    # user_name = models.CharField('用户名', max_length=20, default='')
    name = models.CharField('真实姓名', max_length=20, default='')
    sex_list = (
        ('男', '男'),
        ('女', '女')
    )
    sex = models.CharField('性别', max_length=2, choices=sex_list, default='')
    idcard = models.CharField('身份证号', max_length=20, default='')
    org = models.CharField('单位', max_length=40, default='')
    subject = models.CharField('专业', max_length=20, default='')
    zhicheng = models.CharField('职称', max_length=20, default='')
    tele = models.CharField('电话号码', max_length=11, default='')
    # email = models.CharField('邮箱', max_length=30, default='')
    adress = models.CharField('地址', max_length=40, default='')
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

class DataList(models.Model):
    class Meta:
        verbose_name = 'CSS数据'
        verbose_name_plural = 'CSS数据'
    data_year = models.CharField('数据名称', max_length=40, default='')
    apply_file = models.FileField('申请表', upload_to='up_data/%Y/%m', null=True, blank=True)
    data_file1 = models.FileField('数据附件1', upload_to='up_data/%Y/%m', null=True, blank=True)
    data_file2 = models.FileField('数据附件2', upload_to='up_data/%Y/%m', null=True, blank=True)
    data_file3 = models.FileField('数据附件3', upload_to='up_data/%Y/%m', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.data_year

class UserApply(models.Model):
    class Meta:
        verbose_name = '数据申请'
        verbose_name_plural = '数据申请'
    uid = models.ForeignKey(UserInfo, verbose_name="用户名")
    data_year = models.ForeignKey(DataList, verbose_name="数据名称")
    goal = models.CharField('申请目的', max_length=1000, default='')
    certificate = models.FileField('上传申请表', max_length=100, upload_to='up_apply')
    result_list = (
        ('未审核', '未审核'),
        ('审核中', '审核中'),
        ('审核通过', '审核通过'),
        ('审核未通过', '审核未通过')
    )
    result = models.CharField('申请结果', max_length=10, choices=result_list, default='未审核', null=True, blank=True)
    apply_date = models.DateTimeField('申请时间', null=True, blank=True)
    check_date = models.DateTimeField('审核时间', null=True, blank=True)

    def __str__(self):
        return str(self.data_year)


