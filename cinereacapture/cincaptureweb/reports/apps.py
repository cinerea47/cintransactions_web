from django.apps import AppConfig


class ReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reports'

    def ready(self):
        """https://docs.djangoproject.com/en/4.1/topics/signals/"""
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
