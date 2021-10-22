from home.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name='home'),
    path('history/',historyView,name='history'),
    path('history/<id>',history_delete,name='history_delete')
]
