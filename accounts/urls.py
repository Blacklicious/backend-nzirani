from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# auth views
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'raw-contacts', views.RawContactViewSet)
router.register(r'leads', views.LeadViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path("api/register/", RegisterView.as_view(), name="rest_register"),
    #path("api/login/", LoginView.as_view(), name="rest_login"),
    path("api/logout/", LogoutView.as_view(), name="rest_logout"),
    path("api/user/", UserDetailsView.as_view(), name="rest_user_details"),
    #path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
   # path("api/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),

    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/current-user/', views.CurrentUserView.as_view(), name='current-user'),
    path('api/add-contact/', views.AddContactView.as_view(), name='add_contact'),
]
