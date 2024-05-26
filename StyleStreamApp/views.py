from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import *
from .models import *
import jwt, datetime


# ALI
class DealerRegisterView(APIView):
    def post(self, request):
        serializer = DealerSerialzer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class DealerLoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = Dealer.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('user not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        respose = Response()
        respose.set_cookie(key='jwt', value= token, httponly= True)

        respose.data = {
            'jwt': token
        }

        return respose
    
class DealerView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticatedee!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerialzer(user)

        return Response(serializer.data)
    
class DealerLogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response




class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerialzer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class UserLoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('user not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        respose = Response()
        respose.set_cookie(key='jwt', value= token, httponly= True)

        respose.data = {
            'jwt': token
        }

        return respose
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticatedee!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerialzer(user)

        return Response(serializer.data)
    
class UserLogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response





###
class CategoryView(APIView):
    queryset = Category.objects.all()
    serializer_class = CartSerializer
class ProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class SubProductView(APIView):
    queryset = SubProduct.objects.all()
    serializer_class = SubProductSerializer
class ReviewView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class FavouriteView(APIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
###




# MARIAM







# AMMAR





