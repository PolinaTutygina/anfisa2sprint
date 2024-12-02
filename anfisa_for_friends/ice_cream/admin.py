from django.contrib import admin

# Register your models here.
# Из модуля models импортируем модель Category...
from .models import Category
from .models import Topping
from .models import Wrapper
from .models import IceCream

# ...и регистрируем её в админке:
admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream)