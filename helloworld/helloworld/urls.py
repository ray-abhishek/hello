from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import url, include
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', views.detail, name='deta'),
    url(r'^webhook/', views.handle_jenkins_server_webhooks, name='deta'),
    
)
