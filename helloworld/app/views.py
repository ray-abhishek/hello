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
    # command = """curl -X POST http://jenkins_api:11b1053a6d889c33f1849ffcafdc0ff8c4@localhost:8080/job/server/build/\?token\=Ne6SmlAr2KSoQtNTOAJ0n5fDQUG8Wmw+D6iJhyI6OFo --data-urlencode   json='{"parameter": [{"name":"BRANCH_NAME", "value":"%s"}, {"name":"CONTAINS_MIGRATION", "value":"%s"}]}' -H "Jenkins-Crumb:dda15e90ce2e5fe9252d3d971b7700c3" """ % (branch_name, contains_migration)
    # log.info(command)
    # os.system(command)
    return HttpResponse(status=200)