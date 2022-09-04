from . import views
from django.urls import path
from .views import SignUpView
from .views import contact
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/', contact , name='post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]