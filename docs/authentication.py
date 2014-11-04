REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  # Basic HTTP Auth, realm=”api”
        'rest_framework.authentication.SessionAuthentication',  # For Browseable API
        'rest_framework.authentication.OAuth2Authentication',  # Standard OAuth2
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    )
}