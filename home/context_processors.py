from .models import Setting
def setting(request):
    setting = Setting.objects.get(pk=1)
    # return {'settings': setting}
    if setting:
        return {'setting': setting}