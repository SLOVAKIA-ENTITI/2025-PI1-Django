import os
import random
from django.core.management.base import BaseCommand
from django.conf import settings
from kruzky.models import Veduci, Kruzok

class Command(BaseCommand):
    help = 'Načíta dáta zo súborov'

    def handle(self, *args, **kwargs):
        veduci_path = os.path.join(settings.BASE_DIR, 'data', 'veduci.txt')
        kruzky_path = os.path.join(settings.BASE_DIR, 'data', 'kruzky.txt')

        with open(veduci_path, encoding='utf-8') as f:
            for riadok in f:
                cast = riadok.strip().split(';')
                if len(cast) == 2:
                    meno, email = cast
                    Veduci.objects.get_or_create(email=email, defaults={'meno': meno})

        vsetci_veduci = list(Veduci.objects.all())

        with open(kruzky_path, encoding='utf-8') as f:
            for riadok in f:
                cast = riadok.strip().split(';')
                if len(cast) == 3:
                    nazov, den, miestnost = cast
                    veduci = random.choice(vsetci_veduci)
                    Kruzok.objects.get_or_create(
                        nazov=nazov,
                        defaults={'den': den, 'miestnost': miestnost, 'veduci': veduci}
                    )

        self.stdout.write(self.style.SUCCESS('Hotovo!'))