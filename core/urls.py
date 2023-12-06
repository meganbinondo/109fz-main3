from msilib.schema import AdminExecuteSequence
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from . import views
from .forms import LoginForm
from .views import CustomLoginView

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/index.html', authentication_form=LoginForm), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:index'), name='logout'),

]
