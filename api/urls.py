from os import name
from django.urls import path
from .Views import *

urlpatterns = [
    path('', view=index, name='api-index'),
    path('api_root/', view=api_root, name='api-root'),
    path('new_worker/', view=register_worker, name='register-worker'),
    path('roll_call/', view=make_roll_call, name='make-roll-call'),
    path('login/', view=login, name='login'),
    path('submit-photos/', view=submit_photos, name='submit-photos'),
    path('identify-photo/', view=predict_photo, name='predict-photo'),
]