# Generated by Django 4.1.1 on 2022-09-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_area', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('OP', 'OPEN'), ('CB', 'CABIN')], default='OP', max_length=2)),
                ('area', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_api.project')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_api.space')),
            ],
        ),
    ]
