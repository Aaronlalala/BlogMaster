from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
# Views are equivalent to routes in JavaScript

# django.middleware.csrf.get_token()
@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'success': True, 'user_id': user.id}, status=200)
    
    return Response({'success': False, "error_message": serializer.errors}, status=400)



@api_view(["POST"])
def login_action(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Get token and add in response
        return Response({'success': True}, status=200)

    else:
        return Response({'success': False, 'error_message': "Log in failed"}, status=400)



@api_view(['POST'])
def logout_action(request):
    logout(request)
    return Response({'success': True}, status=200)



@api_view(['GET'])
def get_post(reqeust, pk):
    # Get the post
    post = get_object_or_404(Post, pk=pk)

    data = {
        'id': post.id,
        'user': str(post.user),
        'text': post.text,
        'creation_time': post.creation_time
    }

    return Response({'success': True, 'post': data})
    

@api_view(["POST"])
def create_post(request):
    data = request.data
    try:
        text = data['text']
        user = request.user
        creation_time = timezone.now()

        post = Post.objects.create(text=text, user=user, creation_time=creation_time)
        post.save()
        return Response({'success': True}, status=201)
    except Exception as e:
        return Response({'success': False, 'error_message': str(e)}, status=400)


@api_view(['DELETE'])
def delete_post(request, pk):
    # Get the object to delete
    post = get_object_or_404(Post, pk=pk)

    if request.method == "DELETE":
        if (post.user == request.user):
            post.delete()
            return Response({'success': True, 'message': 'Delete a post'}, status=200)
        else:
            return Response({'success': False, 'message': "You can't delete other users' posts."}, status=500)

    return Response({'success': False}, status=405)


@api_view(['GET'])
def get_comment(request, pk):
    # Get the post
    comment = get_object_or_404(Comment, pk=pk)

    data = {
        'id': comment.id,
        'user': str(comment.user),
        'text': comment.text,
        'creation_time': comment.creation_time,
        'post': str(comment.post)
    }

    return Response({'success': True, 'post': data})


@api_view(['POST'])
def create_comment(request):
    data = request.data
    try:
        text = data['text']
        user = request.user
        creation_time = timezone.now()
        post = get_object_or_404(Post, pk=data['post'])

        comment = Comment.objects.create(text=text, user=user, creation_time=creation_time, post=post)
        comment.save()

        return Response({'success': True}, status=200)

    except Exception as e:
        return Response({'success': False, 'error_message': str(e)}, status=400)


@api_view(['DELETE'])
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "DELETE":
        if (comment.user == request.user):
            comment.delete()
            return Response({'success': True, 'message': "Delete a comment"}, status=200)
        else:
            return Response({'success': False, 'message': "You can't delete other user's comments."}, status=500)

    
    return Response({'success': False}, status=405)