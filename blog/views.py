from django.shortcuts import render

# Create your views here.



def test(request):
    args = dict()
    # return render(request, 'test.html', args)
    return render(request, 'test_boot3.html', args)
