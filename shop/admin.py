from django.contrib import admin

from shop.models import Product, Characteristic, Category


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'amount')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    list_filter = ('price', 'category', 'amount')
    search_fields = ('name', 'category')
    inlines = (CharacteristicInline,)
    autocomplete_fields = ('category',)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('product', 'key', 'value')
    ordering = ('product',)
    search_fields = ('product', 'key', 'value')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


