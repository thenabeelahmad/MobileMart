from django.db import connection
from django.shortcuts import render,redirect
# from django.core.files.storage import FileSystemStorage

def addcomp(request):
    if request.method=="POST":
        com=request.POST['comp']
        c=connection.cursor()
        c.execute(f"""insert into company set name='{com}'""")
        return redirect('addcompany')


        
    return render(request,"company/addcomp.html")    

def addmob(request):
    if request.method=="POST":
        com=request.POST['company']
        m=request.POST['model']
        ro=request.POST['rom']
        ra=request.POST['ram']
        pr=request.POST['price']
        # myfile = request.FILES['pic']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # fill = fs.url(filename)
        
        c=connection.cursor()
        print(c)
        c.execute(f"""insert into mobile set company='{com}',model='{m}',rom='{ro}',ram='{ra}',price='{pr}' """)
               
        return redirect('addmobile')


        
    return render(request,"company/addmob.html") 

def moblist(request):
    query=connection.cursor()
    query.execute("select * from mobile ")
    s=query.fetchall()
    return render(request,"company/moblist.html",{'data':s})

def mobdetail(request,u):
    query=connection.cursor()
    query.execute(f"select * from mobile where model='{u}'")
    s=query.fetchone()
    return render(request,"company/mobdetail.html",{'data':s}) 

def addtoc(request):
    query=connection.cursor()
    query.execute(f"select * from mobile where company='{k}'")
    s=query.fetchone()
    return render(request,"company/addtocart.html",{'data':s}) 


def filtermobile(request):
    if request.method=="POST":
       compani=request.POST['brand']
       c=connection.cursor()
       c.execute(f"""select * from mobile where company like '%{compani}%'  """)
       s=c.fetchall()
       return render(request,"company/filtermobile.html",{'data':s})
    return render(request,"company/filtermobile.html")
    
    
