from rest_framework.throttling import UserRateThrottle

class DetailsRateThrottle(UserRateThrottle):
    scope = 'details'

class AddressRateThrottle(UserRateThrottle):
    scope = 'address'

class UserRateThrottle(UserRateThrottle):
    scope = 'user1'