from rest_framework import generics
from .models import BlogPost, Comment
from .serializers import BlogSerializer, CommentSerializer

class BlogAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = BlogPost.objects.all()

class SingleBlogAPI(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

class CreateCommentAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer