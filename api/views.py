from django.shortcuts import render
from api.models import Mascota
from rest_framework import viewsets, mixins
from api.serializers import MascotaSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass

class MascotaViewSet(CreateListRetrieveViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer