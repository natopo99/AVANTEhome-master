from django.urls import path 
from .views import indexPageView, homeListingsView, addListingView, deleteListingView, editListingView, editListing
from .views import searchListing, viewListingView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('listings/', homeListingsView, name = 'listings'),
    path('addlisting/', addListingView, name = 'addListing'),
    path('deletelisting/<int:house_id>/', deleteListingView, name = 'deleteListing'),
    path('editlisting/<int:house_id>/', editListingView, name = 'editListingView'),   
    path('editlisting/', editListing, name = 'editListing'),  
    path('searchlistings/', searchListing, name = 'searchListing'),   
    path('viewSingleListing/<int:house_id>/', viewListingView, name = 'viewListingView'),   

]
