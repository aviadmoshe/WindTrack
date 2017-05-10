"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import FormView
from . import views,forms

urlpatterns = [
    url(r'^form$', FormView.as_view(template_name="torasearch/upload_form.html",form_class=forms.UploadForm)),
    #url(r'^form$', FormView.as_view(template_name="torasearch/upload_form.html",form_class=forms.UpdateToraForm)),
    #url(r'^SubmitYeshiva', views.SubmitYeshiva, name = 'SubmitYeshiva'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name = 'detail'),
    #url(r'^search/', views.search, name = 'search'),
    url(r'^search/', include('haystack.urls'), name = 'search'),
    url(r'^index$', views.IndexView.as_view(), name = 'index'),
    url(r'^$', views.homepage.as_view(), name = 'homepage'),
    url(r'^Yeshiva/add/$', views.yeshiva_create.as_view(), name = 'yeshiva_add'),
    url(r'^Yeshiva/(?P<pk>[0-9]+)/delete/$', views.yeshiva_delete.as_view(), name='yeshiva_delete'),
    url(r'^Yeshiva/(?P<pk>[0-9]+)/$', views.yeshiva_update.as_view(), name='yeshiva_update'),
    url(r'^register/$', views.RegisterView.as_view(), name = 'register'),
    url(r'^login/$', views.LoginView.as_view(), name = 'login'),
    url(r'^logout/$', views.LogOutView.as_view(), name = 'logout'),
    url(r'^upload/$', views.UpLoadView.as_view(), name = 'upload'),
    url(r'^ReadText/(?P<pk>[0-9]+)$', views.TextReadView.as_view(), name = 'read_text'),
    url(r'^test/$', views.homepage.as_view(), name = 'test'),
    #url(r'^$', include('personal.urls')),
    #url(r'^blog/', include('blog.urls')),
    
]
