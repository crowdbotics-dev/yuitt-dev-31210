from rest_framework import authentication
from users.models import Hjjfjf
from .serializers import HjjfjfSerializer
from rest_framework import viewsets


class HjjfjfViewSet(viewsets.ModelViewSet):
    serializer_class = HjjfjfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hjjfjf.objects.all()
