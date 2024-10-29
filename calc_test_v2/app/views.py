# import csv
# import json
# # import pandas as pd
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.files.storage import default_storage
# from .models import Category, FormulaTemplate
# from rest_framework.decorators import api_view
# from .serializers import FileUploadSerializer
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework import status
# from rest_framework.views import APIView


# def get_file_type(file_name):
#     """Determine the file type based on the file extension."""
#     extension = file_name.split('.')[-1].lower()
#     if extension in ['csv']:
#         return 'csv'
#     elif extension in ['xls', 'xlsx']:
#         return 'excel'
#     elif extension in ['json']:
#         return 'json'
#     else:
#         return None  # Invalid file type

# def parse_and_store_formula(file, file_type):
#     if file_type == 'csv':
#         reader = csv.DictReader(file.read().decode('utf-8').splitlines())
        
#         for row in reader:
#             process_formula_row(row)

#     elif file_type == 'json':
#         data = json.load(file)
        
#         for row in data:
#             process_formula_row(row)

# def process_formula_row(row):
#     # Get or create the category
#     category, _ = Category.objects.get_or_create(name=row["Category"])
    
#     # Check if the formula already exists
#     formula, created = FormulaTemplate.objects.get_or_create(
#         name=row["Formula Name"], 
#         category=category
#     )
    
#     # Update the formula if it already exists
#     if not created:
#         # Update variables and weights
#         formula.variables = row["Variables"].split(", ")
#         formula.weights = [float(w) for w in row["Weights"].split(", ")]
#         formula.save()  # Save changes to the existing formula
#     else:
#         # If the formula was created, set variables and weights
#         formula.variables = row["Variables"].split(", ")
#         formula.weights = [float(w) for w in row["Weights"].split(", ")]
#         formula.save()  # Save new formula


# # @api_view(["POST"])
# # def upload_file(request):
# #     if request.method == 'POST' and request.FILES.get('file'):
# #         uploaded_file = request.FILES['file']
# #         file_type = get_file_type(uploaded_file.name)  # Get the file type based on the extension

# #         if file_type is None:
# #             return HttpResponse("Invalid file type. Please upload a CSV, Excel, or JSON file.")

# #         # Parse and store data based on file type
# #         parse_and_store_formula(uploaded_file, file_type)
        
# #         return HttpResponse("File processed successfully.")

# #     return render(request, 'upload.html')

# # class FileUploadAPI(APIView):
# #     parser_classes = (MultiPartParser, FormParser)

# #     def post(self, request, *args, **kwargs):
# #         uploaded_file = request.FILES.get('file')
# #         if not uploaded_file:
# #             return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

# #         file_type = get_file_type(uploaded_file.name)  # Get the file type based on the extension

# #         if file_type is None:
# #             return Response({"error": "Invalid file type. Please upload a CSV, Excel, or JSON file."}, status=status.HTTP_400_BAD_REQUEST)

# #         # Parse and store data based on file type
# #         parse_and_store_formula(uploaded_file, file_type)
        
# #         return Response({"message": "File processed successfully."}, status=status.HTTP_200_OK)

# class FileUploadAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser) 

#     def post(self, request, *args, **kwargs):
#         serializer = FileUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             uploaded_file = serializer.validated_data['file']
#             description = serializer.validated_data.get('description', '')

#             file_type = get_file_type(uploaded_file.name)
#             if file_type is None:
#                 return Response("Invalid file type. Please upload a CSV, Excel, or JSON file.", 
#                                 status=status.HTTP_400_BAD_REQUEST)

#             # Parse and store data based on file type
#             parse_and_store_formula(uploaded_file, file_type)
#             return Response({
#                 "message": "File processed successfully.",
#                 "description": description
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CSVFileUploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class CSVFileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CSVFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']

            # Read and process the CSV file
            try:
                csv_file = uploaded_file.read().decode('utf-8').splitlines()
                reader = csv.reader(csv_file)
                
                # Process CSV data (e.g., store or print rows)
                rows = [row for row in reader]
                return Response({
                    "message": "File processed successfully.",
                    "rows": rows  # Just for demonstration, include in the response
                }, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
