from rest_framework.serializers import HyperlinkedModelSerializer

from restGhost import models


class ghostpost_serializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.GhostPost

        fields = ['ghostTitle','body', 'is_boast','post_date', 'goodvote', 'badvote', 'totalvotes' ]
