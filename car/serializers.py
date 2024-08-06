from rest_framework import serializers
from car.models import Logo, Car, Contract, Slider, Contractsub


class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['title', 'description', 'image', 'order', 'create', 'update']


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['title', 'description', 'filed_km', 'year', 'price', 'logo', 'color', 'image', 'order',
                  'create', 'update']


class ContractSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['car', 'create', 'update']

class ContractsubPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractsub
        fields = ['id', 'inital_payment', 'month', 'year', ]


class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['title', 'description', 'image', 'order', 'create', 'update']




