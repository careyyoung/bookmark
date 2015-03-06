# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import bookmarks1,sale_orders1,citys1,Note
from forms import NoteForm

# Register your models here.
# So you can see this model in admin page
#admin.site.register(model_name)
admin.site.register(bookmarks1)
admin.site.register(sale_orders1)
admin.site.register(citys1)

class NoteAdmin(admin.ModelAdmin):
    form = NoteForm
admin.site.register(Note, NoteAdmin)
