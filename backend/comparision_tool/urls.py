from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import GoogleDataSetView, SavedQueriesView, CommentsView, CustomUserView
router = routers.DefaultRouter()
router.register(r'google_data_set', GoogleDataSetView, 'google_data_set')
router.register(r'saved_queries', SavedQueriesView, 'saved_queries')
router.register(r'comments', CommentsView, 'comments')
router.register(r'custom_user', CustomUserView, 'custom_user')
urlpatterns = [
  path('api/v1/', include(router.urls)) ,
  path('docs/', include_docs_urls(title="comparision tool api"))
]