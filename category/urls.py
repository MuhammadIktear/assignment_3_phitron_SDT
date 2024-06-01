from django.urls import path
from .import views

urlpatterns=[
    path('add/',views.add_category,name='add_category'),
    path('view/<int:id>',views.view_category,name='view_category'),
    path('delete/<int:id>',views.delete_category,name='delete_category'),
]