from rest_framework import serializers
from company.models import Company
from django.db.transaction import atomic


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name",)

    def save(self, **kwargs):
        Company.save_company()
        return super().save(**kwargs)

    @atomic
    def create(self, validated_data):
        company = Company.get_company()
        company.__dict__.update(validated_data)
        company.save()
        return company
