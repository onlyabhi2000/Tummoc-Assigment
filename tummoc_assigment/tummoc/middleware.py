
from django.utils.deprecation import MiddlewareMixin
import threading
from rest_framework.views import APIView
from rest_framework.response import Response


class RequestCounterMiddleware(MiddlewareMixin):
    _lock = threading.Lock()
    request_count = 0

    def process_request(self, request):
        with self._lock:
            RequestCounterMiddleware.request_count += 1


class RequestCountResetAPIView(APIView):
    def post(self, request):
        RequestCounterMiddleware.request_count = 0
        return Response({"message": "request count reset successfully"})


class RequestCountAPIView(APIView):
    def get(self, request):
        return Response({"requests": RequestCounterMiddleware.request_count})
