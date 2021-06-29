from django.contrib import admin
from django.urls import path
import bootstrapApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bootstrapApp.views.index, name='index'),
]
