from django.shortcuts import render
from .models import UserInfo, UserApply, DataList
from django.forms import modelformset_factory
from .forms import UserInfoForm, ApplyForm
from django.contrib.auth import get_user, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import StreamingHttpResponse
from django import forms

def user_center(request):
   return render(request, 'skyuser/user_center.html')

def user_map(request):
    return render(request, 'skyuser/user_map.html')

def user_info(request):
    if request.user.is_authenticated():
        user = get_user(request)
        user_id = user.id
        if UserInfo.objects.filter(user_id=user_id):
            messages.warning(request, '填写准确的个人资料，是申请数据成功的基础！')
            a = UserInfo.objects.get(user_id=user_id)
            form_user = UserInfoForm(instance=a)
        else:
            messages.warning(request, '在申请数据前需要填写个人资料，请先完善个人资料！')
            a = UserInfo(user_id=user_id)
        if request.method == 'POST':
            form_user = UserInfoForm(request.POST, request.FILES, instance=a)
            if form_user.is_valid():
                form_user.save()
                messages.success(request, '更新个人资料完成！')
                return HttpResponseRedirect('user_info/')
        else:
            form_user = UserInfoForm(instance=a)
    else:
        messages.warning(request, '请先登录或注册成为本站用户！')
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'skyuser/user_info.html', {'form_user': form_user})

def data_apply(request):
    if request.user.is_authenticated():
        user = get_user(request)
        if UserInfo.objects.filter(user_id=user):
            user_queryset = UserInfo.objects.get(user_id=user)
            user_id = user_queryset.id
            a = UserApply(uid_id=user_id, apply_date=timezone.now())
            if request.method == 'POST':
                form_apply = ApplyForm(request.POST, request.FILES, instance=a, initial={'apply_date': timezone.now()})
                if form_apply.is_valid():
                    form_apply.save()
                    messages.success(request, '提交成功')
                    return HttpResponseRedirect('/skyuser/apply_list/')
                else:
                    messages.warning(request, '申请目的不得少于50字！')

            else:
                form_apply = ApplyForm(instance=a)
        else:
            messages.warning(request, '请先补充个人信息！')
            return HttpResponseRedirect('/skyuser/user_info/')
    else:
        messages.warning(request, '请先登录或注册成为本站用户！')
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'skyuser/data_apply.html', {'form_apply': form_apply})

def apply_list(request):
    if request.user.is_authenticated():
        user = get_user(request)
        if UserInfo.objects.filter(user_id=user):
            user_queryset = UserInfo.objects.get(user_id=user)
            user_id = user_queryset.id
            apply_queryset = UserApply.objects.filter(uid_id=user_id). \
                values('id', 'data_year__data_year', 'goal', 'apply_date', 'result', 'result_why',
                       'data_year__data_file1', 'data_year__data_file2', 'data_year__data_file3')
        else:
            apply_queryset = UserApply.objects.filter(uid_id=-1). \
                values('id','data_year__data_year', 'goal', 'apply_date', 'result',
                       'data_year__data_file1', 'data_year__data_file2', 'data_year__data_file3')
    else:
        messages.warning(request, '请先登录或注册成为本站用户！')
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'skyuser/apply_list.html', {'apply_queryset': apply_queryset})

def apply_edit(request, id):
    if request.user.is_authenticated():
        a = UserApply.objects.get(id=id)
        if request.method == 'POST':
            form_apply = ApplyForm(request.POST, request.FILES, instance=a)
            if form_apply.is_valid():
                form_apply.save()
                return HttpResponseRedirect('/skyuser/apply_list')
        else:
            form_apply = ApplyForm(instance=a)
    else:
        messages.warning(request, '请先登录或注册成为本站用户！')
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'skyuser/data_apply.html', {'form_apply': form_apply})

def apply_del(request, id):
    if request.user.is_authenticated():
        a = UserApply.objects.get(id=id)
        a.delete()

        return HttpResponseRedirect('/skyuser/apply_list')


def file_down(request, path):
    the_file_name= str(path).split('/')[-1]             #显示在弹出对话框中的默认的下载文件名
    filename=path    #要下载的文件路径
    response=StreamingHttpResponse(readFile(filename))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)
    return response

def readFile(filename,chunk_size=5120):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break

# class Apply_list(ListView)
#     def apply_list(request):
#         if request.user.is_authenticated():
#             user = get_user(request)
#             apply_queryset = UserApply.objects.filter(uid_id=user.id)
#
#         else:
#             return HttpResponseRedirect('accounts/login/')
#         return render(request, 'skyuser/apply_list.html', {'apply_queryset': apply_queryset})
