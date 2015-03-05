from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from miner.models import FrequentItemSet
from reports.models import Report


class ReportsView(ListView):
    model = Report
    template_name = "reports.html"


class ReportDetailView(DetailView):
    model = Report
    template_name = "report_item.html"

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        items = context['object'].items.all()
        for item in items:
            setattr(item, 'itemset', FrequentItemSet.objects.get(id=item.frequent_item_set))
        context.update({'items': items})
        return context
