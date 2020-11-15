from django.shortcuts import render
from django.views import generic

from .models import User


#  generic 참조 : https://wayhome25.github.io/django/2017/05/02/CBV/
class ListView(generic.ListView):
    #  template_name = 'users/user_list.html'  # 디폴트 템플릿명: <app_label>/<model_name>_list.html
    #  context_object_name = 'question_list'  # 디폴트 컨텍스트 변수명 :  object_list. html파일과 맵핑되는 변수명
    #  paginate_by = 10 # 한 페이지에 보여줄 오브젝트의 갯수
    def get_queryset(self):
        return User.objects.all()


class DetailView(generic.DetailView):
    """
        DetailView 디폴트 지정 속성
        1) model 변수 : Model명 (URLConf 에서 pk 파라미터 값을 활용하여 DB 레코드 조회)
        2) 템플릿 파일 : user_detail.html (모델명소문자_detail.html)
        3) context_object_name = 'user' # 디폴트 컨텍스트 변수명 :  object
    """

    model = User # 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 담는다.
