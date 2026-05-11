"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# django에서 settings.pu에 설정한변수를 '안전하게' 불러오는 방법
from django.conf import settings
# 아, 파일이 저장된 path와 사용자에게 제공할 url을 적절히 처리할 수 있는 무언가
from django.conf.urls.static import static 

# 우리 프로젝트를 위한 모르음집인 urlpatterns리스트ㅔㅇ
# 미디어 (업로드된 정적 파일)을 제공할 수 있는 url을 추가할 것이다.
    # 방법은
    # MEDIA_ROOT 경로에 있는 파일을
    # MEDIA_URL를 사용하여 제공한다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)