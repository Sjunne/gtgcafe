# Generated by Django 2.2.28 on 2022-04-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Coffee', 'Coffee'), ('Tea', 'Tea'), ('Smoothie', 'Smoothie'), ('Juice', 'Juice')], default='', max_length=10)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Jumbo', 'Jumbo')], max_length=10)),
                ('quantity', models.IntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]