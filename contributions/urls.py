from .views import getMonthlyContribution, getMonthlyContributionDetails, getMerryGoRoundContribution, getMerryGoRoundContributionDetails
from rest_framework.routers import DefaultRouter
from django.urls import path



routes = DefaultRouter()

# routes.register('monthlycontribution', getMonthlyContribution)
# routes.register('merrygoroundcontribution', getMerryGoRoundContribution)

urlpatterns = [
    path('monthlycontribution/',getMonthlyContribution,name='monthlycontribution'),
    path('monthlycontribution/<int:id>', getMonthlyContributionDetails,name='monthlycontributionDetails'),
    path('merrygoroundcontribution/',getMerryGoRoundContribution,name='merryGoRoundcontribution'),
    path('merrygoroundcontribution/<int:id>', getMerryGoRoundContributionDetails,name='merryGoRoundcontributionDetails'),
]

urlpatterns += routes.urls
