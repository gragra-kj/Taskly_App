from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Taskly API!",
        "endpoints": {
            "houses": "/api/house/",
            "tasks": "/api/task/",
            "accounts": "/api/accounts/",
        },
    })