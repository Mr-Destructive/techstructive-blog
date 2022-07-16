from rest_framework import routers
from articles import views as article_views

router = routers.DefaultRouter()
router.register(r'blog', article_views.ArticleViewSet)
