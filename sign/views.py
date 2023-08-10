from datetime import datetime
from _thread import start_new_thread

import subprocess
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .Gesture import *
# Create your views here.
from sign.models import *
from .sampleeeeee import generate_video

def main(request):
    return render(request,'index.html')

@login_required(login_url='/')
def addstaff(request):
    return render(request,'admin/add.html')

@login_required(login_url='/')
def block(request):
    return render(request,'admin/blockunblock.html')

@login_required(login_url='/')
def adminhome(request):
    return render(request,'admin/home page.html')

@login_required(login_url='/')
def staffmanage(request):
    ob=staff.objects.all()
    return render(request,'admin/managestaff.html',{'val':ob})

@login_required(login_url='/')
def vwapprparent(request):
    ob=parent.objects.all()
    return render(request,'admin/viewparentsandapprove.html',{'val':ob})


@login_required(login_url='/')
def acceptparent(request,id):
    ob=login.objects.get(id=id)
    ob.type='parent'
    ob.save()
    messages.success(request,'accepted')
    return HttpResponse('''<script>window.location='/vwapprparent#about'</script>''')


@login_required(login_url='/')
def rejectparent(request,id):
    ob=login.objects.get(id=id)
    ob.type='reject'
    ob.save()
    messages.success(request, 'rejected')
    return HttpResponse('''<script>window.location='/vwapprparent#about'</script>''')


@login_required(login_url='/')
def pblock(request,id):
    ob=login.objects.get(id=id)
    ob.type='blocked'
    ob.save()
    messages.success(request, 'blocked')
    return HttpResponse('''<script>window.location='/block#about'</script>''')

@login_required(login_url='/')
def punblock(request,id):
    ob=login.objects.get(id=id)
    ob.type='parent'
    ob.save()
    messages.success(request, 'unblocked')
    return HttpResponse('''<script>window.location='/block#about'</script>''')


@login_required(login_url='/')
def sblock(request,id):
    ob=login.objects.get(id=id)
    ob.type='blocked'
    ob.save()
    messages.success(request, 'blocked')
    return HttpResponse('''<script>window.location='/block#about'</script>''')


@login_required(login_url='/')
def sunblock(request,id):
    ob=login.objects.get(id=id)
    ob.type='staff'
    ob.save()
    messages.success(request, 'unblocked')
    return HttpResponse('''<script>alert("unblocked");window.location='/block#about'</script>''')



@login_required(login_url='/')
def vwrating(request):
    ob=staff.objects.all()
    return render(request,'admin/viewrating.html',{'val':ob})


@login_required(login_url='/')
def staffrating(request):
    staffs=request.POST['select']
    obb=rating.objects.filter(sid__id=staffs)
    ob = staff.objects.all()
    return render(request, 'admin/viewrating.html', {'val':ob,'val1': obb})


@login_required(login_url='/')
def blocking(request):
    type=request.POST['select']
    if type=='parent':
        ob=parent.objects.all()
        return render(request, 'admin/blockunblock.html', {'val': ob,'s':type})
    else:
        ob=staff.objects.all()
        return render(request, 'admin/blockunblock.html', {'val': ob,'s':type})



@login_required(login_url='/')
def vwmaterials(request):
    ob=stdymtrls.objects.all()
    return render(request,'admin/viewstdymtrls.html',{'val':ob})

@login_required(login_url='/')
def vwtips(request):
    ob=tips.objects.all()
    return render(request,'admin/viewtips.html',{'val':ob})

@login_required(login_url='/')
def chatwithstaff(request):
    ob=staff.objects.all()
    return render(request,'parent/chat.html',{'val':ob})


@login_required(login_url='/')
def staffchat(request, id):
    ob = staff.objects.get(lid__id=id)
    request.session['staffid'] = id
    print(id,request.session['lid'],"=================")
    from django.db.models import Q
    obb = chat.objects.filter(Q(pid=request.session['lid'], sid=request.session['staffid']) | Q(sid=request.session['lid'], pid=request.session['staffid'])).order_by('id')
    print(obb,"=============================================")
    return render(request, 'chat2.html', {'val': ob, 'data': obb, 'fr': request.session['lid'],'name':ob.fname+" "+ob.lname})

@login_required(login_url='/')
def chat_s(request):
    msg = request.POST['textarea']
    ob = chat()
    ob.pid = login.objects.get(id=request.session['lid'])
    ob.sid = login.objects.get(id=request.session['staffid'])
    ob.date = datetime.today()
    ob.message = msg
    ob.save()
    return redirect('/red_c')

@login_required(login_url='/')
def red_c(request):
    ob = staff.objects.get(lid__id=request.session['staffid'])
    from django.db.models import Q
    obb = chat.objects.filter(Q(pid=request.session['lid'], sid=request.session['staffid']) | Q(sid=request.session['lid'], pid=request.session['staffid'])).order_by('id')
    print(obb,"=============================================")
    return render(request, 'chat2.html', {'val': ob, 'data': obb, 'fr': request.session['lid'],'name':ob.fname+" "+ob.lname})



@login_required(login_url='/')
def parenthome(request):
    return render(request,'parent/homepage.html')



def parentreg(request):
    return render(request,'registerindex.html')


@login_required(login_url='/')
def sendrating(request):
    ob=staff.objects.all()
    return render(request,'parent/rating.html',{'val':ob})

@login_required(login_url='/')
def sendfdbk(request):

    ob = staff.objects.all()
    return render(request, 'parent/sendfeedback.html', {'val':ob})



@login_required(login_url='/')
def vwmtrls(request):
    ob=stdymtrls.objects.all()
    return render(request,'parent/viewstdymtrl.html',{'val':ob})


@login_required(login_url='/')
def parentvwtips(request):
    ob=tips.objects.all()
    return render(request,'parent/viewtips.html',{'val':ob})


@login_required(login_url='/')
def vwclasswork(request):
    ob = classwork.objects.all()
    return render(request, 'parent/viewclasswork.html',{'val':ob})



@login_required(login_url='/')
def manageclswrk(request):
    ob = classwork.objects.filter(sid__lid__id=request.session['lid'])
    return render(request, 'staff/manageclasswork.html',{'val':ob})

@login_required(login_url='/')
def addclswrk(request):
    return render(request, 'staff/addworks.html')



@login_required(login_url='/')
def managematerials(request):
    ob=stdymtrls.objects.filter(sid__lid__id=request.session['lid'])
    return render(request,'staff/addmanagestdymtrls.html',{'val':ob})


@login_required(login_url='/')
def managetips(request):
    ob=tips.objects.filter(sid__lid__id=request.session['lid'])
    return render(request,'staff/addmanagetips.html',{'val':ob})


@login_required(login_url='/')
def addmaterials(request):
    return render(request,'staff/addstdymtrls.html')



@login_required(login_url='/')
def adtip(request):
    return render(request,'staff/addtips.html')



@login_required(login_url='/')
def chatwithparent(request):
    ob = parent.objects.all()
    return render(request,'staff/chats.html',{'val':ob})


@login_required(login_url='/')
def parentchat(request, id):
    ob = parent.objects.get(lid__id=id)
    request.session['parentid'] = id
    print(id,request.session['lid'],"=================")
    from django.db.models import Q
    obb = chat.objects.filter(Q(sid=request.session['lid'], pid=request.session['parentid']) | Q(pid=request.session['lid'], sid=request.session['parentid'])).order_by('id')
    print(obb,"=============================================")
    return render(request, 'chat3.html', {'val': ob, 'data': obb, 'fr': request.session['lid'],'name':ob.fname+" "+ob.lname})


@login_required(login_url='/')
def chat_p(request):
    msg = request.POST['textarea']
    ob = chat()
    ob.sid = login.objects.get(id=request.session['parentid'])
    ob.pid = login.objects.get(id=request.session['lid'])
    ob.date = datetime.today()
    ob.message = msg
    ob.save()
    return redirect('/red_c2')



@login_required(login_url='/')
def red_c2(request):
    ob = parent.objects.get(lid__id=request.session['parentid'])
    from django.db.models import Q
    obb = chat.objects.filter(Q(sid=request.session['lid'], pid=request.session['parentid']) | Q(pid=request.session['lid'], sid=request.session['parentid'])).order_by('id')
    print(obb,"=============================================")
    return render(request, 'chat3.html', {'val': ob, 'data': obb, 'fr': request.session['lid'],'name':ob.fname+" "+ob.lname})








@login_required(login_url='/')
def staffhome(request):
    return render(request,'staff/homepage.html')


@login_required(login_url='/')
def staffvwfdbck(request):
    ob = feedback.objects.filter(sid__lid__id=request.session['lid'])
    return render(request,'staff/viewfeedbackk.html',{'val':ob})


@login_required(login_url='/')
def staffvwparents(request):
    ob=parent.objects.all()
    return render(request,'staff/viewparents.html',{'val':ob})


@login_required(login_url='/')
def staffvwrating(request):
    ob = rating.objects.filter(sid__lid__id=request.session['lid'])
    return render(request,'staff/viewrating.html',{'val':ob})



def reg(request):
    fnam=request.POST['textfield']
    lnam=request.POST['textfield2']
    plce = request.POST['textfield3']
    addr = request.POST['textarea']
    ph = request.POST['textfield4']
    mail = request.POST['textfield5']
    uname=request.POST['textfield6']
    pw=request.POST['textfield7']

    ob=login()
    ob.username=uname
    ob.password=pw
    ob.type='pending'
    ob.save()

    ob2=parent()
    ob2.fname=fnam
    ob2.lname=lnam
    ob2.place=plce
    ob2.address=addr
    ob2.phno=ph
    ob2.email=mail
    ob2.lid=ob
    ob2.save()
    messages.success(request, 'registered')
    return HttpResponse('''<script>window.location='/'</script>''')



def logincode(request):
    uname=request.POST['textfield']
    pw=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=pw)
        if ob.type=='admin':
            ob1=auth.authenticate(username='admin',password='admin')
            auth.login(request,ob1)
            messages.success(request,'Welcome to admin home page')
            return HttpResponse('''<script>window.location='/adminhome'</script>''')
        elif ob.type=='parent':

            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'Welcome to user home page')
            return HttpResponse('''<script>window.location='/parenthome'</script>''')
        elif ob.type == 'staff':

            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'Welcome to staff home page')
            return HttpResponse('''<script>window.location='/staffhome'</script>''')
        else:
           messages.success(request, 'Incorrect details')
           return HttpResponse('''<script>alert("Incorrect details");window.location='/'</script>''')
    except:
       messages.success(request, 'Incorrect details')
       return HttpResponse('''<script>window.location='/'</script>''')


@login_required(login_url='/')
def staffreg(request):
    sfnam = request.POST['textfield']
    slnam = request.POST['textfield2']
    splce = request.POST['textfield3']
    sph = request.POST['textfield4']
    smail = request.POST['textfield5']
    suname = request.POST['textfield6']
    spw = request.POST['textfield7']
    ob = login()
    ob.username = suname
    ob.password = spw
    ob.type = 'staff'
    ob.save()
    ob2 = staff()
    ob2.fname = sfnam
    ob2.lname = slnam
    ob2.place = splce
    ob2.phno = sph
    ob2.email = smail
    ob2.lid = ob
    ob2.save()
    messages.success(request, 'registered')
    return HttpResponse('''<script>window.location='/staffmanage#about'</script>''')


@login_required(login_url='/')
def addtipcode(request):
     tp=request.POST['textarea']

     ob=tips()
     ob.tips=tp
     ob.date=datetime.today()
     ob.sid=staff.objects.get(lid__id=request.session['lid'])
     ob.save()
     messages.success(request, 'added')
     return HttpResponse('''<script>window.location='/managetips#about'</script>''')

@login_required(login_url='/')
def addstdymtrlscode(request):
    flname=request.POST['textfield']
    fl=request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(fl.name,fl)
    ob=stdymtrls()
    ob.name=flname
    ob.file=fp
    ob.date = datetime.today()
    ob.sid=staff.objects.get(lid__id=request.session['lid'])
    ob.save()
    messages.success(request, 'added')
    return HttpResponse('''<script>window.location='/managematerials#about'</script>''')


@login_required(login_url='/')
def sendfeedbackcode(request):
    fb=request.POST['textarea']
    staffs=request.POST['select']
    ob=feedback()
    ob.feedback=fb
    ob.date=datetime.today()
    ob.pid=parent.objects.get(lid__id=request.session['lid'])
    ob.sid=staff.objects.get(id=staffs)
    ob.save()
    messages.success(request, 'feedback sent')
    return HttpResponse('''<script>window.location='/sendfdbk#about'</script>''')

@login_required(login_url='/')
def genvideo(request):
    txt=request.POST['textarea']
    fn=generate_video(txt)
    print(fn,"ggggggggg")
    return render(request,"parent/viewvideo.html",{"fn":fn})

@login_required(login_url='/')
def loadvideo(request):
    return render(request,"parent/txt_to_video.html")
def cam_check():
    subprocess.call(
        ['python.exe',  r'E:\django\signlanguage\sign\Gesture1.py' ])

    # gc1 = GestureController()
    # gc1.start()
@login_required(login_url='/')
def loadcam(request):
    start_new_thread(cam_check, ())

    return HttpResponse('''<script>window.location='/parenthome'</script>''')


@login_required(login_url='/')
def srating(request):
    rt=request.POST['select2']
    rw=request.POST['textarea']
    staffs = request.POST['select']
    ob=rating()
    ob.rating=rt
    ob.review=rw
    ob.date=datetime.today()
    ob.pid = parent.objects.get(lid__id=request.session['lid'])
    ob.sid = staff.objects.get(id=staffs)
    ob.save()
    messages.success(request, 'rating and review sent')
    return HttpResponse('''<script>window.location='/sendrating#about'</script>''')


@login_required(login_url='/')
def editstaff(request,id):
    ob=staff.objects.get(id=id)
    request.session['sid']=id
    return render(request,'admin/edit.html',{'val':ob})


@login_required(login_url='/')
def editcode(request):
    stfnam = request.POST['textfield']
    stlnam = request.POST['textfield2']
    stplce = request.POST['textfield3']
    stph = request.POST['textfield4']
    stmail = request.POST['textfield5']
    ob=staff.objects.get(id=request.session['sid'])
    ob.fname = stfnam
    ob.lname = stlnam
    ob.place = stplce
    ob.phno = stph
    ob.email = stmail
    ob.save()
    messages.success(request, 'edited')
    return HttpResponse('''<script>window.location='/staffmanage#about'</script>''')


@login_required(login_url='/')
def deletestaff(request,id):
    ob=staff.objects.get(lid__id=id)
    ob.delete()
    iob=login.objects.get(id=id)
    iob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/staffmanage#about'</script>''')

@login_required(login_url='/')
def tpedit(request,id):
    ob = tips.objects.get(id=id)
    request.session['sid'] = id
    return render(request,'staff/edittip.html',{'val': ob})

@login_required(login_url='/')
def tipeditcode(request):
    tipp= request.POST['textarea']
    ob = tips.objects.get(id=request.session['sid'])
    ob.tips=tipp
    ob.date=datetime.today()
    ob.save()
    messages.success(request, 'edited')
    return HttpResponse('''<script>window.location='/managetips#about'</script>''')

@login_required(login_url='/')
def deletetip(request,id):
    ob=tips.objects.get(id=id)
    ob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/managetips#about'</script>''')


@login_required(login_url='/')
def sedit(request,id):
    ob = stdymtrls.objects.get(id=id)
    request.session['sid'] = id
    return render(request,'staff/editstdymtrl.html',{'val': ob})


@login_required(login_url='/')
def seditcode(request):
    try:

        ename= request.POST['textfield']
        efile = request.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(efile.name, efile)
        ob = stdymtrls.objects.get(id=request.session['sid'])
        ob.name=ename
        ob.file = fp
        ob.date=datetime.today()
        ob.save()
        messages.success(request, 'edited')
        return HttpResponse('''<script>window.location='/managematerials#about'</script>''')
    except:
        ename = request.POST['textfield']

        ob = stdymtrls.objects.get(id=request.session['sid'])
        ob.name = ename

        ob.date = datetime.today()
        ob.save()
        messages.success(request, 'edited')
        return HttpResponse('''<script>window.location='/managematerials#about'</script>''')


@login_required(login_url='/')
def sdelete(request,id):
    ob=stdymtrls.objects.get(id=id)
    ob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/managematerials#about'</script>''')

@login_required(login_url='/')
def workdelete(request,id):
    ob=classwork.objects.get(id=id)
    ob.delete()
    messages.success(request, 'deleted')
    return HttpResponse('''<script>window.location='/manageclswrk#about'</script>''')

@login_required(login_url='/')
def addworkcode(request):
    wr = request.POST['textarea']
    sub = request.POST['textfield']
    ob = classwork()
    ob.works = wr
    ob.subject= sub
    ob.date = datetime.today()
    ob.sid = staff.objects.get(lid__id=request.session['lid'])
    ob.save()
    messages.success(request, 'added')
    return HttpResponse('''<script>window.location='/manageclswrk#about'</script>''')


def logout(request):
    auth.logout(request)
    return render(request,'index.html')











