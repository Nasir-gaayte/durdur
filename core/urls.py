from django.urls import path 
from .views import( home,
                   service,
                   addCards,
                   cardDetail,
                   city,
                   about,
                   )


urlpatterns = [
    path('',home,name='home'),
    path('service/',service,name='service'),
    path('city/',city,name='city'),
    path('about/',about,name='about'),
    path('add_card/',addCards,name='add_card'),
    path('card_detail/<str:pk>/',cardDetail,name='card_detail'),
]
