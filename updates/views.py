from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from cfeapi.mixins import JsonResponseMixin
from .models import Update
# def detail_view(request):
#     return render() #return JSON data

def update_model_detail_view(request):
    '''
    URI -- for a REST API
    '''
    data = {
        "count": 100,
        "content": "some new content"

    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "some new content"
        }
        return JsonResponse(data)


class JsonCBV2(View):
    def get(self, request, *args, **kwargs):
        data = {
        "count": 100,
        "content": "some new content"
        }
        return JsonResponse(data)