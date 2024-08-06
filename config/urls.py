from django.contrib import admin
from django.urls import path, include
#
# from users.views import RegisterView
# from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/api/', include('about.urls')),
    path('car/api/', include('car.urls')),
    path('credit_terms/api/', include('credit_terms.urls')),
    path('users/api/', include('users.urls')),
    ]
#
#     path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', RegisterView.as_view(), name='auth_register'),
# ]
