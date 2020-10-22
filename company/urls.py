from django.urls import path
from company.viewsets import CompanyViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'company', CompanyViewSet)
urlpatterns = router.urls
