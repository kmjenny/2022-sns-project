from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('show', show_page, name="showpage"),
    path('<int:id>', detail,name="detail"),
    path('new/',new,name="new"),
    path('create/', create,name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('update_comment/<str:id>', update_comment, name="update_comment"),
    path('delete_comment/<str:id>', delete_comment, name="delete_comment"),
    path('edit_comment/<str:id>', edit_comment, name="edit_comment"),
]
