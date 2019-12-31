from django.shortcuts import render, redirect
from .models import ConsultPost, IndustryColumn, MeasurePost
from django.http import HttpResponse
from .forms import ConsultPostForm, UserLoginForm, MeasurePostForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home.html')
def plan(request):
    return render(request, 'plan.html')
def example(request):
    return render(request, 'example.html')
def aboutus(request):
    return render(request, 'aboutus.html')

def supervise_list(request):
    if request.GET.get('category') == 'measure':
        measure_list = MeasurePost.objects.all()
        category = 'measure'
        paginotor = Paginator(measure_list, 5)
        page = request.GET.get('page')
        measures = paginotor.get_page(page)
        context = {'measures': measures, 'category': category}
    else:
        consult_list = ConsultPost.objects.all()
        category = 'consult'
        paginotor = Paginator(consult_list, 5)
        page = request.GET.get('page')
        consults = paginotor.get_page(page)
        context = {'consults': consults, 'category': category}
   
    return render(request, 'supervise.html', context)

def consult_detail(request, id):
    consult = ConsultPost.objects.get(id=id)
    context = {'consult': consult}
    return render(request, 'consult_detail.html', context)

def success_detail(request, id):
    measure = MeasurePost.objects.get(id=id)
    context = {'measure': measure}
    return render(request, 'limit.html', context)

def measure_detail(request, id):
    measure = MeasurePost.objects.get(id=id)
    context = {'measure': measure}
    return render(request, 'measure_detail.html', context)



def post(request):
    if request.method == "POST":
        if 'consult_post' in request.POST:
            consult_post_form = ConsultPostForm(data=request.POST)
            if consult_post_form.is_valid():
                new_consult = consult_post_form.save(commit=False)
                if request.POST['consult_column'] != 'none':
                    new_consult.consult_column = IndustryColumn.objects.get(id=request.POST['consult_column'])
                else:
                    return HttpResponse("请选择企业所属行业")
                new_consult.save()
                return redirect("longhaotianhua:contactus")
            else:
                allerror = ""
                for error in consult_post_form.errors:
                    allerror = allerror + consult_post_form.errors[error][0] + "  "
                return HttpResponse(allerror)
        elif 'measure_post' in request.POST:
            measure_post_form = MeasurePostForm(data=request.POST)
            if measure_post_form.is_valid(): 
                new_measure = measure_post_form.save(commit=False)
                if (request.POST['measure_column']) != 'none':
                    # 初始化变量
                    A = B = C = D = E = F = G = H = I = J = K = 0
                    flag = False
                    register_place = measure_post_form.cleaned_data['register_place']
                    income = measure_post_form.cleaned_data['income']
                    profit = measure_post_form.cleaned_data['profit']
                    security_nums = measure_post_form.cleaned_data['security_nums']
                    debt = measure_post_form.cleaned_data['debt']
                    patent = measure_post_form.cleaned_data['patent']
                    if (request.POST['company_value']) != '':
                        company_value = measure_post_form.cleaned_data['company_value']
                        J = int(company_value)
                    else:
                        new_measure.company_value = 0
                    if (request.POST['personal_value']) != '':
                        personal_value = measure_post_form.cleaned_data['personal_value']
                        K = int(personal_value)
                    else:
                        new_measure.personal_value = 0

                    new_measure.measure_column = IndustryColumn.objects.get(id=request.POST['measure_column'])
                    if ('1' == request.POST['measure_column']):
                        B = 10
                    elif ('3' == request.POST['measure_column']):
                        C = 5
                    elif ('4' == request.POST['measure_column']):
                        flag = True
                        D = 10
                        

                    if ('海淀' in register_place):
                        A = 10
                    if ('朝阳' in register_place):
                        A = 5
                    E = int(income)
                    if (int(profit) <= 0):
                        F = -10
                    if (int(security_nums) < 10):
                        G = -10
                    elif (10 <= int(security_nums) < 20):
                        G = 5
                    elif (20 <= int(security_nums)< 50):
                        G = 10
                    elif (50 <= int(security_nums) < 80):
                        G = 15
                    else:
                        G = 20
                    H = int(debt)
                    I = int(patent) * 10
                    
                    limit = A + B + C + D + (E - H) / 2 + F + G + I + J * 0.6 + K
                    if (flag and (int(limit) > 300)):
                        limit = 300
                    new_measure.limit = limit
                else:
                    return HttpResponse("请选择企业所属行业")
                new_measure.save()
                return redirect("longhaotianhua:success_detail", id=new_measure.id)
            else:
                allerror = ""
                for error in measure_post_form.errors:
                    allerror = allerror + measure_post_form.errors[error][0] + "  "
                return HttpResponse(allerror)     
    else:
        consult_post_form = ConsultPostForm()
        measure_post_form = MeasurePostForm()
        columns = IndustryColumn.objects.all()
        context = {'consult_post_form': consult_post_form, 'measure_post_form': measure_post_form, 'columns': columns}
        return render(request, 'contactus.html', context)

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("longhaotianhua:supervise")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")