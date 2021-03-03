from account.decorators import super_admin_required
from utils.api import APIView, validate_serializer

from article.models import Article
from article.serializers import (ArticleSerializer, CreateArticleSerializer,
                                      EditArticleSerializer)


class ArticleAdminAPI(APIView):
    @validate_serializer(CreateArticleSerializer)
    @super_admin_required
    def post(self, request):
        """
        publish announcement
        """
        data = request.data
        announcement = Article.objects.create(title=data["title"],
                                                   content=data["content"],
                                                   created_by=request.user,
                                                   visible=data["visible"])
        return self.success(ArticleSerializer(announcement).data)

    @validate_serializer(EditArticleSerializer)
    @super_admin_required
    def put(self, request):
        """
        edit announcement
        """
        data = request.data
        try:
            announcement = Article.objects.get(id=data.pop("id"))
        except Article.DoesNotExist:
            return self.error("Article does not exist")

        # * 可以直接把屬性設置完
        for k, v in data.items():
            setattr(announcement, k, v)
        announcement.save()

        return self.success(ArticleSerializer(announcement).data)

    @super_admin_required
    def get(self, request):
        """
        get announcement list / get one announcement
        """
        announcement_id = request.GET.get("id")
        if announcement_id:
            try:
                announcement = Article.objects.get(id=announcement_id)
                return self.success(ArticleSerializer(announcement).data)
            except Article.DoesNotExist:
                return self.error("Article does not exist")
        announcement = Article.objects.all().order_by("-create_time")
        if request.GET.get("visible") == "true":
            announcement = announcement.filter(visible=True)
        return self.success(self.paginate_data(request, announcement, ArticleSerializer))

    @super_admin_required
    def delete(self, request):
        if request.GET.get("id"):
            Article.objects.filter(id=request.GET["id"]).delete()
        return self.success()
