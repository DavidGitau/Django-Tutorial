from django.urls import path, include
from .views import (
    home_view, get_name, redirect1, 
    thanks, create_person, fav, entry
)


app_name = 'tut'
urlpatterns = [
    path('', home_view, name='home'),
    path('cviews/', include('cviews.urls')),
    path('name/', get_name, name='name'),
    path('thanks/', thanks, name='thanks'),
    path('person', create_person, name='person'),
    path('redirect1/', redirect1),
    path('fav/', fav, name='fav'),
    path('entry/', entry, name='entry')
]