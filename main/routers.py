from django.contrib import admin

from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()
router.register(r'response',viewset.Response,base_name='response')
router.register(r'answer',viewset.MyViewSets,base_name='what')
# router.register(r'right',viewset.RightAnswers,base_name='right')
router.register(r'quiz',viewset.Quizes,base_name='quiz')
router.register(r'question',viewset.Question,base_name='quiz')
router.register(r'test',viewset.Test,base_name='test'),
router.register(r'variant',viewset.Variant,base_name='variant')
urlpatterns = router.urls