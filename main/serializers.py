from rest_framework.serializers import ModelSerializer
from .models import Post
from reviews.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance: Post):
        # print('instance:',instance)
        rep = super().to_representation(instance)
        # print("repr:",rep)
        rep['author'] = instance.author.username
        comments = instance.comments.all()
        rep['comments'] = CommentSerializer(comments,many=True).data
        return rep
        
        rep = super().to_representation(instance)
        # print('repr: ', rep)
        rep['author'] = instance.author.username
        
        # comments = instance.comments.all()
        
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data #комментарий и информация о нем
        # rep['comments'] = instance.comments.count() # количество комментариев к каждому посту
        rep["likes"] = instance.likes.count()
        return rep