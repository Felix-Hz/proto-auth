from django.http import JsonResponse

# from django.shortcuts import render


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Test response n1."})
