from django.conf.urls import url
from .views import question_list, question_detail, category_list, category


urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^categories/$', category_list, name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', category, name='category'),
    url(r'^(?P<pk>\d+)$', question_detail, name='question_detail'),
]