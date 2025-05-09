import json
from django.http import JsonResponse
from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = {
            "id": model_data.id,
            "title": model_data.title,
            "content": model_data.content,
            "price": model_data.price,
        }
    else:
        data = {
            "message": "No products found."
        }
    return JsonResponse(data)