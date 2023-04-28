from django.urls import path
from . import views
from rest_framework import routers
from .views import UserViewSet
routes = routers.DefaultRouter()

# routes.register('monthlycontribution', MonthlyContributionViewSet)
# routes.register('merrygoroundcontribution', MonthlyContributionViewSet)
# routes.register('api/redflags', RedFlagViewSet)
# routes.register('api/interventions', InterventionViewSet)
routes.register('api/users', UserViewSet)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('api/admin',views.AdminSignUpView.as_view()),
    path('api/client',views.ClientSignUpView.as_view()),
    path('api/token',views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]
urlpatterns += routes.urls