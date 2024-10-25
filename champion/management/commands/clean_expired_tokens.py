# management/commands/clean_expired_tokens.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from champion.models import VideoAccessToken

class Command(BaseCommand):
    help = 'Deletes expired video access tokens'

    def handle(self, *args, **kwargs):
        VideoAccessToken.objects.filter(expires_at__lt=timezone.now()).delete()
        self.stdout.write("Expired tokens deleted.")
