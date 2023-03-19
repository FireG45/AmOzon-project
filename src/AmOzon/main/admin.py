from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)

@admin.action(description='Дублировать выбраннные записи')
def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()

@admin.action(description='Переименовывет выбраннные записи в записи с id в имени')
def set_name_as_id(modeladmin, request, queryset):
    for object in queryset:
        object.title = object.id
        object.save()

@admin.action(description='Рандомизирует цену у выбраннныъ записей')
def randomize_price(modeladmin, request, queryset):
    import random
    for object in queryset:
        object.price = random.randint(65, 125000)
        object.save()

admin.site.add_action(duplicate)
admin.site.add_action(set_name_as_id)
admin.site.add_action(randomize_price)
