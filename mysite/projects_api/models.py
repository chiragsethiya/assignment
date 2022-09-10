from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    total_area = models.IntegerField(default=0)


class Space(models.Model):
    WORKSPACE_TYPES = [
        ('OP', 'OPEN'),
        ('CB', 'CABIN')
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=2, choices=WORKSPACE_TYPES, default='OP')
    area = models.IntegerField(default=0)


class ProjectSpace(models.Model):
    space = models.ForeignKey('Space', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
