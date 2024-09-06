# Generated by Django 4.2.4 on 2023-09-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0035_remove_user_pfimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewandRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]