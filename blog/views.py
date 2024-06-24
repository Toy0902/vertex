import operator

from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from blog.forms import CommentForm
from blog.models import Rasmlar,Matn
from django.db.models import Q
from  functools import reduce



def index(request):
    rasm = Rasmlar.objects.all()
    matn = Matn.object.all()
    context = {
        "rasm": rasm,
        "matn": matn
    }
    return render(request, "index.html", context=context)


def index_detel(request, id):
    matn = get_object_or_404(Matn, id=id)
    comments = matn.comments.filter()
    comment_count = comments.count()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = matn
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
            'detel': matn,
            'comments': comments,
            'new_comments': new_comment,
            'comment_form': comment_form,
            'comments_count': comment_count
        }
    return render(request,'detel.html', context=context)




class SearchResultlist(ListView):
    model = Matn
    template_name = 'index.html'
    context_object_name = 'matn'

    def get_queryset(self):
        queryset = super().get_queryset()
        text = self.request.GET.get('query', None)
        if not text:
            return queryset
        text_ajratish = text.split(' ')
        text_ol = reduce(operator.and_,
        (Q(nomi__icontains=i) | Q(text__icontains=i) for i in text_ajratish))
        return queryset.filter(text_ol)

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     queryset = self.get_queryset()
    #
    #
    #     if queryset.exists():
    #         asosiy_matn_id = queryset.values_list('id', flat=True)
    #         oxshash_matnlar = Matn.objects.filter(
    #             Q(nomi__in=queryset.values_list('nomi', flat=True))
    #
    #         ).exclude(id__in=asosiy_matn_id)
    #     else:
    #         oxshash_matnlar = Matn.objects.none()
    #
    #     context['oxshahsh_matnlar'] = oxshash_matnlar
    #     return context

def news_detail(request, matn):
    matn = get_object_or_404(Matn, slug=matn, status=Matn.Status.Published)
    context = {}
    hit_count = get_hitcount_model().object.get_for_object(matn)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk':hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    comments = matn.comments.filter(active=True)
    new_comment = None
