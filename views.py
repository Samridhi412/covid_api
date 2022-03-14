from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "bcb788bf94mshc6cd115fcd27082p1c5d0bjsn27503b606948",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
def home(req):
    if req.method=="POST":
        selectedcountry=req.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'selectedcountry':selectedcountry,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(req,'corona.html',context)
    noofresults=int(response['results'])
    mylist=[]
    for x in range(0,noofresults):
        # print(response['response'][x]['country'])
        mylist.append(response['response'][x]['country'])
    # print(mylist)
    context={'mylist':mylist}
    # context={'response':response}
    return render(req,'corona.html',context)
# Create your views here.
