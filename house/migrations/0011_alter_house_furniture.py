# Generated by Django 4.1.6 on 2023-02-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_remove_zv_tipe_remove_zv_user_alter_house_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='furniture',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
