from app import views
from django.urls import path,include


urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('register/',views.register,name="register"),
    path('crypto_home/',views.crypto_home,name="crypto_home"),
    path('prices/',views.prices,name="prices"),
    path('tic_tac/',views.tic_tac,name="tic_tac"),
    path('map/',views.map,name="map"),
]
