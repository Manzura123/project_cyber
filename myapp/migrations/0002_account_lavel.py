# Generated by Django 5.1.2 on 2024-12-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='lavel',
            field=models.CharField(default='dasturchi', max_length=50, verbose_name='lavozimi'),
            preserve_default=False,
        ),
    ]
