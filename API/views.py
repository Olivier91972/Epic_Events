from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .permissions import AdminPermission, SalesPermission, SupportPermission, IsSuperUser
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer, UserSerializer


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        user_group = str(self.request.user.groups.get())
        client_name = self.request.query_params.get('company_name')
        client_email = self.request.query_params.get('email')
        if 'Admin' == user_group:
            queryset = Client.objects.all()
        elif 'Equipe de vente' == user_group:
            queryset = Client.objects.filter(sales_contact=self.request.user)
        elif 'Equipe support' == user_group:
            client_events = Event.objects.filter(support_contact=self.request.user)
            list_clients = []
            for event in client_events:
                if event.client not in list_clients:
                    list_clients.append(event.client)
            queryset = list_clients

        # gestion des filtres
        if client_name is not None:
            queryset = queryset.filter(company_name=client_name)
        if client_email is not None:
            queryset = queryset.filter(email=client_email)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class ContractViewSet(ModelViewSet):

    serializer_class = ContractSerializer

    def get_queryset(self):
        user_group = str(self.request.user.groups.get())
        client_name = self.request.query_params.get('company_name')
        client_email = self.request.query_params.get('email')
        contract_date = self.request.query_params.get('date_created')
        contract_amount = self.request.query_params.get('amount')
        if 'Admin' == user_group:
            queryset = Contract.objects.all()
        else:
            queryset = Contract.objects.filter(sales_contact=self.request.user)

        # gestion des filtres
        if client_name is not None:
            client = Client.objects.get(company_name=client_name)
            queryset = queryset.filter(client=client)
        if client_email is not None:
            client = Client.objects.get(email=client_email)
            queryset = queryset.filter(client=client)
        if contract_date is not None:
            queryset = queryset.filter(date_created=contract_date)
        if contract_amount is not None:
            queryset = queryset.filter(amount=contract_amount)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class EventViewSet(ModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        user_group = str(self.request.user.groups.get())
        client_name = self.request.query_params.get('company_name')
        client_email = self.request.query_params.get('email')
        event_date = self.request.query_params.get('event_date')
        if 'Admin' == user_group:
            queryset = Event.objects.all()
        else:
            queryset = Event.objects.filter(support_contact=self.request.user)

        # gestion des filtres
        if client_name is not None:
            client = Client.objects.get(company_name=client_name)
            queryset = queryset.filter(client=client)
        if client_email is not None:
            client = Client.objects.get(email=client_email)
            queryset = queryset.filter(client=client)
        if event_date is not None:
            queryset = queryset.filter(event_date=event_date)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission | SupportPermission]
        elif self.action in ['create']:
            permission_classes = [IsSuperUser | AdminPermission | SalesPermission]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission | SupportPermission]
        else:
            permission_classes = [IsSuperUser | AdminPermission]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
            permission_classes = [IsSuperUser | AdminPermission]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]
