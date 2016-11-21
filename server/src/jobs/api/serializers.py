from rest_framework.serializers import (
    ModelSerializer,
    )

from jobs.models import Job


class JobListSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'daily_rate',
        ]