from rest_framework import serializers
from .models import RebateProgram


class RebateProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = RebateProgram
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
