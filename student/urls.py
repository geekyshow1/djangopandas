from django.urls import path
from student import views
urlpatterns = [
    path('', views.home, name='home'),
    path('import_students/', views.import_students, name='import_students'),
]
