from rest_framework import viewsets, routers
from .models import Program


class ProgramViewSet(viewsets.ModelViewSet):
    """
    Basic API view for programs
    """
    queryset = Program.objects.all()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'programs', ProgramViewSet)