from rest_framework.response import Response
from rest_framework.views import APIView
import read_csv.func
from .models import Reader
from .serializers import ReaderSerializer


class ReaderView(APIView):
    def get(self, request, s):
        reader = Reader(s, read_csv.func.read(s))
        serializer_for_request = ReaderSerializer(instance=reader)
        return Response(serializer_for_request.data)