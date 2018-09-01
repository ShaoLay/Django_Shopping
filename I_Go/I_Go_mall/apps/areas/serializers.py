from rest_framework import serializers

from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name')


# bj_area = Area.objects.get(id=1101000)
# bj_area.id
# bj_area.name
# bj_area.subs = [area_object, area_object, .....]


class SubAreaSerializer(serializers.ModelSerializer):
    subs = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')

    # {
    #     "id": xxx,
    #     'name': xxx,
    #     'subs': [
    #         {
    #             "id":xx,
    #             'name':xxx
    #         },
    #         {
    #
    #         }
    #     ]
    # }