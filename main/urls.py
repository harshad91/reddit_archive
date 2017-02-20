from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'(?P<year>\d{4})/(?P<subreddit>\w+)/$',
        views.subreddit_home,
        name='home'
    )
]
