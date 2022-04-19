# Generated by Django 4.0.4 on 2022-04-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='Адрес электронной почты')),
                ('role', models.IntegerField(choices=[(1, 'Подписчик'), (2, 'Автор')], verbose_name='Роль')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]