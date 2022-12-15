from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reader
from .serializers import ReaderSerializer


class ReaderView(APIView):
    def get(self, request, s):
        if s == 'wine.csv':
            s = 'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'
        reader = Reader(s, app.read_csv.func.read(s))
        serializer_for_request = ReaderSerializer(instance=reader)
        return Response(serializer_for_request.data)
