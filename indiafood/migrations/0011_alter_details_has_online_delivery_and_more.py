# Generated by Django 4.2.1 on 2023-06-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indiafood', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='has_online_delivery',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='has_table_booking',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='is_book_form_web_view',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='is_delivering_now',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='is_table_reservation_supported',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='opentable_support',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='price_range',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='switch_to_order_menu',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='cityid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='votes',
            field=models.IntegerField(),
        ),
    ]
