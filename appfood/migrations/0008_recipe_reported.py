# Generated by Django 5.1.3 on 2024-12-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfood', '0007_rename_recipe_notification_recipess'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
