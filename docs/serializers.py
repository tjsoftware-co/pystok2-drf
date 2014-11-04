from rest_framework import viewsets, routers, serializers
from .models import Program, ProgramFor, ProgramCategory


# Serializers define the API representation.
class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ('name', 'program_for', 'program_category')


class ProgramViewSet(viewsets.ModelViewSet):
    """
    Basic API view for programs
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer