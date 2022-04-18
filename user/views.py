from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.views.generic import DetailView 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)
    
    
class ShowProfilePageView(DetailView):
	model = profile
	template_name = 'users/userprofile.html'

	def get_context_data(self, *args, **kwargs):
		users = profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs )
		page_user = get_object_or_404(profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context
