from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=40)
    parent = None   # doing `parent = Folder()` results in `name not defined`

    def _str_(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField() # not initialized yet
    parent = Folder()

    def _str_(self):
        return self.title