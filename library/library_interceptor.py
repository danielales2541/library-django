import datetime
from django.conf import settings  # ✅ ESTA ES LA LÍNEA QUE FALTABA
from django.http import JsonResponse

class LibraryInterceptorMiddleware:
    def __init__(self, get_response):
        print("LibraryInterceptorMiddleware initialized")
        self.get_response = get_response
        self.open_hour = getattr(settings, 'CALENDAR_OPEN', 16)
        self.close_hour = getattr(settings, 'CALENDAR_CLOSE', 24)

    def __call__(self, request):
        print("LibraryInterceptorMiddleware called")
        print(self.open_hour, self.close_hour)
        print("Request path:", request.path)
        if request.path.startswith('/api/loans/'):
            now = datetime.datetime.now()
            hour = now.hour
            print("Current hour:", hour)
            if not (self.open_hour <= hour < self.close_hour):
                
                return JsonResponse({
                    "message": "Fuera de hora laboral",
                    "date": now.isoformat()
                }, status=401)
        return self.get_response(request)
