# Generated by Django 2.2.1 on 2019-05-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(blank=True, max_length=150, null=True)),
                ('image_2', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=150, null=True)),
                ('display', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('attribute_value_id', models.IntegerField()),
            ],
            options={
                'db_table': 'product_attribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_id', models.IntegerField()),
            ],
            options={
                'db_table': 'product_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('review', models.TextField()),
                ('rating', models.SmallIntegerField()),
                ('created_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
    ]
