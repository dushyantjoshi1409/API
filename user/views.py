from django.shortcuts import render
import requests
def index(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    print(users)
    return render(request, "index.html", {"users": users})
# Create your views here.

def all_country(request):
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()
    return render(request, "all_country.html", {"countries": countries})

import requests
from django.shortcuts import redirect

def search_view(request):
    search_query = request.GET.get('query', '')
    if search_query:
        response = requests.get(f'https://restcountries.com/v3.1/name/{search_query}')
        if response.status_code == 200:
            countries = response.json()
            # Assuming you want to redirect to a detail page for the first matching country
            if countries:
                return redirect('country_detail', country_code=countries[0]['cca3'])
    
    # If no query or no results, you might want to render a search page or redirect elsewhere
    return render(request, 'search.html', {'error': 'No results found'})
