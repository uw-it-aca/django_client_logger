# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


INSTALLED_APPS += [
    'django_client_logger',
    ]

MIDDLEWARE += [
    'userservice.user.UserServiceMiddleware',
]
