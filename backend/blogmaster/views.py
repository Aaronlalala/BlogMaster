from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

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
