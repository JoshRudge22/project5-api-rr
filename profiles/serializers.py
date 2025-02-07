from rest_framework import serializers
from .models import Profile
from dj_rest_auth.serializers import UserDetailsSerializer

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    preferred_role = serializers.ChoiceField(choices=Profile.JOB_CHOICES, required=False)

    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'age', 'address', 'documents', 'email', 'preferred_role', 'looking_for_work']




class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.profile_picture.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )