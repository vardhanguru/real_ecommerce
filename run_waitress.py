#!/usr/bin/env python
"""
Waitress server runner for Django application
Run this script to start the application with Waitress WSGI server
"""

import os
import sys
import django
from django.conf import settings
from django.core.management import call_command
from waitress import serve

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')

# Setup Django
django.setup()

# Import WSGI application after Django setup
from ecommerce_project.wsgi import application

if __name__ == '__main__':
    # Run migrations (optional - comment out if you prefer to run manually)
    print("Running migrations...")
    call_command('migrate', verbosity=1)
    
    # Collect static files (optional - for production-like setup)
    print("Collecting static files...")
    call_command('collectstatic', verbosity=0, interactive=False)
    
    # Start Waitress server
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    
    print(f"\n{'='*60}")
    print(f"Starting Waitress server at http://{host}:{port}")
    print(f"{'='*60}\n")
    
    serve(application, host=host, port=port, _quiet=False)
