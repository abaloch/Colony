from django.apps import AppConfig


class MicroblogConfig(AppConfig):
    name = 'microblog'


    def ready(self):
        import users.signals
