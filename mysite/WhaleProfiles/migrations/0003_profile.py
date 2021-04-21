# Generated by Django 3.1.6 on 2021-04-19 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('WhaleProfiles', '0002_auto_20210326_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('verified', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=500)),
            ],
        ),
    ]