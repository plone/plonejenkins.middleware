# -*- encoding: utf-8 -*-
from cornice import Service
from plonejenkins.middleware.security import validatejenkins

callbackCommit = Service(name='Callback for commits', path='/callback/corecommit',
                    description="Callback for commits jobs on jenkins")


@callbackCommit.post()
@validatejenkins
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

    We are going to write on the comment

    """
    #import pdb; pdb.set_trace()
    answer = request.json_body()
    commit_hash = request.GET('commit_hash')
    # We connect to github to write something about this commits
    # /repos/plone/:repo/commits/:sha/comments
    commit = request.registry.settings['github'].get_commit(commit_hash)
    commit.create_comment('Hey!')