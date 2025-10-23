import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Location

def home(request):
    return render(request, "tracker/home.html")

def dashboard(request):
    return render(request, "tracker/dashboard.html")

@csrf_exempt
@require_http_methods(["POST"])
def update_location(request):
    try:
        data = json.loads(request.body.decode())
        username = data.get("username")
        latitude = float(data.get("latitude"))
        longitude = float(data.get("longitude"))
        accuracy = data.get("accuracy", None)
    except Exception:
        return HttpResponseBadRequest("Invalid data")

    if not username:
        return HttpResponseBadRequest("Username required")

    loc = Location.objects.create(
        username=username,
        latitude=latitude,
        longitude=longitude,
        accuracy=float(accuracy) if accuracy else None,
    )
    return JsonResponse({"status": "ok", "id": loc.id})

def latest_locations_json(request):
    qs = Location.objects.order_by("-timestamp")
    seen = {}
    result = []
    for loc in qs:
        if loc.username not in seen:
            seen[loc.username] = True
            result.append({
                "username": loc.username,
                "latitude": loc.latitude,
                "longitude": loc.longitude,
                "accuracy": loc.accuracy,
                "timestamp": loc.timestamp.isoformat()
            })
    return JsonResponse(result, safe=False)
