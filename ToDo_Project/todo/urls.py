from django.contrib import admin
from django.urls import path,include

handler404 = 'django.views.defaults.page_not_found'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todo_app.urls')),
]
