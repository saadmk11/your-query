"""yourquery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import (login_view, 
                            register_view, 
                            logout_view, 
                            user_profile, 
                            user_profile_update)
from contact.views import contact
from core.views import home, about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Core
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    #Accounts
    url(r'^profile/(?P<username>\w+)/$', user_profile, name='user_profile'),
    url(r'^profile/(?P<username>\w+)/edit/$', user_profile_update, name='user_profile_update'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    #Contact
    url(r'^contact/$', contact, name='contact'),
    #Questions
    url(r'^questions/', include('questions.urls', namespace='questions')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    