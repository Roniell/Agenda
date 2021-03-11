from core.models import Agenda

from rest_framework import serializers


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
