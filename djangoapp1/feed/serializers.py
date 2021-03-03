from rest_framework import serializers
from .models import Music




class MusicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Music
        fields = ('track', 'title', 'artwork', 'artist', 'date_posted')


