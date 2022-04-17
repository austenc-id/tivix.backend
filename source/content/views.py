from django.shortcuts import redirect
from .request import OMDb

def search(request, query, quantity):
    requestor = OMDb(query, quantity)
    results = requestor.search()
    search = requestor.save(results)

    return redirect(f'/api/galleries/{search.id}')
