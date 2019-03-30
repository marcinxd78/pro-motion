from datetime import timedelta

from django.db import models
from solo.models import SingletonModel
# Create your models here.
from django.utils.safestring import mark_safe

class SiteConfiguration(SingletonModel):

    Type_sun = models.CharField(max_length=255, default='', verbose_name='Oznaczenie')
    Type_mode_sun = models.BooleanField(default=False, verbose_name='Aktywność')
    Type_info = models.CharField(max_length=255,default='',blank=True , verbose_name='Oznacznie')
    Type_mode_info = models.BooleanField(default=False, verbose_name='Aktywność')
    Type_mode_all = models.BooleanField(default=False, verbose_name="Aktywność")

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Konfiguracja"

class Prom(models.Model):
    Prod_name = models.CharField(max_length=128, verbose_name='Produkt')  # nazwa produktu
    Start_date = models.DateField(null=True, blank=True,
                                  verbose_name='Data rozpoczęcia wyświetlania')  # data rozpoczecia wyświetlania
    Stop_date = models.DateField(null=True, blank=True,
                                 verbose_name='Data zakończnia wyświetlania')  # data zakończenia wyświetlania
    Main_label = models.CharField(max_length=128, null=True, verbose_name='Główny label')  # główny label
    Second_label = models.CharField(max_length=72, null=True, blank=True,
                                    verbose_name='Dodatkowy label', default=' ')  # pomocniczy label
    Price_whole = models.IntegerField(null=True, blank=True, verbose_name='Cena całkowita')  # cena część całkowita
    Price_rest = models.IntegerField(null=True, blank=True, verbose_name='Reszta')  # cena reszta
    Product_weight = models.CharField(max_length=20, null=True, blank=True, default=' ', verbose_name='Gramatura')
    Product_img = models.ImageField(null=True, blank=True, verbose_name='Zdjęcie produktu')  # zdjęcie produktu
    Type_slide = models.BooleanField(default=False,
                                     verbose_name='Slajd informacyjny')  # typ slajdy dla zmiany grida
    Price_sep = models.CharField(null=True, blank=True, default=",", max_length=10,
                                 verbose_name='Separator ceny')  # separator ceny
    Gram_sep = models.CharField(null=True, blank=True, default="/", max_length=10,
                                verbose_name='Separator gramatury')  # separator gramatury

    def __str__(self):
        return self.Prod_name

    @property
    def exit_price(self):
        return str(self.Price_whole) + ',' + str(self.Price_rest) + ' zł'

    exit_price.fget.short_description = 'Cena'

    @property
    def show_day(self):
        return ((self.Stop_date - self.Start_date) + timedelta(days=1))

    show_day.fget.short_description = 'Wyświetlanie'

    class Meta:
        verbose_name = 'Promocja'
        verbose_name_plural = 'Promocje'
