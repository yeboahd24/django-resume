from django.urls import path
from .views import resume


urlpatterns = [
    path('<int:pk>/', resume, name='resume'),
]