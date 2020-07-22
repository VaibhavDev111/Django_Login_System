from loginapp.serializer import (UserInfoSerializer, EnterExitSerializer)
from rest_framework.generics import (RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView)
from django.http import Http404
from rest_framework.mixins import (CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin)
from loginapp.models import (UserInfo, EnterExitInfo)


class retrieveUserData(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    lookup_field = 'id'     
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()


class enterExitUser(RetrieveAPIView, CreateModelMixin, UpdateModelMixin, ListModelMixin):
    permission_classes = []
    authentication_classes = []
    lookup_field = 'uid'
    serializer_class = EnterExitSerializer
    queryset = EnterExitInfo.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def get_object(self):
        request = self.kwargs
        passed_id = request.get('uid', None)
        print(passed_id)
        queryset = self.queryset
        count = queryset.filter(uid=passed_id).count()
        if count <= 0:
            raise Http404("Nothing found")
        obj = None
        if passed_id is not None:
            obj = queryset.filter(uid=passed_id,).order_by('id').last()
        # print(obj.isIn)
        return obj
