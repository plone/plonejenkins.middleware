# -*- encoding: utf-8 -*-
from cornice import Service
from plonejenkins.middleware.security import validatetoken

callbackCommit = Service(name='Callback for commits', path='/callback/corecommit',
                    description="Callback for commits jobs on jenkins")


@callbackCommit.post()
@validatetoken
def functionCallbackCommit(request):
    """
    When jenkins is finished it calls this url
    {"name":"JobName",
     "url":"JobUrl",
     "build":{"number":1,
        "phase":"STARTED",
        "status":"FAILED",
        "url":"job/project/5",
        "full_url":"http://ci.jenkins.org/job/project/5"
        "parameters":{"branch":"master"}
     }
    }
    """
    answer = request.json_body()
    commit_hash = request.GET('commit_hash')