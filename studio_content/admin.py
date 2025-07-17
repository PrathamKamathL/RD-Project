# studio_content/admin.py

from django.contrib import admin
from .models import Client, MonthlyPayment # ENSURE THESE ARE THE MODELS YOU ARE IMPORTING

class MonthlyPaymentInline(admin.TabularInline):
    """
    Allows editing MonthlyPayment records directly within the Client admin page.
    """
    model = MonthlyPayment
    extra = 1 # Number of empty forms to display
    fields = ('year', 'month', 'is_paid', 'amount_paid', 'paid_on') # Added amount_paid
    readonly_fields = ('created_at', 'updated_at') # These fields should not be editable manually
    # You can add a custom form for more control, but for now, the default is fine.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Customizes the display of Client in the Django Admin interface.
    """
    list_display = ('name', 'rd_number', 'phone_number','denomination', 'is_active', 'created_at') # Changed email to rd_number
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'rd_number', 'phone_number') # Changed email to rd_number
    date_hierarchy = 'created_at'
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'rd_number', 'phone_number','denomination', 'is_active') # Changed email to rd_number
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    inlines = [MonthlyPaymentInline] # Add the inline for MonthlyPayment

@admin.register(MonthlyPayment)
class MonthlyPaymentAdmin(admin.ModelAdmin):
    """
    Customizes the display of MonthlyPayment in the Django Admin interface.
    This is useful for viewing all payments across all clients.
    """
    list_display = ('client', 'year', 'month', 'is_paid', 'amount_paid', 'paid_on', 'created_at') # Added amount_paid
    list_filter = ('is_paid', 'year', 'month', 'client')
    search_fields = ('client__name', 'client__rd_number') # Search by client's name or RD number
    date_hierarchy = 'paid_on' # Use paid_on for date navigation
    ordering = ('-year', '-month', 'client__name') # Order by most recent month
    fieldsets = (
        (None, {
            'fields': ('client', 'year', 'month', 'is_paid', 'amount_paid', 'paid_on') # Added amount_paid
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
