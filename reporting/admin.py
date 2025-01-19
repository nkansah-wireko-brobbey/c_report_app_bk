from django.contrib import admin
from .models import Receiving, Phone, Shipping, Employee

# Register the Receiving model
@admin.register(Receiving)
class ReceivingAdmin(admin.ModelAdmin):
    list_display = ('receiving_id', 'phone', 'received_date')  # Columns to display in admin
    search_fields = ('receiving_id', 'phone__brand')  # Searchable fields
    list_filter = ('received_date',)  # Filter sidebar options

# Register other models
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'quantity')
    search_fields = ('brand', 'model')

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('shipping_id', 'phone', 'destination', 'shipped_date', 'quantity')
    search_fields = ('destination',)
    list_filter = ('shipped_date',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name')
    search_fields = ('name',)
