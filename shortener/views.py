# Create your views here.

from django.http import Http404
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response

from .models import ShortURL
from .serializers import ShortenSerializer, ExpandSerializer


# Widok tworzący skrócony URL (POST/ /shorten)
class ShortenView(generics.CreateAPIView):
    serializer_class = ShortenSerializer

    # Naspisanie metody create, aby zwrócić pełny skrócony URL
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Zapis nowego obiektu
        short = serializer.save()
        # Tworzymy pełny URL na podstawie hosta
        host = request.build_absolute_uri('/')[:-1]

        return Response(
            {
                'short_url': f'{host}/{short.code}',
                'code': short.code,
            },
            status=status.HTTP_201_CREATED,
        )


# Widok pozwalający rozszyfrować skrócony kod (GET/expand/<code>)
class ExpandView(generics.RetrieveAPIView):
    lookup_field = 'code'  # Szukanie po polu 'code'
    queryset = ShortURL.objects.all()
    serializer_class = ExpandSerializer


# Widok do przekierowania użytkowania na oryginalny adres (GET /<code>)
def redirect_view(request, code):
    try:
        # Pobieranie odpowiedniego obiektu z bazy
        link = ShortURL.objects.get(code=code)
    except ShortURL.DoesNotExist:
        # Jeśli nie istnieje - wyrzucamy 404
        raise Http404('Unknown shorten code')

    # Przekieruj użytkownika na oryginalny URL (HTTP 302)
    return redirect(link.original_url, permanent=False)
