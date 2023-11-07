from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import views, viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LeadSerializer, RawContactSerializer, UserSerializer, ContactSerializer, CustomTokenObtainPairSerializer
from .models import Contact, Lead, RawContact
from django.core.exceptions import MultipleObjectsReturned
from rest_framework.decorators import action
from django.core.mail import send_mail


class CustomPermission(BasePermission):
    """
    Custom permission to only allow authenticated users to edit an object.
    """
    def has_permission(self, request, view):
        # Write permissions are only allowed to the authenticated users.
        if view.action == 'create':
            return True  # Anyone can list, regardless of authentication
        return request.user and request.user.is_authenticated


class SignupView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        
        # Step 1: Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Step 2: Log in the newly created user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'Lead': 'User created and logged in successfully',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Could not authenticate user'
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.CreateAPIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class CurrentUserView(APIView):
    """
    Retrieve the currently authenticated user's details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]  # Optional: only allow authenticated users

    def create(self, request, *args, **kwargs):
        # Get the user
        user_id = request.data.get('user')
        
        print("user id from front-end : " + str(user_id))
        try:
            user = User.objects.get(id=user_id)
            print(user)
            # Create the contact
            contact_data = {
                'telephone': request.data.get('telephone'),
                'adresse': request.data.get('adresse'),
                'business': request.data.get('business'),
                'job': request.data.get('job'),
                'status': request.data.get('status'),
            }
            print(contact_data)
            
            try:
                contact, created = Contact.objects.update_or_create(
                    user=user,  # Here, we use the user instance, not just the ID.
                    defaults=contact_data,
                )
                print("Contact updated or created:", contact)
            except MultipleObjectsReturned:
                return Response({'error': 'Multiple contacts found for the same user. Cannot proceed.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(contact)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomPermission]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [CustomPermission]

class RawContactViewSet(viewsets.ModelViewSet):
    queryset = RawContact.objects.all()
    serializer_class = RawContactSerializer
    permission_classes = [CustomPermission]  # Add this line

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [CustomPermission]  # Add this line

    def perform_create(self, serializer):
        # Save the lead first
        lead = serializer.save()
        # After saving, send the email
        self.send_email_to_user(lead)

    def send_email_to_user(self, lead):
        # Define your email sending logic here
        subject = 'New Lead Created'
        message = f'Lead {lead.name} was created successfully.'
        email_from = 'n.traore@-mak.org'
        recipient_list = [lead.email]
        send_mail(subject, message, email_from, recipient_list)
