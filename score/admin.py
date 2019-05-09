from django.contrib import admin
from .models import game
from .models import result

admin.site.register(game)
admin.site.register(result)