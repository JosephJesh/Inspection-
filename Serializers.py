from rest_framework import serializers
from Inspection.models import Details

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields =[
            'name',
            'Email_id',
        ]