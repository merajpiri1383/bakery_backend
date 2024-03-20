from django.db.models.signals import post_save
from django.contrib.auth import get_user_model 
from django.dispatch import receiver
from threading import Thread
from time import sleep
def delete_user_async(instance,created): 
    sleep(60)
    if created : 
        try : 
            user = get_user_model().objects.get(email=instance.email)
            if not user.is_active : 
                user.delete()
        except : pass
@receiver(signal=post_save,sender=get_user_model())
def delete_user(sender,instance,created,**kwargs):
    """
    delete inactive user after 120s of registeration 
    """ 
    task = Thread(target=delete_user_async,args=[instance,created])
    task.start()