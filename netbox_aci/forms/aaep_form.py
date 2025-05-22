"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import aaep_model, domain_model

class AAEPForm(NetBoxModelForm):

    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name',
            'slug',
            'description',
            'infrastructure_vlan',
            'domains',
        ),
    )

    class Meta:
        model = aaep_model.AAEP
        fields = (
            'name',
            'slug',
            'description',
            'comments',
            'infrastructure_vlan',
            'domains',
        )


class AAEPStaticBindingForm(NetBoxModelForm):

    comments = CommentField()

    fieldsets = (
        FieldSet(
            'aaep',
            'tenant',
            'applicationprofile',
            'epg',
            'encap',
            'mode',
        ),
    )

    class Meta:
        model = aaep_model.AAEPStaticBinding
        fields = (
            'aaep',
            'tenant',
            'applicationprofile',
            'epg',
            'encap',
            'mode',
        )

    def clean(self):
        """
        Prevent duplicate entries
        """
        super().clean()

        tenant = self.cleaned_data.get("tenant")
        applicationprofile = self.cleaned_data.get("applicationprofile")
        epg = self.cleaned_data.get("epg")
        encap = self.cleaned_data.get("encap")
        mode = self.cleaned_data.get("mode")

        if tenant and applicationprofile and epg:
            if aaep_model.AAEPStaticBinding.objects.filter(mode='access_untagged').exists():
                self.add_error("mode", "Duplicate entry")
            if aaep_model.AAEPStaticBinding.objects.filter(mode='access_8021p').exists():
                if mode not in 'trunk':
                    self.add_error("mode", "Duplicate entry")
                if aaep_model.AAEPStaticBinding.objects.filter(encap=encap).exists():
                    self.add_error("encap", "Duplicate entry")
            if aaep_model.AAEPStaticBinding.objects.filter(mode='trunk').exists():
                if mode in 'access_untagged':
                    self.add_error("mode", "Duplicate entry")
            if aaep_model.AAEPStaticBinding.objects.filter(encap=encap).exists():
                self.add_error("encap", "Duplicate entry")


class AAEPFilterForm(NetBoxModelFilterSetForm):

    model = aaep_model.AAEP

    domains = forms.ModelMultipleChoiceField(
        queryset=domain_model.Domain.objects.all(),
        required=False
    )
