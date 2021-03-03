from django.conf.urls import url

from ..views.admin import ArticleAdminAPI

urlpatterns = [
    url(r"^article/?$", ArticleAdminAPI.as_view(), name="announcement_admin_api"),
]
