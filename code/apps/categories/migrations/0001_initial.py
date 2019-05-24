# Generated by Django 2.2.1 on 2019-05-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
    ]