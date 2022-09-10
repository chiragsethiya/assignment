from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    # def update(self, instance, validated_data):
    #     validated_data.pop('name', None)
    #     return super().update(instance, validated_data)

    class Meta:
        model = models.Project
        fields = ['id', 'name', 'total_area']


class SpaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='space.name')
    area = serializers.IntegerField(source='space.area')

    class Meta:
        model = models.ProjectSpace
        fields = ['name', 'area', 'count']
