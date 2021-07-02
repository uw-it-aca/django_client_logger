
INSTALLED_APPS += [
    'django_client_logger',
    ]

MIDDLEWARE += [
    'userservice.user.UserServiceMiddleware',
]
