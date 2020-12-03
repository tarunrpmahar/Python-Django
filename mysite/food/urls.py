#this is url.py file of food app

from django.urls import path
from . import views

app_name= 'food'   #namespace if there are other app with same name='detail' so django get confuse which detail to select
urlpatterns = [

    #delete item
    path('delete/<int:id>', views.delete_item, name='delete_item'),

    #edit item
    path('update/<int:id>', views.update_item, name='update_item'),

    # add items   /foodie/add
    path('add/', views.create_item, name='create_item'),

    #/foodie
    path('', views.index, name='index'),
    #path('hello/', views.index, name='index'),

    #/foodie/detail/id
    #path('detail/<int:item_id>/', views.detail, name='detail'),

    # /foodie/id
    path('<int:item_id>/', views.detail, name='detail'),
    
    #/foodie/football/
    path('football/', views.football, name='football'),
]
