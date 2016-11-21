from jobs.models import Job

from rest_framework.generics import (
    ListAPIView
)

from .serializers import (
    JobListSerializer
    )

class JobListAPIView(ListAPIView):
    serializer_class = JobListSerializer

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Job.objects.all() #filter(user=self.request.user)

        return queryset_list
