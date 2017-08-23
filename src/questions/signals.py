from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Answer, SendNotification


@receiver(post_save, sender=Answer)
def send_notification(created, sender, instance, *args, **kwargs):
    if created:
        question = instance.question
        if instance.user == question.user:
            pass
        else:
            from_user = instance.user
            user = question.user
            notification = SendNotification.objects.create(user=user, 
                                                           from_user=from_user, 
                                                           question=question, 
                                                           message="You Have an Answer!")
