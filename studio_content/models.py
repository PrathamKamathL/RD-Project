# studio_content/models.py

from django.db import models

class Client(models.Model):
    """
    Represents a client of the studio.
    """
    name = models.CharField(max_length=200, help_text="Full name of the client.")
    rd_number = models.CharField(max_length=50, unique=True, help_text="Unique RD number for the client.")
    phone_number = models.CharField(max_length=20, blank=True, null=True, help_text="Client's phone number (optional).")
    denomination = models.CharField(max_length=100, blank=True, null=True, help_text="Denomination of the client (optional).")
    is_active = models.BooleanField(default=True, help_text="Is this client currently active?")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the client record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the client record was last updated.")

    class Meta:
        ordering = ['name'] # Order clients alphabetically by name
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        """
        String representation of the Client.
        """
        return f"{self.name} (RD: {self.rd_number})"

class MonthlyPayment(models.Model):
    """
    Records a monthly payment status and amount for a specific client.
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments', help_text="The client associated with this payment.")
    year = models.IntegerField(help_text="The year of the payment.")
    month = models.IntegerField(help_text="The month of the payment (1-12).")
    is_paid = models.BooleanField(default=False, help_text="Check if the payment for this month is made.")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="The amount paid for this month (optional).")
    paid_on = models.DateField(blank=True, null=True, help_text="Date the payment was marked as paid (optional).")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when this payment record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when this payment record was last updated.")

    class Meta:
        # Ensure that a client can only have one payment record per month/year combination
        unique_together = ('client', 'year', 'month')
        ordering = ['-year', '-month'] # Order payments by most recent first
        verbose_name = "Monthly Payment"
        verbose_name_plural = "Monthly Payments"

    def __str__(self):
        """
        String representation of the MonthlyPayment.
        """
        status = "Paid" if self.is_paid else "Unpaid"
        amount_info = f" - ₹{self.amount_paid}" if self.amount_paid is not None else ""
        return f"{self.client.name} ({self.client.rd_number}) - {self.month}/{self.year} - {status}{amount_info}"

