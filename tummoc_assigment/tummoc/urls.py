from django.urls import path
from .views_auth import RegisterView, LoginView
from .movie_views import CollectionAPIView, MoviesAPIView
from .middleware import RequestCountAPIView, RequestCountResetAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('collection/', CollectionAPIView.as_view()),
    path('collection/<uuid:collection_uuid>/', CollectionAPIView.as_view()),
    path('request-count/', RequestCountAPIView.as_view()),
    path('request-count/reset/', RequestCountResetAPIView.as_view()),
    path('movies/', MoviesAPIView.as_view()),

]
