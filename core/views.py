from django.shortcuts import render
from django.views import generic
from core.models import Post
from core.forms import PostForm

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse_lazy
from templated_email import send_templated_mail


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class ContatoView(generic.TemplateView):
    template_name = "core/contato.html"

    def post(self,request, *args, **kwargs):
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        assunto=request.POST.get('assunto')
        mensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['vitor.333.martins@gmail.com'],
        context={
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'assunto':assunto,
            'mensagem':mensagem
        },)
        return HttpResponseRedirect(reverse_lazy("core:contato"))


class CreatePostView(generic.CreateView):
    template_name = "core/create-post.html"
    models = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('core:index')

    def get_initial(self):
        return {'author': self.request.user}