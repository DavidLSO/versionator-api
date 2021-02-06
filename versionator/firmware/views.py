from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import FirmmwareSerializer
from .models import Firmmware


class FirmwareViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    queryset = Firmmware.objects.all()
    serializer_class = FirmmwareSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)
