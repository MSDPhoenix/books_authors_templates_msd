from django.urls import path
from . import views

urlpatterns = [
    path('',views.books_page),
    path('add_book',views.add_book),
    path('view_book/<int:book_id>',views.view_book),
    path('delete_book/<int:book_id>',views.delete_book),
    path('authors',views.authors_page),
    path('add_author',views.add_author),
    path('view_author/<int:author_id>',views.view_author),
    path('delete_author/<int:author_id>',views.delete_author),
    path('add_book_to_author/<int:author_id>',views.add_book_to_author),
    path('book_to_remove_from_author/<int:book_id>/<int:author_id>',views.remove_book_from_author),
    path('add_author_to_book/<int:book_id>',views.add_author_to_book),
    path('remove_author_from_book/<int:book_id>/<int:author_id>',views.remove_author_from_book),
    path('update_book/<int:book_id>',views.update_book),
    path('save_book_update/<int:book_id>',views.save_book_update),
    path('update_author/<int:author_id>',views.update_author),
    path('save_author_update/<int:author_id>',views.save_author_update),
    
]
