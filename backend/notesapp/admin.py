from django.contrib import admin
from .models import Note, Folder

class NotesAppAdmin(admin.ModelAdmin):
  list = ('title', 'text')

myModels = [Note, Folder]
admin.site.register(myModels)
# admin.site.register(Note, NotesAppAdmin)