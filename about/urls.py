from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('docurey/<int:id>', views.docurey),
]
