from django.conf.urls import url

from ..views.oj import ArticleAdminAPI

urlpatterns = [
    url(r"^article/?$", ArticleAdminAPI.as_view(), name="announcement_api"),
]
