from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def team(request):
    teamname = int(request.GET["teamnumber"])

    if teamname == 4:
        result = "최고의 팀이네요"
    else:
        result = "친해지고 싶어요"

    return render(request, "team.html", {"result" : result})