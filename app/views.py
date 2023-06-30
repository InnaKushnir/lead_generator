from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import UserCreateForm, ObjectSearchForm
from app.models import User, Object


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "app/user_form.html"
    success_url = reverse_lazy("app:home")


def home(request):
    users = User.objects.all()
    num_users = users.count()
    context = {"num_users": num_users, "users": users}
    return render(request, "base.html", context)


class ObjectListView(LoginRequiredMixin, generic.ListView):
    model = Object
    template_name = "app/object_list.html"
    paginate_by = 3

    def get_queryset(self):
        form = ObjectSearchForm(self.request.GET)
        if form.is_valid():
            category = form.cleaned_data["category"]
            city = form.cleaned_data["city"]
            count = form.cleaned_data["count"]
            queryset = Object.objects.filter(category=category, city=city)[:count]
        else:
            queryset = Object.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ObjectSearchForm(self.request.GET)
        return context


class ObjectCreateView(generic.CreateView):
    model = Object
    fields = "__all__"
    success_url = reverse_lazy("app:object-list")
