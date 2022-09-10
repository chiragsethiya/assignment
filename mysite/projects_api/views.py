from django.shortcuts import render

# Create your views here.

from . import models, serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = serializers.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            spaces = models.Space.objects.all()
            for space in spaces.iterator():
                project_space = models.ProjectSpace(
                    space=space, project_id=project.id)
                project_space.save()
            # device.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class SpaceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        try:
            workspace_type = self.request.query_params.get('type')
            project_spaces = models.ProjectSpace.objects.filter(
                project=int(self.request.query_params.get('project_id'))).filter(space__type__contains=workspace_type)
            return project_spaces
        except:
            return models.ProjectSpace.objects.all()
    serializer_class = serializers.SpaceSerializer
    permission_classes = [AllowAny]
