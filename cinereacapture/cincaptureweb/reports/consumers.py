from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        #self.user = self.scope['user']
        self.GROUP_NAME = 'user-notifications'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def user_joined(self, event):
        html = get_template("reports/partial/sales_transactions.html").render(
            context={
                "username": event["text"],
                'servTrans': event["servTrans"],
                'total_transactions': 12
            }
        )
        self.send(text_data=html)
