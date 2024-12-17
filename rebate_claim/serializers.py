from rest_framework import serializers
from .models import RebateClaim


class RebateClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = RebateClaim
        fields = '__all__'
        read_only = ('claim_date', 'updated_at')
