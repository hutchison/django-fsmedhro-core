from django.urls import path
from . import views

app_name = 'fsmedhro_core'

urlpatterns = [
    path('edit/', views.FachschaftUserEdit.as_view(), name='edit'),
    path('', views.FachschaftUserDetail.as_view(), name='detail'),
    # path('user/<int:user_id>', views.user_profile, name='user_profile'),
    # path('user', views.user_self, name='user_self'),
]
