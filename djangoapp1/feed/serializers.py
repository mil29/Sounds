from rest_framework import serializers
from .models import Music



class MusicSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="feed:user-detail")

    class Meta:
        model = Music
        fields = ('url', 'track', 'title', 'artwork', 'artist', 'date_posted')


