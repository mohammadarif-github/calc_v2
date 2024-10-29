# from rest_framework import serializers
# from .models import FormulaTemplate, Category

# class FileUploadSerializer(serializers.Serializer):
#     file = serializers.FileField()

#     def validate_file(self, file):
#         # Check file size, type, or other custom conditions here
#         allowed_types = ['csv', 'xls', 'xlsx', 'json']
#         file_type = file.name.split('.')[-1].lower()

#         if file_type not in allowed_types:
#             raise serializers.ValidationError("Unsupported file type. Please upload a CSV, Excel, or JSON file.")
#         return file



# from rest_framework import serializers

# class FileUploadSerializer(serializers.Serializer):
#     file = serializers.FileField()
#     description = serializers.CharField(max_length=255, required=False)


# serializers.py
from rest_framework import serializers

class CSVFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
