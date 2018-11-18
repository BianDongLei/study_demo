from django.shortcuts import render

# Create your views here.
from apps.index.models import noteInfo


def note_response(request):
    return render(request, "note.html")


def submit_form(request):
    if request is None:
        return
    # 表单提交时一定要先判断request的方法，request中有get方法与post的方法，
    # 如果使用前端使用get方法，POST数据将为空。
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        msg = request.POST.get("message", "")
        if name == "" or email == "" or address == "" or msg == "":
            pass
        else:
            note = noteInfo()
            note.name = name
            note.email = email
            note.address = address
            note.leave_msg = msg
            note.save()
    # all_msg = noteInfo.objects.filter(name="卞栋磊")
    # filter方法可以将数据库中所有name="卞栋磊"的数据记录都查询出来，
    # 保存为一个noteInfo列表，可以使用for in将列表中的noteInfo元素全部查询出来。
    # filter()方法也可以添加多个参数，即可查询所有符合这多个参数要求的所有记录。
    # for noteinfo in all_msg:
    #     print(noteInfo)
    #     noteInfo.delete() # 这里可以直接对noteinfo做删除或者修改操作
    emails = []
    addresses = []
    if name is not None or not name == "":
        filter_msg = noteInfo.objects.filter(name=name)
        num = filter_msg.__len__()
        for msgdetail in filter_msg:
            emaildetail = msgdetail.email
            addressdetail = msgdetail.address
            if emaildetail not in emails:
                emails.append(emaildetail)
            if addressdetail not in addresses:
                addresses.append(addressdetail)

    return render(request, "response.html", {"filter_msg": filter_msg, "num": num,
                                             "name": name, "emails": emails,
                                             "addresses": addresses})
