from django.contrib import admin

from .models import User
from .models import Coords, Image, Pereval, Level

admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Image)
admin.site.register(Pereval)
admin.site.register(Level)
