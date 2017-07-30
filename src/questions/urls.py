from django.conf.urls import url
from .views import (question_list, 
                    question_detail, 
                    question_ask, 
                    question_update, 
                    category_list, 
                    category,
                    answer_update,
                    question_delete,
                    answer_delete)


urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^ask/$', question_ask, name='question_ask'),
    url(r'^categories/$', category_list, name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', category, name='category'),
    url(r'^(?P<slug>[\w-]+)/delete/$', question_delete, name='question_delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$', question_update, name='question_update'),
    url(r'^(?P<slug>[\w-]+)/answer/(?P<pk>\d+)/edit/$', answer_update, name='answer_update'),
    url(r'^(?P<slug>[\w-]+)/answer/(?P<pk>\d+)/delete/$', answer_delete, name='answer_delete'),
    url(r'^(?P<slug>[\w-]+)/$', question_detail, name='question_detail'),
]