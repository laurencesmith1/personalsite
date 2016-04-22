from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import DecimalForm
from fractions import Fraction


# def dec2frac(request):
    # # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # # # create a form instance and populate it with data from the request:
        # form = DecimalForm(request.POST)
        # # # check whether it's valid:
        # if form.is_valid():
        # # # process the data in form.cleaned_data as required
            # dec = form.cleaned_data['dec']
            # dec = float(dec) - 1#first convert the number to a float, in case someone enters an integer
            # frac = Fraction(dec).limit_denominator()
            # # # redirect to a new URL:
            # # return HttpResponseRedirect('converter/result/')

    # # # if a GET (or any other method) we'll create a blank form
    # else:
        # frac="Sorry, there was an error"

    # return render(request, 'dec2frac/result.html', {'frac': frac})
    # #return render(request, 'result.html')
	
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DecimalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #print(form.cleaned_data['your_name'])
            # redirect to a new URL:
            return HttpResponseRedirect('/result/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DecimalForm()
        print(form)

    return render(request, 'name.html', {'form': form})

def result(request):
    # # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # # create a form instance and populate it with data from the request:
        form = DecimalForm(request.POST)
        # # check whether it's valid:
        if form.is_valid():
        # # process the data in form.cleaned_data as required		
            dec = form.cleaned_data['dec']
            dec2frac = float(dec) - 1#first convert the number to a float, in case someone enters an integer
            dec2frac = Fraction(dec2frac).limit_denominator()            
            
            try:
                frac = Fraction(form.cleaned_data['frac'])
                frac2dec = (frac.numerator/frac.denominator) + 1
            except ValueError:
                frac2dec="error"
            # # redirect to a new URL:
            # return HttpResponseRedirect('converter/result/')

    # # if a GET (or any other method) we'll create a blank form
    else:
        frac2dec="error"
        dec2frac="error"

    return render(request, 'result.html', {'dec': dec, 'frac': frac, 'frac2dec': frac2dec, 'dec2frac':dec2frac})
    #return render(request, 'result.html')