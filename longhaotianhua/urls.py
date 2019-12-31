from django.urls import path
from . import views

app_name = 'longhaotianhua'

urlpatterns = [
    path('supervise/', views.supervise_list, name='supervise'),
    path('supervise-consult-detail/<int:id>/', views.consult_detail, name='supervise_consult_detail'), 
    path('supervise-measure-detail/<int:id>/', views.measure_detail, name='supervise_measure_detail'), 
    path('contactus/', views.post, name='contactus'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('plan/', views.plan, name='plan'),
    path('example/', views.example, name='example'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('success-detail/<int:id>/', views.success_detail, name='success_detail'),
]