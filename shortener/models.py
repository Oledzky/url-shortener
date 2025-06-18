from django.db import models

# Create your models here.
import secrets, string
from django.db import models

# Długość kodu skróconego URL-a
CODE_LEN = 7

# Wykorzystuję litery i cyfry do losowego generowania kodu
ALPHABET = string.ascii_letters + string.digits


# Funkcja generująca unikalny kod
def gen_code():
    return ''.join(secrets.choice(ALPHABET) for i in range(CODE_LEN))


class ShortURL(models.Model):
    # Pełny URL do skrócenia
    original_url = models.URLField()

    # Wygenerowany unikalny kod
    code = models.CharField(max_length=CODE_LEN, unique=True, default=gen_code)

    # Data utworzenia wpisu (np. do ustawienia wygasania)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} + {self.original_url}'
