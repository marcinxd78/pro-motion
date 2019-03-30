from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Prom
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration
# Register your models here.


#admin.site.register(SiteConfiguration, SingletonModelAdmin)



@admin.register(Prom)
class PromAdmin(admin.ModelAdmin):
    list_display = ('Prod_name', 'Start_date', 'Stop_date', 'Main_label', 'image_tag', 'exit_price', 'show_day',)
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    fieldsets = [
        ['Nazwa produktu', {
            'fields': ['Prod_name', ]
        }], ['Data', {
            'fields': ['Start_date', 'Stop_date']
        }], ['Opis produktu', {
            'fields': ['Main_label', 'Second_label']
        }], ['Cena', {
            'fields': [('Price_whole', 'Price_rest'), 'Price_sep', 'Gram_sep', 'Product_weight']
        }], ['Prezentacja', {
            'fields': ['Product_img', 'image_tag', ]
        }], ['Opcje dodatkowe', {
            'fields': ['Type_slide', ]
        }], ]

    def image_tag(self, obj, ):

        if obj.Product_img:
            return mark_safe('<img src="{url}" width="150px" height=150px />'.format(
                url=obj.Product_img.url
            ))
        else:
            return "Brak zdjęcia"

    image_tag.short_description = 'Zdjęcie'

#@admin.register(SiteConfiguration)
#class ConfigAdmin(SingletonModelAdmin):
 #   fieldsets = [
  #      ['Otwarte w niedziele', {
   #         'fields': ['Type_sun', 'Type_mode_sun' ]
    #    }], ['Informacja', {
     #       'fields': ['Type_info', 'Type_mode_info']
      #  }], ['Przedstaw wszystkie produkty', {
       #     'fields': ['Type_mode_all']
        #}]]

