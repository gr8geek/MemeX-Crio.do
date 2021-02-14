from django.urls import path
from .views import handle_api,handle_id

urlpatterns = [
    path('',handle_api),
    path('/<int:id>',handle_id)
]

