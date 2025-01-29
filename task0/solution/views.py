from django.http import JsonResponse
from datetime import datetime, timezone

def home(request):
    return JsonResponse({
        "email": "ikwuegbu300@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/mikemando/HNG-Task-0"
    })