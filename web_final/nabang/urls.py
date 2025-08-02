
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import check_username
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import delete_account, find_user_info,find_user_info_pw
from social_django import views as social_views

def index(request):
    return render(request,'index.html')

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('airecommend/', views.airecommend, name='airecommend'),
    path('file-upload/', views.file_upload, name='file_upload'),
    path('path-to-image-upload-handler', views.image_upload_handler, name='image-upload-handler'),
    path('airecommend_result/', views.airecommend_result, name='airecommend_result'),
    path('airemodeling/', views.airemodeling, name='airemodeling'),
    path('airemodeling_result/', views.airemodeling_result2, name='airemodeling_result'),
    path('path-to-image_change_handler', views.image_change_handler, name='image_change_handler'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),
    path('personaldata/', views.personal_data, name='personal_data'),
    path('terms/', views.terms_of_service, name='terms_of_service'),
    path("password_change/", views.MyPasswordChangeView.as_view(), name="password_change"),
    path('delete_account/', delete_account, name='delete_account'),
    path('find_user_info/', find_user_info, name='find_user_info'),
    path('find_user_info_pw/', find_user_info_pw, name='find_user_info_pw'),
    path('board/', include('board.urls')),
    path('common/', include('common.urls')),
    path('accounts/', include('allauth.urls')),
    path('rule/', views.rule, name='rule'),
    path('check_username/', views.check_username, name='check_username'),  # 아이디 중복 확인 UR
    path('oauth/', include('social_django.urls', namespace='kakao')),  # <--
    path('login/kakao/', social_views.auth, name='kakao-login', kwargs={'backend': 'kakao'}),  # 
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accounts/kakao/login/callback/', views.kakao_login, name='custom_kakao'), # custom kakaotalk loginL
    path('airemodeling/', views.airemodeling, name='airemodeling'),
    path('airemodeling_result/', views.airemodeling_result, name='airemodeling_result'),
    path('color_analysis_api', views.color_analysis_api, name='color_analysis_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
