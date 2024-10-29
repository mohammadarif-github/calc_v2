from django.urls import path
from .views import CSVFileUploadAPIView

urlpatterns = [
    path('api/upload/', CSVFileUploadAPIView.as_view(), name='file-upload'),
]
# {
#     "name": "File Upload Api",
#     "description": "",
#     "renders": [
#         "application/json",
#         "text/html"
#     ],
#     "parses": [
#         "multipart/form-data",
#         "application/x-www-form-urlencoded"
#     ]
# }