from rest_framework import routers
from articles import views as article_views
from blog import views as blog_views

router = routers.DefaultRouter()
router.register(r"articles", article_views.ArticleViewSet)
router.register(r"blog", blog_views.BlogViewSet)
