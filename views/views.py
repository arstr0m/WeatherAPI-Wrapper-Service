import consts.consts
import requests
import utils.url
from django.core.cache import cache
from django.http import JsonResponse
from django.conf import settings


def get_weather(request, city):
    if not isinstance(city, str) or not city:
        return JsonResponse({"error": "Invalid city parameter"}, status=400)

    cache_key = f"weather_{city}"
    cached_data = cache.get(cache_key)

    if cached_data:
        cached_data['got_from'] = 'cache'
        return JsonResponse(cached_data)

    try:
        api_url = utils.url.get_url(city)
    except Exception as e:
        return JsonResponse({"error": f"Error generating API URL: {e}"}, status=500)

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"HTTP request failed: {e}"}, status=500)

    if response.status_code == 200:
        weather_data = response.json()
        cache.set(cache_key, weather_data, timeout=1200)
        return JsonResponse(weather_data)
    else:
        return JsonResponse({"error": "Could not fetch weather data"}, status=response.status_code)


def test_cache(request):
    exists = cache.get('endpoint')
    if exists:
        return JsonResponse(exists)
    cache.set('endpoint', 'Hello, Redis!', timeout=60)
    value = cache.get('endpoint')
    return JsonResponse({'cached_value': value})
