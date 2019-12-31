from django.db import models
from django.utils import timezone

# Create your models here.

class IndustryColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ConsultPost(models.Model):
    # 企业名称
    consult_company_name = models.CharField(max_length=50)
    # 申请人姓名
    apply_name = models.CharField(max_length=50)
    # 申请人电话
    tel_number = models.CharField(max_length=12)
    # 邮箱
    email = models.CharField(max_length=50)
    # 融资金额
    money = models.CharField(max_length=30)
    # 用途
    use_for = models.CharField(max_length=100)
    # 时间
    created = models.DateTimeField(default=timezone.now)

    consult_column = models.ForeignKey(
        IndustryColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='consult_company_name'
    )
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.consult_company_name

class MeasurePost(models.Model):
    # 1.企业名称
    measure_company_name = models.CharField(max_length=50)
    # 2.注册地
    register_place = models.CharField(max_length=50)
    # 3.近12个月主营业务收入
    income = models.CharField(max_length=50)
    # 4.近12个月净利润
    profit = models.CharField(max_length=50)
    # 5.当期社保人数
    security_nums = models.CharField(max_length=50)
    # 6.负债总额
    debt = models.CharField(max_length=50)
    # 7.专利
    patent = models.CharField(max_length=50)
    # 8.实用新型
    practice = models.CharField(max_length=50)
    # 9.软件著作
    software = models.CharField(max_length=50)
    # 10.外观设计
    design = models.CharField(max_length=50)
    # 11.企业市场价值
    company_value = models.CharField(max_length=50, default=0)
    # 12.个人市场价值
    personal_value = models.CharField(max_length=50, default=0)
    # 栏目
    measure_column = models.ForeignKey(
        IndustryColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='measure_company_name'
    )
    # 13. 初审额度
    limit = models.CharField(max_length=50, default="0")
    # 时间
    created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.measure_company_name


