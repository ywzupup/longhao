from django import forms
from .models import ConsultPost, MeasurePost
from django.contrib.auth.models import User

class ConsultPostForm(forms.ModelForm):
    consult_company_name = forms.CharField(max_length=50, required=True, error_messages={'required': "请输入正确的企业名称"})
    apply_name = forms.CharField(max_length=50, required=True, error_messages={'required': "请输入正确的申请人名称"})
    tel_number = forms.IntegerField(max_value=99999999999, min_value=10000000000, error_messages={'required': "请输入正确的电话号码"})
    email = forms.EmailField(required=False, error_messages={"required": "请输入正确的邮箱"})
    money = forms.FloatField(min_value=0, error_messages={"required": "请输入正确的融资金额"})
    use_for = forms.CharField(required=False)
    class Meta:
        model = ConsultPost
        fields = ('consult_company_name', 'apply_name', 'tel_number', 'email', 'money', 'use_for')

        
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class MeasurePostForm(forms.ModelForm):
    measure_company_name = forms.CharField(max_length=50, required=True, error_messages={'required': "请输入正确的企业名称"})
    register_place = forms.CharField(max_length=50, required=True, error_messages={'required': "请输入正确的注册地"})
    income = forms.FloatField(min_value=0, error_messages={'required': "请输入正确的近12个月主营业务收入"})
    profit = forms.FloatField(min_value=0, error_messages={"required": "请输入正确的近12个月净利润"})
    security_nums = forms.IntegerField(min_value=0, error_messages={"required": "请输入正确的当期社保人数"})
    debt = forms.FloatField(min_value=0, error_messages={"required": "请输入正确的负债总额"})
    patent = forms.IntegerField(min_value=0, error_messages={"required": "请输入正确的专利个数"})
    practice = forms.IntegerField(min_value=0, error_messages={"required": "请输入正确的实用新型个数"})
    software = forms.IntegerField(min_value=0, error_messages={"required": "请输入正确的软件著作个数"})
    design = forms.IntegerField(min_value=0, error_messages={"required": "请输入正确的外观设计个数"})
    company_value = forms.IntegerField(required=False, min_value=0,error_messages={"required": "请输入正确的企业名下办公楼、厂房等市场价值"})
    personal_value = forms.IntegerField(required=False, min_value=0,error_messages={"required": "请输入正确的个人名下办公楼、厂房等市场价值"})
    limit = forms.IntegerField(min_value=0, required=False)
    class Meta:
        model = MeasurePost
        fields = ('measure_company_name', 'register_place', 'income', 'profit', 
                'security_nums', 'debt', 'patent', 'practice', 'software', 
                'design', 'company_value', 'personal_value', 'limit')
    