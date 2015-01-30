from django.contrib import admin

from .models import FrequentItemSet, Operation


class MinerAdmin(admin.ModelAdmin):
    using = 'miner'

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def get_queryset(self, request):
        return super(admin.ModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(
            db_field, request=request, using=self.using, **kwargs)


class FrequentItemSetAdmin(MinerAdmin):
    list_display = ['id', 'remote_host', 'remote_port', 'count', 'protocol',
                    'operation']


class OperationAdmin(MinerAdmin):
    list_display = ['id', 'start', 'end', 'interval', 'tag']


admin.site.register(FrequentItemSet, FrequentItemSetAdmin)
admin.site.register(Operation, OperationAdmin)
