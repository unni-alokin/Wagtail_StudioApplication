from django.urls import path
from studio import views

urlpatterns = [
    path('work', views.index, name = "work"),
    path('about', views.about, name = "about"),
    path('blogs', views.blog, name="blogs"),

    # path('work', views.work, name = "work"),
 ]