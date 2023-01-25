from django.http import HttpResponse ,JsonResponse

def home_page(request):
    print("this is rest ")
    friends =[
        'ankit',
        'ravi',
        
        'uttam'
    ]
    return JsonResponse(friends, safe=False)
