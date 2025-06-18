# 🔗 Minimal URL Shortener API (Django REST Framework)

Ten projekt to **minimalistyczny backendowy skracacz URL-i** oparty na Django REST Framework.  
Pozwala na szybkie tworzenie skróconych linków oraz przekierowywanie użytkowników na oryginalne adresy.

---

## ✅ Funkcjonalności

- 🔧 **Tworzenie skróconych URL-i** – `POST /shorten`
- ↪️ **Przekierowanie na oryginalny URL** – `GET /<code>`
- 🔍 **Rozszyfrowanie skrótu przez API** – `GET /expand/<code>`

---

## 🧰 Wymagania

- Python 3.8+
- Django 4.x
- Django REST Framework

Instalacja zależności:

```bash
pip install django djangorestframework
```

---

## 🚀 Uruchomienie projektu

```bash
python manage.py migrate        # Wykonaj migracje bazy danych
python manage.py runserver     # Uruchom lokalny serwer
```

Domyślnie aplikacja będzie dostępna pod adresem:  
`http://localhost:8000/`

---

## 🧪 Testowanie API

### 1. Tworzenie skróconego URL-a

#### `POST /shorten`

```bash
http POST :8000/shorten original_url=http://example.com/very/long/url
```

**Przykładowa odpowiedź:**

```json
{
  "short_url": "http://localhost:8000/EXOYm4V"
}
```

---

### 2. Przekierowanie na oryginalny adres

#### `GET /<code>`

Po uzyskaniu kodu (np. `EXOYm4V`), odwiedź:

```bash
http GET :8000/EXOYm4V
```

Lub bezpośrednio w przeglądarce:  
`http://localhost:8000/EXOYm4V`

To żądanie przekieruje użytkownika na oryginalny URL.

---

### 3. Odczytanie oryginalnego URL-a przez API

#### `GET /expand/<code>`

```bash
http GET :8000/expand/EXOYm4V
```

**Przykładowa odpowiedź:**

```json
{
  "original_url": "http://example.com/very/long/url"
}
```

---

### Instalacja `httpie`

```bash
pip install httpie      
```