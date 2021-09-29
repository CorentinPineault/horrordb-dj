# Generated by Django 3.2.7 on 2021-09-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webseries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('creators', models.ManyToManyField(to='common.Person')),
                ('tags', models.ManyToManyField(to='common.Tag')),
            ],
        ),
    ]
