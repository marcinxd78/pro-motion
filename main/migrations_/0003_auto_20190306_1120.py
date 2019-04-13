# Generated by Django 2.1.7 on 2019-03-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190225_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prom',
            options={'verbose_name': 'Promocja', 'verbose_name_plural': 'Promocje'},
        ),
        migrations.AlterField(
            model_name='prom',
            name='Main_label',
            field=models.CharField(max_length=128, null=True, verbose_name='Główny label'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Price_rest',
            field=models.IntegerField(blank=True, null=True, verbose_name='Reszta'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Price_whole',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cena całkowita'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Prod_name',
            field=models.CharField(max_length=128, verbose_name='Produkt'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Product_img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Zdjęcie produktu'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Second_label',
            field=models.CharField(blank=True, default='', max_length=72, null=True, verbose_name='Dodatkowy label'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data rozpoczęcia wyświetlania'),
        ),
        migrations.AlterField(
            model_name='prom',
            name='Stop_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data zakończnia wyświetlania'),
        ),
    ]