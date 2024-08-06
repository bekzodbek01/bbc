from rest_framework import serializers
from about.models import About, News, Contact, Connection


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'description', 'image', 'create', 'update']


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'phone', 'description', 'image', 'create', 'update']


class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['title', 'longitude', 'latitude', 'create', 'update']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone', 'email', 'telegram', 'instagram', 'facebook', 'create', 'update']
