from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializers
from .permissions import IsHouseManagerOrNot

class HouseViewSet(viewsets.ModelViewSet):
    queryset=House.objects.all()
    serializer_class=HouseSerializers
    permission_classes=[IsHouseManagerOrNot, ]