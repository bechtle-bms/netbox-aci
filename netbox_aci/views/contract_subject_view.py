"""
Define the logic of the plugin.
"""

from netbox.views import generic
from utilities.views import GetRelatedModelsMixin
from .. import tables
from .. models import contract_subject_model
from .. forms import contract_subject_form

__all__ = (
    "ContractSubjectView",
    "ContractSubjectListView",
    "ContractSubjectEditView",
    "ContractSubjectDeleteView",
    "ContractSubjectBulkDeleteView",
)


class ContractSubjectView(GetRelatedModelsMixin, generic.ObjectView):
    queryset = contract_subject_model.ContractSubject.objects.all()

    def get_extra_context(self, request, instance):

        subjectfilter = instance.filter_subject.all()
        filter_table = tables.ContractFilterTable(subjectfilter)

        return {
            'filter_table': filter_table,
            'related_models': self.get_related_models(request, instance),
        }


class ContractSubjectListView(generic.ObjectListView):
    queryset = contract_subject_model.ContractSubject.objects.all()
    table = tables.ContractSubjectTable


class ContractSubjectEditView(generic.ObjectEditView):
    queryset = contract_subject_model.ContractSubject.objects.all()
    form = contract_subject_form.ContractSubjectForm
    default_return_url = 'plugins:netbox_aci:contractsubject_list'


class ContractSubjectDeleteView(generic.ObjectDeleteView):
    queryset = contract_subject_model.ContractSubject.objects.all()


class ContractSubjectBulkDeleteView(generic.BulkDeleteView):
    queryset = contract_subject_model.ContractSubject.objects.all()
    table = tables.ContractSubjectTable
