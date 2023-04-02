from rest_framework import serializers

from api.models import Company, Employee

# create serailizers here

class CompanySerializer(serializers.ModelSerializer):
    company_id=serializers.ReadOnlyField()

    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    id= serializers.ReadOnlyField()

    class Meta:
        model= Employee
        field="__all__"


