from ._anvil_designer import collectPaymentTemplate
from anvil import *
import stripe.checkout
import anvil.server

class collectPayment(collectPaymentTemplate):
  def create_invoice_button_click(self, **event_args):
    """
    Called when the 'Create Invoice' button is clicked.
    """
    line_items = [
        {"item_id": "1", "description": "Service A", "amount": 100.0, "quantity": 2},
        {"item_id": "2", "description": "Service B", "amount": 50.0, "quantity": 3}
    ]

    try:
        invoice = anvil.server.call('create_qbo_invoice', line_items)
        alert(f"Invoice created successfully! Invoice ID: {invoice['Id']}, Total: ${invoice['TotalAmt']:.2f}")
    except Exception as e:
        alert(f"Failed to create invoice: {e}")

  def create_customer_button_click(self, **event_args):
    """
    This method is called when the 'Create Customer' button is clicked.
    """
    first_name = self.first_name_input.text
    last_name = self.last_name_input.text
    email = self.email_input.text

    if not first_name or not last_name or not email:
        alert("Please fill in all fields: First Name, Last Name, and Email.")
        return

    try:
        # Single server call to handle both QBO and local customer creation
        customer_data = anvil.server.call('create_and_store_customer', first_name, last_name, email)
        alert(f"Customer created successfully! Customer ID: {customer_data['Id']}")
    except Exception as e:
        if "already exists" in str(e):
            alert("This email address is already associated with a customer in QuickBooks Online. Please use a different email or contact support if you believe this is an error.")
        else:
            alert(f"Failed to create customer: {e}")
