# Generated by Django 2.2.1 on 2019-05-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_id', models.CharField(max_length=32)),
                ('product_id', models.IntegerField()),
                ('attributes', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField()),
                ('buy_now', models.IntegerField()),
                ('added_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'shopping_cart',
                'managed': False,
            },
        ),
    ]
