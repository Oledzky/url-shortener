# Minimal URL Shortener API (Django REST Framework)

Ten projekt to **prosty backendowy skracacz URL-i**, zbudowany na Django REST Framework.  
Pozwala w ekstremalnie minimalistyczny sposób tworzyć skrócone linki oraz przekierowywać użytkowników na oryginalne adresy.

---

## Funkcjonalności

- [x] Tworzenie skróconych URL-i (`POST /shorten`)
- [x] Przekierowanie na oryginalny URL (`GET /<code>`)
- [x] Rozszyfrowanie kodu przez API (`GET /expand/<code>`)

---

## Wymagania

- Python 3.8+
- Django 4+
- Django REST Framework

Instalacja zależności:
```bash
pip install django djangorestframework
