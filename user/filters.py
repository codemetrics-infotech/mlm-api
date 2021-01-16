from django_filters.rest_framework import DjangoFilterBackend, FilterSet

class UserFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        # Merge filterset kwargs provided by view class
        if hasattr(view, 'get_filterset_kwargs'):
            kwargs.update(view.get_filterset_kwargs())
        return kwargs

class UserFilter(FilterSet):
    def __init__(self, *args, username=None, **kwargs):
        super().__init__(*args, **kwargs)
        filterset_fields = (username)