# Generated by Django 2.2.7 on 2019-11-27 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_name', models.CharField(max_length=30)),
                ('tree_type', models.CharField(max_length=30)),
                ('tree_description', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=10)),
                ('lng', models.CharField(max_length=10)),
                ('first_branch_height', models.IntegerField(max_length=255)),
                ('heighest_reach', models.IntegerField(max_length=255)),
                ('drop_zone', models.IntegerField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('age_range', models.CharField(max_length=30)),
                ('accessibility', models.IntegerField()),
                ('tree_fruit', models.BooleanField()),
                ('tree_view', models.BooleanField()),
                ('tree_animals', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
                ('photo_link', models.CharField(max_length=50)),
                ('rating_overall', models.IntegerField()),
                ('rating_climbability', models.IntegerField()),
                ('rating_interest', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='trees.Trees')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
