from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('filter_tiems/',ItemFilterView.as_view(),name = 'filter_tiems'),
   ]