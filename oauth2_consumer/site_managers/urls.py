from rest_framework import routers
from oauth2_consumer.site_managers import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet)
router.register(r'social_apps', views.SocialAppViewSet)

urlpatterns = router.urls
