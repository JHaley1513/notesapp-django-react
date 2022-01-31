from django.db import models
# from django.utils import timezone
# can also use "default=timezone.now()" for DateTimeFields

class Note(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)   # auto-sets when object is created
    modified = models.DateTimeField(auto_now=True)   # auto-sets every time object is saved
    starred = models.BooleanField(default=False)
    # if deleted, put in "recently deleted" to be deleted after some time passes (or manually)
    deleted = models.BooleanField(default=False)
    
    def _str_(self):
        return self.title