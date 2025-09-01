from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    DoctorViewSet,
    MappingViewSet,
    RegisterView,
    MyTokenObtainPairView,
    AppointmentListCreateView,
    AppointmentDetailView,
)
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # router endpoints
    path('', include(router.urls)),

    # mappings
    path('mappings/', MappingViewSet.as_view({'get': 'list', 'post': 'create'}), name='mappings-list-create'),
    path('mappings/<int:pk>/', MappingViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='mappings-detail'),

    # appointments
    path('appointments/', AppointmentListCreateView.as_view(), name='appointments-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointments-detail'),
]
