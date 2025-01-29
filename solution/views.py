from django.http import JsonResponse
from datetime import datetime, timezone


def home(request):
    currDateTime = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    timeStamp = currDateTime.split('+')[0] + 'Z'

    return JsonResponse({
        "email": "ikwuegbu300@gmail.com",
        "current_datetime": timeStamp,
        "github_url": "https://github.com/mikemando/HNG-Task-0"
    })