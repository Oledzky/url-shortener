import pytest

from shortener.models import ShortURL
from shortener.serializers import ShortenSerializer, ExpandSerializer


# Sprawdza, czy serializer akceptuje poprawny adres URL
@pytest.mark.django_db
def test_shorten_serializer_valid():
    data = {'original_url': 'https://example.com'}
    serializer = ShortenSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['original_url'] == 'https://example.com'


# Sprawdza, czy serializer odrzuca brakujący adres URL
@pytest.mark.django_db
def test_shorten_serializer_invalid_missing_url():
    data = {}
    serializer = ShortenSerializer(data=data)
    assert not serializer.is_valid()
    assert 'original_url' in serializer.errors


# Sprawdza, czy serializer odrzuca niepoprawny format adresu URL
@pytest.mark.django_db
def test_shorten_serializer_invalid_url_format():
    data = {'original_url': 'not-a-url'}
    serializer = ShortenSerializer(data=data)
    assert not serializer.is_valid()
    assert 'original_url' in serializer.errors


# Sprawdza, czy serializer poprawnie zwraca wszystkie pola dla jednego obiektu
@pytest.mark.django_db
def test_expand_serializer_output_fields():
    obj = ShortURL.objects.create(original_url='https://example.com', code='abc123')
    serializer = ExpandSerializer(obj)
    data = serializer.data
    assert data['original_url'] == 'https://example.com'
    assert data['code'] == 'abc123'
    assert 'created_at' in data


# Sprawdza, czy serializer poprawnie serializuje listę obiektów
@pytest.mark.django_db
def test_expand_serializer_multiple_objects():
    obj1 = ShortURL.objects.create(original_url='https://a.com', code='a1')
    obj2 = ShortURL.objects.create(original_url='https://b.com', code='b2')
    serializer = ExpandSerializer([obj1, obj2], many=True)
    data = serializer.data
    assert len(data) == 2
    assert data[0]['original_url'] == 'https://a.com'
    assert data[1]['code'] == 'b2'


# Sprawdza, czy serializer zapisuje nowy obiekt w bazie danych
@pytest.mark.django_db
def test_shorten_serializer_save_creates_instance():
    data = {'original_url': 'https://save.com'}
    serializer = ShortenSerializer(data=data)
    assert serializer.is_valid()
    instance = serializer.save(code='unique123')
    assert isinstance(instance, ShortURL)
    assert instance.original_url == 'https://save.com'
    assert instance.code == 'unique123'
