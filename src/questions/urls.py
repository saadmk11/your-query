from django.conf.urls import url
from .views import question_list, question_detail, question_ask, category_list, category


urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^ask/$', question_ask, name='question_ask'),
    url(r'^categories/$', category_list, name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', category, name='category'),
    url(r'^(?P<slug>[\w-]+)/$', question_detail, name='question_detail'),
]