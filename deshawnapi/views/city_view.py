
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

    def retrieve(self, request, pk=None):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        # Step 1: Get a single city based on the primary key in the request URL
        city = City.objects.get(pk=pk)

        # Step 2: Serialize the city record as JSON
        serialized = CitySerializer(city, context={'request': request})

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Step 1: Get all city data from the database
        cities = City.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = CitySerializer(cities, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name',)

# # To serialize a list of cities (multiple rows)
# cities = City.objects.all()
# serialized = CitySerializer(cities, many=True)

# # To serialize a single city (1 row)
# city = City.objects.get(pk=pk)
# serialized = CitySerializer(city, many=False)