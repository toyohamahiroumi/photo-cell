from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PhotoCreate, SignUpView, UserDetailView

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('photos_form/', PhotoCreate.as_view(), name='photos_form'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ユーザー詳細画面へのパスを追記
    path('<username>/', UserDetailView.as_view(template_name='app/user_detail.html'),
         name='userdetail'),
    path('icon/edit/', views.IconEdit.as_view(), name='icon_edit'),
]
