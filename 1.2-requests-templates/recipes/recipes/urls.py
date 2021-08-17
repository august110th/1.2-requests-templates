from django.urls import path
from calculator.views import pasta_view, omlet_view, buter_view, home_view

urlpatterns = [
    path('pasta/', pasta_view, name='pasta'),
    path('omlet/', omlet_view, name='omlet'),
    path('buter/', buter_view, name='buter'),
    path('', home_view, name='home')

]