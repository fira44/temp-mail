#!/usr/bin/env python3
"""
Test script for the Mail module
"""

import sys
import os
import time
from mail import Mail

def test_mail():
    """Test the Mail class functionality"""
    print("Testing Mail module...")
    
    try:
        # Create a mail instance
        print("Creating temporary email address...")
        mail = Mail()
        
        # Get the email address
        email_address = mail.get_mail_adress()
        print(f"Generated email address: {email_address}")
        
        # Wait a moment for activation
        print("Waiting for email activation...")
        time.sleep(2)
        
        # Activate the mail (though it should already be activated in __init__)
        activation_status = mail.activate_mail()
        print(f"Activation status code: {activation_status}")
        
        # Get emails (should be empty initially)
        print("Checking for emails...")
        emails = mail.get_mails()
        print(f"Number of emails received: {len(emails)}")
        
        if emails:
            print("Emails received:")
            print(emails)
        else:
            print("No emails received yet. This is normal for a new temporary email address.")
            
        print("\nTest completed successfully!")
        print("To receive emails, you would need to use this email address for account registration")
        print("and wait for verification emails to arrive.")
        
    except Exception as e:
        print(f"Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_mail()