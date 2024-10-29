from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy
from .views import export_users_csv, export_users_pdf
urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
        path('users/export/csv/', export_users_csv, name='export-users-csv'),
    path('users/export/pdf/', export_users_pdf, name='export-users-pdf'),


]
