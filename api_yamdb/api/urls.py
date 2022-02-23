from django.urls import include, path
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'titles', views.TitleViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'users/me', views.UsersMeView, basename='me')
router.register(r'titles/(?P<title_id>\d+)/reviews', views.ReviewViewSet,
                basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments')

urlpatterns = [
    path('auth/signup/', views.SignUpUserView.as_view()),
    path('auth/token/', views.CreateUserToken.as_view()),
    path('users/me/', views.UsersMeView.as_view(
        {'get': 'list', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('', include(router.urls)),
]
