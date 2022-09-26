"""
"""

from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from hangry_app.models import HangryPerson


class HangryPersonSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = HangryPerson
        fields = '__all__'


class HangryPersonViewSet(viewsets.ModelViewSet):
    """"""

    model = HangryPerson
    queryset = model.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HangryPersonSerializer
