# from django.urls import path
# from views import index


# app_name = "BookStore"
# urlpatterns = [
#     path("", views.index, name="home-index"),
#     # path("books/create", views.create, name="home-create"),
#     # path("books/store", views.store, name="home-store"),
#     # path("books/<int:id>/edit", views.edit, name="home-edit"),
#     # path("books/<int:id>", views.show, name="home-show"),
#     # path("books/<int:id>/delete", views.destroy, name="home-destroy"),
#     # path("books/<int:id>/update", views.update, name="home-update"),
# ]
from django.urls import path
from .views import *

app_name = 'BookStore'

urlpatterns = [
    path('',  index, name="book-index"),
    path("books/create", create, name="book-create"),
    path("books/store", store, name="book-store"),
    path("books/<int:id>", show, name="book-show"),
    path("books/<int:id>/delete", destroy, name="book-delete"),
    path("books/<int:id>/update", update, name="book-update"),
    path("books/<int:id>/edit", edit, name="book-edit")

]
