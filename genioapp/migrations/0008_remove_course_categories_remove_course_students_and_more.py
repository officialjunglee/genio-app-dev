# Generated by Django 4.2.7 on 2023-11-20 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("genioapp", "0007_merge_20231119_0142"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="categories",
        ),
        migrations.RemoveField(
            model_name="course",
            name="students",
        ),
        migrations.RemoveField(
            model_name="instructor",
            name="students",
        ),
        migrations.RemoveField(
            model_name="student",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="student",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="status",
        ),
        migrations.AddField(
            model_name="student",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="country",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="student",
            name="gender",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="student",
            name="name",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="genioapp.instructorprofile",
            ),
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
                (
                    "email",
                    models.EmailField(
                        default="w@example.com", max_length=254, unique=True
                    ),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=10)),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("country", models.CharField(blank=True, max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]