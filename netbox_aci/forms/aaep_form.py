"""
Define the django form elements for the user interface. 
"""

from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from .. models import aaep_model, domain_model

__all__ = (
    "AAEPForm",
    "AAEPStaticBindingForm",
    "AAEPFilterForm",
)


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

        aaep = self.cleaned_data.get("aaep")
        tenant = self.cleaned_data.get("tenant")
        applicationprofile = self.cleaned_data.get("applicationprofile")
        epg = self.cleaned_data.get("epg")
        #encap = self.cleaned_data.get("encap")
        mode = self.cleaned_data.get("mode")

        same_aaep = aaep_model.AAEPStaticBinding.objects.filter(aaep=aaep)

        # General duplicate protection
        if same_aaep.filter(
            tenant=tenant,
            applicationprofile=applicationprofile,
            epg=epg,
        ).exists():
            raise forms.ValidationError("EPG is already in use")

        # Specific protection for nasty access_untagged combinations
        if mode == "access_untagged":
            if same_aaep.filter(
                mode="access_8021p"
            ).exists():
                raise forms.ValidationError(
                    {"mode": "'access_8021p' is already in use."}
                )
            if same_aaep.filter(
                mode="trunk"
            ).exists():
                raise forms.ValidationError(
                    {"mode": "'trunk' is already in use."}
                )
        if mode == "access_8021p":
            if same_aaep.filter(
                mode="access_untagged"
            ).exists():
                raise forms.ValidationError(
                    {"mode": "'access_untagged' is already in use."}
                )
        if mode == "trunk":
            if same_aaep.filter(
                mode="access_untagged"
            ).exists():
                raise forms.ValidationError(
                    {"mode": "'access_untagged' is already in use."}
                )


class AAEPFilterForm(NetBoxModelFilterSetForm):

    model = aaep_model.AAEP

    domains = forms.ModelMultipleChoiceField(
        queryset=domain_model.Domain.objects.all(),
        required=False
    )
