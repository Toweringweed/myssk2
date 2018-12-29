from django import forms
from django.forms import ModelForm
from .models import UserInfo, UserApply, DataList
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm, Textarea

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        # fields = '__all__'
        exclude = ['user']

class ApplyForm(ModelForm):
    class Meta:
        model = UserApply
        fields = ['data_year', 'goal', 'certificate']
        widgets = {
            'goal': Textarea(attrs={'cols': 55, 'rows': 6})
        }
    def clean(self):
        goal = self.cleaned_data['goal']
        if len(goal)< 50:
            raise forms.ValidationError('申请目的不得少于50字！')





