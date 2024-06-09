from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Post, Valoracion

class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'titulo', 'cuerpo', 'user', 'url']
        extra_kwargs = {
            'url': {'view_name': 'post-detail'},
        }
class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    fecha_registro = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Valoracion
        fields = ['id', 'rating', 'comment', 'fecha_registro', 'user', 'post', 'url']
