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