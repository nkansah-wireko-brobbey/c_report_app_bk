from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .query_builder import build_dynamic_query
from .reporting_query_configurations import  AVAILABLE_FIELDS_MAP,MODEL_MAP, RELATIONSHIP_MAP

@api_view(['GET'])
def metadata_view(request):
    metadata = {
        "tables": list(MODEL_MAP.keys()),
        "fields": AVAILABLE_FIELDS_MAP,
        "relationships":  RELATIONSHIP_MAP
    }
    return Response(metadata)


class DynamicQueryView(APIView):
    def post(self, request):
        config = request.data
        try:
            results = build_dynamic_query(config)
            return Response(results)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

