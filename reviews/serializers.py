from rest_framework.serializers import ModelSerializer

from .models import Comment, Reply

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance:Comment):
        rep =  super().to_representation(instance)
        rep["author"] = instance.author.username
        del rep['post']
        return rep

    def to_representation(self, instance:Comment):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.username
        rep["likes"] = instance.likes.count()
        del rep['post']
        return rep

class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
