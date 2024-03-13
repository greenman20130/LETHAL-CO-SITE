from django.apps import AppConfig


class NewslineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsline'

    def ready(self) -> None:
        import newsline.signals
