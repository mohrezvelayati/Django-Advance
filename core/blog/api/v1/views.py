from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404



@api_view(["GET","POST"]) 
def postList(request):
    if request.method == "GET":
        post = Post.objects.filter(status = True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        


@api_view(["GET", "PUT", "DELETE"]) 
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id, status = True)
    serializer = PostSerializer(post)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"Detail:": "Item removed Successfully"},status=staticmethod)