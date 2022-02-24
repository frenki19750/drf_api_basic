from django.urls import path, include
from .views import articale_list, articale_detail, ArticaleAPIView, ArticaleDetails, GenericAPIView, ArticaleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articale', ArticaleViewSet, basename='articale')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    #path('articale/', articale_list),
    path('articale/', ArticaleAPIView.as_view()),
    # path('detail/<int:pk>', articale_detail),
    path('detail/<int:id>/', ArticaleDetails.as_view()),
    path('generic/articale/<int:id>/', GenericAPIView.as_view()),
    ]