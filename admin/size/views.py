from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from size.models import Size
from region.models import Region
from admin.mixins import LoginRequiredMixin
from .forms import FormSize, CustomModelMultipleChoiceField


class AdminSizeIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/size/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sizes'] = Size.objects.filter(is_deleted=False)
        return context


class AdminSizeCreateView(LoginRequiredMixin, FormView):
    template_name = 'admin/size/create.html'
    form_class = FormSize
    success_url = reverse_lazy('admin_size_index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AdminSizeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'admin/size/update.html'
    template_name_suffix = "_form"
    model = Size
    success_url = reverse_lazy('admin_size_index')
    fields = [
        "name", "slug", "description", "vcpu", "disk", "memory", "transfer", "regions", "price", "is_active"
    ]

    def get_form(self, form_class=None):
        form = super(AdminSizeUpdateView, self).get_form(form_class)
        form.fields["regions"] = CustomModelMultipleChoiceField(
            queryset=Region.objects.filter(is_deleted=False), 
            widget=forms.CheckboxSelectMultiple()
        )
        return form

class AdminSizeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'admin/size/delete.html'
    model = Size
    success_url = reverse_lazy('admin_size_index')

    def delete(self, request, *args, **kwargs):
        size = self.get_object()
        size.delete()
        return super(self).delete(request, *args, **kwargs)
