from rest_framework import views
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from company.models import Company
from company.serializers import CompanySerializer
from django.db.transaction import atomic


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    # TODO Allow only one company to be created

    def list(self, request, *args, **kwargs):
        company_instance = Company.get_company()
        if company_instance is None:
            return super().list(request, *args, **kwargs)
        else:
            serializer = self.serializer_class(company_instance)
            return Response(serializer.data)
