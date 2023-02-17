from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('todolist/', views.todolist_view, name='todolist'),
    path('add', views.add_view, name='add'),
    path('inform/<int:pk>', views.info_view, name='inform'),
]