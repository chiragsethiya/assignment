from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'spaces',
                views.SpaceViewSet, basename='project-spaces')

urlpatterns = [
    path('', include(router.urls)),
]
