from django.db import models

# Create your models here.
class Editor(models.Model):
    '''
    Class that defines an Editor for an article
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        # return ' %s' %  (self.first_name)
        return self.first_name

    class Meta:
        ordering = ['first_name']
