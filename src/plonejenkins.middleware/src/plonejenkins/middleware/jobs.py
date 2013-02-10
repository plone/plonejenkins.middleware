
from pyramid.renderers import render


def create_jenkins_job_xml(displayname,
                           python_version,
                           email_notification_recipients,
                           buildout='jenkins.cfg',
                           node='Slave',
                           git_branch=None,
                           git_url='git://github.com/plone/buildout.coredev.git',
                           url_to_callback=None,
                           pull=None):

    command = """${python} bootstrap.py
bin/buildout -c ${buildout}
merge pull the pull request

bin/jenkins-alltests -1

    """
    
    result = render('plonejenkins.middleware:templates/plone.xml', {'':''})
