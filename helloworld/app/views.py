from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



def detail(request):
    return HttpResponse("You're looking at question %s." % request)


@csrf_exempt
@require_POST
def handle_jenkins_server_webhooks(request):
    print(request.__dict__," is request \n\n")
    print(request.body," is request body \n\n")
    payload = json.loads(request.body)
    print(payload, " is payload \n\n")
    if 'ref_type' in payload and payload['ref_type'] == 'tag':
            branch_name = payload['ref'].split("release")[0][:-1]
    else:
        ref_key = 'ref'
        ref = payload[ref_key]
        print(ref," is ref")
        branch_name = ref.replace("refs/heads/", "").replace("refs/tags/", "")
    if branch_name not in ['master', 'beta', 'int-beta', 'prod-1.7']:
        return HttpResponse(status=400)
    
    contains_migration = ''
    added_files = list()
    for commit in payload["commits"]:
        added_files.extend(commit["added"])

    for file_name in added_files:
        if "migrations" in file_name:
            contains_migration = 'true'
            break

    print(contains_migration," is contains_migration")
    command = """curl -X POST http://jenkins_api:119b7414e30b8d610b40e3574ccf32a829@localhost:8080/job/server/build/\?token\=1234 --data-urlencode json='{"parameter": [{"name":"BRANCH_NAME", "value":"%s"}, {"name":"CONTAINS_MIGRATION", "value":"%s"}]}' -H "Jenkins-Crumb:ff5591471489a19aa6cf1f0e51c899c14acf538a294ec15f2e7a7c00f3140071" """ % (branch_name, contains_migration)
    print('MY COMMAND ',command)
    os.system(command)
    return HttpResponse(status=200)


    