class ProgramForViewSet(viewsets.ModelViewSet):
    """
    Basic API view for ProgramFor
    """
    queryset = ProgramFor.objects.all()


class ProgramCategoryViewSet(viewsets.ModelViewSet):
    """
    Basic API view for ProgramFor
    """
    queryset = ProgramCategory.objects.all()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'programs-for', ProgramForViewSet)
router.register(r'programs-category', ProgramCategoryViewSet)