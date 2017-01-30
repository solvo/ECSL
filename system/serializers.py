from rest_framework import serializers
from .models import *
from django.utils.text import slugify
from rest_framework.reverse import reverse as drf_reverse


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        read_only_fields = ('slug',)
        fields = '__all__'

    def validate(self, data):
        data['slug'] = slugify(data['title'])
        return data

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': drf_reverse('topic-detail', kwargs={'pk': obj.pk}, request=request),
            'vars': drf_reverse('var-list', request=request) + '?topic={}'.format(obj.pk),
        }

