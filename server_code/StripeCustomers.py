import anvil.secrets
import anvil.users
import anvil.tables as tables 
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



key = anvil.secrets.get_secret("pristine_stripe_test_secret")