from django.contrib import admin
from django.urls import path
from Book import views
urlpatterns = [
    path('books',views.allbook),
    path('addnew',views.newbook),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete)
]
