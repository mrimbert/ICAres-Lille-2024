from django.contrib import admin
import csv
from .models import User, Lien
from django.http import HttpResponse

# Register your models here.
from .models import Epreuve

admin.site.register(Epreuve)
admin.site.register(Lien)

class UserAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'ecole', 'get_formule_display', 'get_isParticipant_display', 'has_paid']
    list_filter = ['formule', 'ecole', 'has_paid']
    search_fields = ['nom', 'prenom', 'email']

    # Ajouter l'export CSV
    actions = ['export_as_csv', 'mark_as_paid']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Trésorier').exists():
            return qs.filter(ecole=request.user.ecole)
        return qs

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        field_names += ['formule_display', 'isParticipant_display']  # Ajouter les champs à afficher

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([
                getattr(obj, field) if field not in ['formule_display', 'isParticipant_display'] else obj.get_formule_display() if field == 'formule_display' else obj.get_isParticipant_display()
                for field in field_names
            ])

        return response

    export_as_csv.short_description = "Exporter en CSV"

    def mark_as_paid(self, request, queryset):
        queryset.update(has_paid=True)

    mark_as_paid.short_description = "Marquer comme payé"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.groups.filter(name='Trésorier').exists():
            return actions
        else:
            actions.pop('mark_as_paid', None)
        return actions

admin.site.register(User, UserAdmin)