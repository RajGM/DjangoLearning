from django.http import HttpResponse
from django.conf.urls import path
from django.urls import path
from django.conf import settings
import sys

settings.configure(
    DEBUG=TRUE,
    SECRET_KEY='THIsIsSecretKey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middle.common.CommonMiddleware',
        'django.middle.csrf.CsrfViewMiddleware',
        'django.middle.clickjacking.XFrameOptions.Middleware'
    )
)

def index(request):
    return HttpRespnse('<html><head><nody>HELLO This is a light weight Django server</body></head></html')

urlpatterns = [
    path('',index)
]

if __name__== "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)