# Mail Module

A Python module for creating temporary email addresses and retrieving emails for automation purposes.

## Overview

This module provides functionality to:
- Generate temporary email addresses
- Activate email accounts
- Retrieve emails sent to the temporary address

The module uses the emailmux.com service to create temporary email addresses that can be used for account verification and other automation tasks.

## Installation

```bash
pip install requests
```

## Usage

```python
from mail import Mail

# Create a mail instance with default domains (outlook, google_plus, googlemail,gmail)
mail = Mail()

# Create a mail instance with specific domains (e.g., only gmail)

# mail = Mail(["gmail"])

# Create a mail instance with a proxy
# mail = Mail(proxy="http://user:pass@host:port")

# Get the email address
email_address = mail.get_mail_adress()
print(f"Email address: {email_address}")

# Get emails sent to this address
emails = mail.get_mails()
print(f"Received emails: {emails}")
```

## API

### Mail(domains=["outlook", "google_plus", "googlemail"], proxy="")

Constructor for the Mail class.

**Parameters:**
- `domains` (list): List of domain preferences for email generation. Default is ["outlook", "google_plus", "googlemail,"gmail"]. 
  You can specify specific domains like ["gmail"] for only Gmail addresses.
- `proxy` (str): Proxy URL to use for requests (optional)

### get_mail_adress()

Returns the generated email address.

**Returns:**
- `str`: The temporary email address

### get_mails()

Retrieves all emails sent to the temporary address.

**Returns:**
- `list`: List of email objects

### activate_mail()

Activates the email account to start receiving emails.

**Returns:**
- `int`: HTTP status code

## Example

See `test_mail.py` for a complete example of how to use this module.