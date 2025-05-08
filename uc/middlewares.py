from django.shortcuts import render
from uc.models import UnderConstruction
from decouple import config

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
    #     print("This is before view")
    #     # response = self.get_response(request)
    #     response = render(request, "uc/maintenance.html")
    #     print("This is after view")
    #     return response

    def __call__(self, request):
        uc = UnderConstruction.objects.first()
        if request.user.is_staff:
            return self.get_response(request)  # get_response is a function to call the next step (middleware or view)
        
        sec_key = config("MAINTENANCE_BYPASS_KEY")   # config() is used to securely read values from a .env file
        if 'sk' in request.GET and request.GET['sk'] == sec_key:
            request.session['bypass_maintenance'] = True   # Custom session key to allow certain users pass maintenance
            request.session.set_expiry(0)   # session expires when the browser is closed.
        
        if request.session.get('bypass_maintenance', False):
            return self.get_response(request)
        
        try:
            if uc and uc.is_under_construction:
                context = {
                    'uc_note':uc.uc_note,
                    'uc_duration': uc.uc_duration,
                }
                return render(request, "uc/maintenance.html", context=context)
        except:
            pass
        return self.get_response(request)