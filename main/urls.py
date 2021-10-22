from home.views import home,historyView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name='home'),
    path('history/',historyView,name='history')
]
