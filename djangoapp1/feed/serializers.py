from rest_framework import serializers
from .models import Music




class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ['track', 'title', 'artwork', 'artist', 'date_posted', 'artist_name',]

# class TrackSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Music
#         fields = ['track']


