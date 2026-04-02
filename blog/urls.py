from django.urls import path
from .views import CommentRetrieveUpdateDeleteView, CategoryRetrieveUpdateDeleteView, PostRetrieveUpdateDeleteView, CategoryView, PostView, CommentView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category-view'),
    path('comment/', CommentView.as_view(), name='comment-view'),
    path('post/', PostView.as_view(), name='post-view'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'), 
    path('comment/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-retrieve-update-delete'), 
    path('post/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'), 
]