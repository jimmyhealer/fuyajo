from utils.api import APIView

from article.models import Article
from article.serializers import ArticleSerializer


class ArticleAdminAPI(APIView):
    def get(self, request):
        announcements = Article.objects.filter(visible=True)
        return self.success(self.paginate_data(request, announcements, ArticleSerializer))
