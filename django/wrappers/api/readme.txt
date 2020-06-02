Чтобы создать api:
    https://www.django-rest-framework.org/#quickstart
    https://www.django-rest-framework.org/tutorial/quickstart/
    1)pip install djangorestframework
    2)in projectnameapp/settings.py add:
        INSTALLED_APPS = [
            ...
            'rest_framework'
        ]
    3)in someapp/urls.py add:
        urlpatterns = [
            ...
            path('api-auth', include('rest_framework.urls'))
        ]
    4)in rooturls.py:
        '''
            from django.conf.urls import url, include
            from django.contrib.auth.models import User
            from rest_framework import routers, serializers, viewsets

            # Serializers define the API representation.
            class UserSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model = User
                    fields = ['url', 'username', 'email', 'is_staff']

            # ViewSets define the view behavior.
            class UserViewSet(viewsets.ModelViewSet):
                queryset = User.objects.all()
                serializer_class = UserSerializer

            # Routers provide an easy way of automatically determining the URL conf.
            router = routers.DefaultRouter()
            router.register(r'users', UserViewSet)

            # Wire up our API using automatic URL routing.
            # Additionally, we include login URLs for the browsable API.
            urlpatterns = [
                url(r'^', include(router.urls)),
                url(r'^api-auth/', include('rest_framework.u	rls', namespace='rest_framework'))
        	'''
		]
    5)Create serializer (our presentation of db):
        someapp/serializers.py
        '''
            from django.contrib.auth.models import User, Group
            from rest_framework import serializers


            class UserSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model = User
                    fields = ['url', 'username', 'email', 'groups']


            class GroupSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model = Group
                    fields = ['url', 'name']
        '''

        someapp/views.py
        '''
            from django.contrib.auth.models import User, Group
            from rest_framework import viewsets
            from rest_framework import permissions
            from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


            class UserViewSet(viewsets.ModelViewSet):
                """
                API endpoint that allows users to be viewed or edited.
                """
                queryset = User.objects.all().order_by('-date_joined')
                serializer_class = UserSerializer
                permission_classes = [permissions.IsAuthenticated]


            class GroupViewSet(viewsets.ModelViewSet):
                """
                API endpoint that allows groups to be viewed or edited.
                """
                queryset = Group.objects.all()
                serializer_class = GroupSerializer
                permission_classes = [permissions.IsAuthenticated]
        '''
    6)root/urls.py
        '''
            from django.urls import include, path
            from rest_framework import routers
            from tutorial.quickstart import views

            router = routers.DefaultRouter()
            router.register(r'users', views.UserViewSet)
            router.register(r'groups', views.GroupViewSet)

            # Wire up our API using automatic URL routing.
            # Additionally, we include login URLs for the browsable API.
            urlpatterns = [
                path('', include(router.urls)),
                path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
            ]
        '''
    7)Paginations
        REST_FRAMEWORK = {
            'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
            'PAGE_SIZE': 10
        }

    8)It's will work!!
    9)Example from curl:
        bash: curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
        {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "email": "admin@example.com",
                    "groups": [],
                    "url": "http://127.0.0.1:8000/users/1/",
                    "username": "admin"
                },
                {
                    "email": "tom@example.com",
                    "groups": [                ],
                    "url": "http://127.0.0.1:8000/users/2/",
                    "username": "tom"
                }
            ]
        }
     10)Не забыть сделать миграции
     11)Создрать superuser'a


1)Создание нового API:
	