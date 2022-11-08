from django.urls import path
from studio import views

urlpatterns = [
    path('work', views.index, name = "work"),
    path('about', views.about, name = "about"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name = 'contact')

    # path('work', views.work, name = "work"),
 ]