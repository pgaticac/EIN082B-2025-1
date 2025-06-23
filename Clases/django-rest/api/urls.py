from rest_framework import routers
from django.urls import path, include
from .views import CarreraViewSet

router = routers.DefaultRouter()
router.register('carrera',CarreraViewSet)



urlpatterns =[
    path('',include(router.urls))
]