from django.urls import path
from . import views


urlpatterns = [
    # 'name=' will be used to go to point to that given URL in any html files
    
    # any post's URL will be like: :8000/python(category)/classes-python(the slug)
    path('<slug:category_slug>/<slug:slug>',views.details,name='post_details'),
    # all same post category will be here :8000/python
    path('<slug:slug>/',views.category,name='category_details'),
]
