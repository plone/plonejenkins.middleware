
from pyramid.renderers import render


def create_jenkins_job_xml(displayname, git_url, git_branch, python_version, email_notification_recipients, buildout, node, url_to_callback=None, pull=None, ):

    command = """${python} bootstrap.py
bin/buildout -c ${buildout}
merge pull the pull request

bin/jenkins-alltests -1

    """
    
    result = render('plonejenkins.middleware:templates/plone.xml', {'':''})
