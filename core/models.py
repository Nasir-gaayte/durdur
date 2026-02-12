from django.db import models

import os

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver


class CardMolel(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    img = models.ImageField(null=True,blank=True,upload_to='img')
    head_line= models.TextField()
    body = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    
    

@receiver(models.signals.post_delete, sender=CardMolel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)
         
         
            

@receiver(models.signals.pre_save, sender=CardMolel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file =CardMolel.objects.get(pk=instance.pk).img
       
    except CardMolel.DoesNotExist:
        return False

    new_file = instance.img
  
    if not old_file == new_file  :
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
        else:
            os.path.isfile(old_file.path) == 0
            return None     
    
    
