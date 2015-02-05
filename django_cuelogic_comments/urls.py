from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mongodbapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', "django_cuelogic_comments.Comments.get"),
    url(r'edit/(?P<id>\d+)/', "django_cuelogic_comments.Comments.edit"),
    url(r'delete/(?P<id>\d+)/', "django_cuelogic_comments.Comments.delete"),
    url(r'reply/$', "django_cuelogic_comments.Comments.reply"),
)
