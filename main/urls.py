from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('<str:post_id>/update_comment/<str:comment_id>', update_comment, name="update_comment"),
    path('<str:post_id>/delete_comment/<str:comment_id>', delete_comment, name="delete_comment"),
    path('<str:post_id>/edit_comment/<str:comment_id>', edit_comment, name="edit_comment"),

    path('like_toggle/<int:post_id>', like_toggle, name="like_toggle"),
    path('my_like/<int:user_id>', my_like, name="my_like"),
    path('dislike_toggle/<int:post_id>', dislike_toggle, name="dislike_toggle"),
    path('my_dislike/<int:user_id>', my_dislike, name="my_dislike"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)