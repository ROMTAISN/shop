from django.apps import AppConfig
# import redis


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'


# red = redis.Redis(
#     host='redis-13109.c304.europe-west1-2.gce.cloud.redislabs.com',
#     port=13109,
#     password='G3M8lFx3Vu03IWgjnHZgLHoZS8ocV3RK'
# )
