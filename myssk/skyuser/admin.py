from django.contrib import admin
from .models import UserInfo, UserApply, DataList


class ApplyInline(admin.TabularInline):
    model = UserApply
    fields = ['uid', 'data_year', 'goal', 'certificate', 'apply_date', 'result', 'check_date']
    def get_readonly_fields(self, request, obj=None):

        return ['uid', 'data_year', 'goal', 'certificate', 'apply_date']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 0
        return max_num


class InfoInline(admin.TabularInline):
    model = UserInfo
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['result']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 50
        return max_num


class UserInfoAdmin(admin.ModelAdmin):
    model = UserInfo
    list_display = ('user', 'name', 'sex', 'org', 'subject', 'zhicheng', 'tele')
    fields = (
        ('user', 'name', 'sex', 'idcard'),
        ('org', 'subject', 'zhicheng'),
        ('tele', 'adress')
    )
    readonly_fields =['user', 'name', 'sex', 'idcard', 'org', 'subject', 'zhicheng', 'tele', 'adress']
    search_fields = ('user', 'name', 'sex', 'org')
    list_filter = ['sex', 'org', 'subject']
    inlines = [ApplyInline]


class UserApplyAdmin(admin.ModelAdmin):

    list_display = ('uid', 'data_year', 'goal', 'result', 'apply_date', 'check_date')

    search_fields = ['data_year']
    fields = ['uid', 'data_year', 'goal', 'apply_date', 'result', 'check_date']
    readonly_fields = ['uid', 'data_year', 'goal', 'apply_date', ]
    ordering = ['result', '-apply_date']
    list_filter = ['result', 'data_year', 'uid__sex']


class DataListAdmin(admin.ModelAdmin):
    model = DataList
    list_display = ('data_year', 'apply_file', 'data_file1', 'data_file2', 'data_file3', 'update_time')
    search_fields = ['data_year']
    ordering = ['-update_time']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserApply, UserApplyAdmin)
admin.site.register(DataList, DataListAdmin)

admin.site.site_header = '中国社会综合状况调查 用户管理系统'
admin.site.site_title = '中国社会综合状况调查 用户管理系统'