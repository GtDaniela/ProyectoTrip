from django.contrib import admin
from django.urls import path,re_path
from apptrip import views
from apptrip.views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'apptrip'
#para1:nombrecontrolador, para2:nombredelafuncion asociada(vista) param3:alias
urlpatterns = [
    re_path('admin/', admin.site.urls),
    # re_path('accounts/', include('django.contrib.auth.urls')),
    # re_path(r'^$',LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^$', views.login, name='login'),
    re_path('inicio/',views.inicio, name="inicio"),
    re_path('registrarse/', views.registrarse, name='registrarse'),
    re_path('login/', views.login, name='login'),
    re_path(r'^logout/$',LogoutView.as_view(), name='logout')
    # re_path('logout/',LogoutView.as_view(), name='logout')

]
