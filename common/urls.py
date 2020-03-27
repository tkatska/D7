from common.views import index, RegisterView, CreateUserProfile  
from django.urls import path
from django.urls import reverse_lazy
from allauth.account.views import login, logout

app_name = 'common'  
urlpatterns = [  
    path('', index, name='index'),  
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url=reverse_lazy('common:profile-create')  
    ), name='register'),  
  path('profile-create/', CreateUserProfile.as_view(), name='profile-create'), 
]