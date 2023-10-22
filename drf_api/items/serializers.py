from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Standard image validation function
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Item
        fields = [
            'id', 'owner', 'is_owner', 'drawer', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'description', 'image'
        ]

class ItemDetailSerializer(ItemSerializer):
    """
    Serializer for the Item model used in Detail view
    Drawer is a read only field so that we dont have to set it on each update
    """
    drawer = serializers.ReadOnlyField(source='drawer.id')
