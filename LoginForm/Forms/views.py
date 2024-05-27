from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from Forms.models import Studentform
from Forms.forms import Studentform_Form


def Register(request):  
    context={}
    if request.method=="GET":
        return render(request,'register.html')
    else:
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        mail=request.POST['email']
        user=request.POST['uname']
        p=request.POST['pwd']
        cp=request.POST['cpwd']
        
        if user =='' or p =='' or cp =='' or f_name =='' or mail == '' or l_name == '':
            context['errmsg']="Fields cannot be empty"
            return render(request,'register.html',context)
        elif p!=cp:
            context['errormsg']="Password and confirm password does not match"
            return render(request,'register.html',context)
        else:
            
            try:
                u=User.objects.create(first_name=f_name,last_name=l_name,email=mail,username=user)
                u.set_password(p)
                u.save()
                context['success']="User created successfully"
                subject = 'welcome to Ranjitha world'
                message = f'Hi {user.username}, thank you for registering in Ranjitha World.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'register.html',context)
            except Exception:
                context['Errmsg']="User already Exists"
                return render(request,'register.html',context)  
            
def user_login(request):
    context={}
    if request.method=="GET":
        return render(request,'login.html')
    else:
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        u=authenticate(username=uname,password=pwd)    
        if u is not None:
            login(request,u)
            return redirect('/index')
        else:
            context['errmsg']="Invalid user name and password "
            return render(request,'login.html',context)
        
def user_logout(request):
    logout(request)
    return redirect('/login')

def Index(request):
    return render(request,'index.html')


def Student_form(request):
    context={}
    if request.method=="GET":
        return render(request,'s_regform.html')
    else:
        name=request.POST['name']
        fn=request.POST['f_name']
        mn=request.POST['m_name']
        dob=request.POST['dob']
        #gen=request.POST=['gender']
        add=request.POST['address']
        mail=request.POST['email']
        m_no=request.POST['mobile']
        
        a=Studentform.objects.create(name=name,f_name=fn,m_name=mn,dob=dob,address=add,email=mail,m_no=m_no)
        a.save()
        context['success']="Registered successfully"
        return render(request,'s_regform.html',context) 
               
def Student_Details(request):
    a=Studentform.objects.all()
    context={}
    context['data']=a
    return render(request,'s_details.html',context)   
  
def Delete(request):
    a=Studentform.objects.get(id=id)
    a.delete()
    return render(request,'s_details.html') 
def Edit(request,id):
    a=Studentform.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        fn=request.POST['f_name']
        mn=request.POST['m_name']
        dob=request.POST['dob']
        #gen=request.POST=['gender']
        add=request.POST['address']
        mail=request.POST['email']
        m_no=request.POST['mobile']
        
        a.name=name
        a.f_name=fn
        a.m_name=mn
        a.dob=dob
        a.address=add
        a.email=mail
        a.mobile=m_no
        a.save()
        return redirect ('/s_details')
    return render(request,'s_regform.html',{'x':a})
        
def form(request):
    context={
    'st_form':Studentform_Form()
    }
    if request.method=='POST':
        a=Studentform_Form(request.POST)
        if a.is_valid():
           a.save()
    return render(request,'djangoform.html',context)       
