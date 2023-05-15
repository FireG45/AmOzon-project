from django.contrib import admin
from .models import Product, OrderInfo, OrderItem
from userauth.models import Basket

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderInfo)
admin.site.register(OrderItem)
admin.site.register(Basket)

@admin.action(description='Дублировать выбраннные записи')
def duplicate(modeladmin, request, queryset):
    for object in queryset: # pragma: no cover
        object.id = None # pragma: no cover
        object.save() # pragma: no cover

@admin.action(description='Переименовывет выбраннные записи в записи с id в имени')
def set_name_as_id(modeladmin, request, queryset):
    for object in queryset: # pragma: no cover
        object.title = f"Товар {object.id}" # pragma: no cover
        object.save() # pragma: no cover

@admin.action(description='Рандомизирует цену у выбраннныъ записей')
def randomize_price(modeladmin, request, queryset):
    import random # pragma: no cover
    for object in queryset: # pragma: no cover
        object.price = random.randint(65, 10500) # pragma: no cover
        object.save() # pragma: no cover

admin.site.add_action(duplicate)
admin.site.add_action(set_name_as_id)
admin.site.add_action(randomize_price)
