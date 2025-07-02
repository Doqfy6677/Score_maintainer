from flask import Flask, request
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from the parent directory
from app import app

# Handler for Vercel serverless function
def handler(request, context):
    """Handle a request to the serverless function."""
    
    # Get the path from the request
    path = request.get('path', '/')
    
    # Create a test request context
    with app.test_request_context(
        path=path,
        method=request.get('method', 'GET'),
        headers=request.get('headers', {}),
        query_string=request.get('query', '')
    ):
        try:
            # Process the request
            response = app.full_dispatch_request()
            
            # Return the response
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data().decode('utf-8')
            }
        except Exception as e:
            # Return an error response
            return {
                'statusCode': 500,
                'body': str(e)
            }