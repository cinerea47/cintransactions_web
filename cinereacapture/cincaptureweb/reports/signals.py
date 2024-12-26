from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from reports.models import ServiceTransactions, ExpenseTransactions

from account.models import Account




@receiver(post_save, sender=ServiceTransactions)
def sales_created(sender, instance, **kwargs):
    print("Add user katwishi")
    print(instance.user.firstname)
    servTrans = ServiceTransactions.objects.all()
    channel_layer = get_channel_layer()
    group_name = 'user-notifications'
    event = {
        "type": "user_joined",
        "text": instance.transactionID,
        "servTrans": servTrans,
    }
    async_to_sync(channel_layer.group_send)(group_name, event)


@receiver(post_save, sender=ExpenseTransactions)
def expenses_created(sender, instance, **kwargs):
    print("Add user katwishi")
    print(instance.user.firstname)




