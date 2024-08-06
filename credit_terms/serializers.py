from rest_framework import serializers
from credit_terms.models import Credit_terms


class Credit_termsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Credit_terms
        fields = ['title', 'description', 'file', 'create', 'update']
