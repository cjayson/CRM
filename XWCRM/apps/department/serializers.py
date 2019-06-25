from rest_framework.serializers import ModelSerializer
from .models import Department


class DepartmentModelSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ["name","desc"]