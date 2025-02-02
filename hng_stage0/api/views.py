from django.shortcuts import render

# Create your views here.

# view to handle GET request and return the required JSON response.

from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    if request.method == 'GET':
        data = {
            "email": "christineoyiera51@gmail.com",
            "current_datetime": datetime.utcnow().isoformat() + "Z",
            "github_url": "https://github.com/clencyc/Backend-HNG"
        }
        return JsonResponse(data, status=200)
    
if __name__ == "__main__":
    app.run(debug=True)