from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import LoginAccount
from .serializers import LoginSerializer


class AccountListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, id=None):
    if id:
      # If an id is provided in the GET request, retrieve the LoginAccount by that id
      try:
        queryset = LoginAccount.objects.get(id=id)
      except LoginAccount.DoesNotExist:
        # If the Account does not exist, return an error response
        return Response({'errors': 'This Account does not exist.'}, status=400)

      # Serialize Accounts from Django queryset object to JSON formatted data
      read_serializer = LoginSerializer(queryset)

    else:
      # Get all Accounts from the database using Django's model ORM
      queryset = LoginAccount.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = LoginSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
    return Response(read_serializer.data)


  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = LoginSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new account record in the database
      account_object = create_serializer.save()

      # Serialize the new account from a Python object to JSON format
      read_serializer = LoginSerializer(account_object)

      # Return a HTTP response with the newly created account data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the account, the user wants to update exists or not
      account = LoginAccount.objects.get(id=id)
    except LoginAccount.DoesNotExist:
      # If the account does not exist, return an error response
      return Response({'errors': 'This account does not exist.'}, status=400)

    # If the account does exists, use the serializer to validate the updated data
    update_serializer = LoginSerializer(account, data=request.data)

    # If the data to update the account is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the account in the database
      account_object = update_serializer.save()

      # Serialize the account from Python object to JSON format
      read_serializer = LoginSerializer(account_object)

      # Return a HTTP response with the newly updated account
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the account, the user wants to update exists
      account = LoginAccount.objects.get(id=id)
    except LoginAccount.DoesNotExist:
      # If the account does not exist, return an error response
      return Response({'errors': 'This account does not exist.'}, status=400)

    # Delete the chosen account from the database
    account.delete()

    # Return a HTTP response notifying that the account was successfully deleted
    return Response(status=204)