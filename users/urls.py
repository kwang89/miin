from django.urls import path

from . import views


'''
    example)
    user_list.html : {% url 'users:user-detail' question.id %}
    위 url 맵핑을 참조
'''

app_name = 'users'  # url namespace

urlpatterns = [
    path('', views.ListView.as_view(), name='user-list'),  # name : path mapping 가능
    path('details/<int:pk>/', views.DetailView.as_view(), name='user-detail'),  # name : path mapping 가능
    # path('', views.user_list)
]