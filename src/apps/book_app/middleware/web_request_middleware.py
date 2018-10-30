from django.utils.deprecation import MiddlewareMixin
from apps.book_app.models import WebRequest

class WebRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        WebRequest.objects.create(title = request, data = request.__dict__)
