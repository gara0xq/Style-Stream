from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# ALI
router.register('user-register', UserRegisterView)
router.register('user-login', UserLoginView)
router.register('get-user', UserView)
router.register('user-logout', UserLogoutView)
router.register('dealer-register', DealerRegisterView)
router.register('dealer-login', DealerLoginView)
router.register('get-dealer', DealerView)
router.register('dealrt-logout', DealerLogoutView)

###
router.register('category', CategoryView)
router.register('product', ProductView)
router.register('sub-product', SubProductView)
router.register('review', ReviewView)
router.register('favoutite', FavouriteView)
###

# MARIAM



# AMMAR





urlpatterns = [
    path('', include(router.urls)),
]