from django.shortcuts import render

from django.http import HttpResponse

from django.db import connection

def hello_world(request):
    return HttpResponse("Hello World")

def index(request):
    key = '123'
    name = request.POST.get('name')
    no = request.POST.get('no')
    all = request.POST.get('all')
    nname = request.POST.get('nname')
    nno = request.POST.get('nno')
    ngrade = request.POST.get('ngrade')
    result = {}
    result['s'] = False
    result['n'] = False
    result['all'] = False
    result['insert'] = False
    cursor = connection.cursor()
    if name:
        result['s'] = True
        sql = "select Sname, Sno, AES_DECRYPT(UNHEX(Grade),'{}') from S " \
              "where S.Sname='{}'".format(key, name)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result['sr'] = rows
        result['sn'] = name
    elif no:
        result['n'] = True
        sql = "select Sname, Sno, AES_DECRYPT(UNHEX(Grade),'{}') from S " \
              "where S.Sno='{}'".format(key, no)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result['sr'] = rows
        result['sn'] = no
    elif nname and nno and ngrade:
        sql = "insert into S (Sname, Sno, Grade)" \
              "values ('{}', '{}', HEX(AES_ENCRYPT('{}','{}')))".format(nname, nno, ngrade, key)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result['insert'] = True
    elif all == 'all':
        result['all'] = True
        sql = "select Sname, Sno, AES_DECRYPT(UNHEX(Grade),'{}') from S where 1".format(key)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result['sr'] = rows
        result['sn'] = '所有学生'
    return render(request, 'index.html', result)
