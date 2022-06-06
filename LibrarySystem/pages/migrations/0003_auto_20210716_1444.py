# Generated by Django 3.2.5 on 2021-07-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210710_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='addbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50, null=True)),
                ('bookauthor', models.CharField(max_length=50, null=True)),
                ('ISBN', models.CharField(max_length=50, null=True)),
                ('Year', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]