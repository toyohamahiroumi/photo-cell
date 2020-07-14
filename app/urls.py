from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'app'
urlpatterns = [
    path('', login_required(views.Index.as_view()), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('photos_form/', login_required(views.PhotoCreate.as_view()),
         name='photos_form'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ユーザー詳細画面へのパスを追記
    path('<username>/', views.UserDetailView.as_view(template_name='app/user_detail.html'),
         name='userdetail'),
    path('icon/edit/', views.IconEdit.as_view(), name='icon_edit'),
    # path('photos_list/', PhotoList.as_view(), name='photos_list'),

]
