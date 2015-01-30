from django.contrib import admin

from .models import FrequentItemSet


class FrequentItemSetAdmin(admin.ModelAdmin):
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

    list_display = ['id', 'remote_host', 'remote_port', 'count', 'protocol',
                    'operation']


admin.site.register(FrequentItemSet, FrequentItemSetAdmin)
