from django.urls import path, include

import demo.views

urlpatterns = [
    path('hello_world', demo.views.hello_world),
    path('index', demo.views.index)
]