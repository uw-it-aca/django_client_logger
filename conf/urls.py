# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.urls import include, re_path


urlpatterns = [
    re_path(r'^', include('django_client_logger.urls')),
]
