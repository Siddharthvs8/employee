# Create your views here.
from django . shortcuts import render,redirect,Http404,get_object_or_404
from.models import Employee
from .forms import EmployeeForm
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def welcome(request):
    #retfrom django.shortcuts import render,HttpResponse,redirect,get_object_or_404
    #return HttpResponse("hello geeks")
    emp=Employee.objects.all()
    print(emp)
    return render(request,"home.html",{'e':emp})
def add(request):
     return render(request,'add.html')
def add_all(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST or None)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print('hi')
            return redirect('/school/welcome/')
        else:
            # Do something in case if form is not valid
            raise Http404
        return redirect('/school/add/')
def update(request,sid):
    obj=get_object_or_404(Employee,pk=sid)
    form=EmployeeForm(request.POST or None, instance=obj)
    print(form)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/school/welcome/')
    return render(request,'update.html',{'employee':form})
def delete(request,sid):
    Employee.objects.filter(id=sid).delete()
    return redirect('/school/welcome/')
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/school/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/school/welcome")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/school/login")
