from app import app

# This is the handler that Vercel calls
def handler(request, context):
    return app(request, context)