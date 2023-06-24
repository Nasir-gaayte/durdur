from django.urls import path 
from .views import( home,
                   service,
                   addCards,
                   cardDetail,
                   )


urlpatterns = [
    path('',home,name='home'),
    path('service/',service,name='service'),
    path('add_card/',addCards,name='add_card'),
    path('card_detail/<str:pk>/',cardDetail,name='card_detail'),
]
