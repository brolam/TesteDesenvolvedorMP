from django.shortcuts import render
from candidates.forms import EvaluationForm
from candidates.models import SKILL_TECHNOLOGY_RATING_CHOICES 

def evaluation_new(request):
    form = None
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_all_emails_with_evaluation()
            return render(request, 'evaluation/show.html', {'email': form.instance.email})
    else:
        form = EvaluationForm()
    return render(request, 'evaluation/new.html', 
    		{
    			'form': form, 
    			'SKILL_TECHNOLOGY_RATING_CHOICES': SKILL_TECHNOLOGY_RATING_CHOICES,  
    		}
    	)