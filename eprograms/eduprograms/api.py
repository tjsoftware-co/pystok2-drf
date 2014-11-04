from rest_framework import viewsets, routers, serializers
from .models import Program, ProgramFor, ProgramCategory, ProgramChapter


class ProgramChapterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramChapter


class ProgramForSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramFor


class ProgramCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramCategory


# Serializers define the API representation.
class ProgramSerializer(serializers.HyperlinkedModelSerializer):

    program_for = ProgramForSerializer(many=True)
    program_category = ProgramCategorySerializer(many=True)
    programchapter_set = ProgramChapterSerializer(many=True)

    class Meta:
        model = Program
        fields = ('name', 'program_for', 'program_category',
                  'programchapter_set')


class ProgramViewSet(viewsets.ModelViewSet):
    """
    Basic API view for programs
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramForViewSet(viewsets.ModelViewSet):
    """
    Basic API view for ProgramFor
    """
    queryset = ProgramFor.objects.all()
    serializer_class = ProgramForSerializer


class ProgramCategoryViewSet(viewsets.ModelViewSet):
    """
    Basic API view for ProgramFor
    """
    queryset = ProgramCategory.objects.all()
    serializer_class = ProgramCategorySerializer


class ProgramChapterViewSet(viewsets.ModelViewSet):
    """
    Basic API view for ProgramChapter
    """
    queryset = ProgramChapter.objects.all()
    serializer_class = ProgramChapterSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'programs-for', ProgramForViewSet)
router.register(r'programs-category', ProgramCategoryViewSet)
router.register(r'programs-chapter', ProgramChapterViewSet)