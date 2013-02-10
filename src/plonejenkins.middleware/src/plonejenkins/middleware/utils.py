from datetime import datetime
from lxml import etree
import StringIO


def add_log(request, who, message):
    f = open(request.registry.settings['log_file'], 'w+')
    m = who + " " + message + str(datetime.now()) + '\n'
    f.write(m)
    f.close()


def jenkins_job(request, job, url_to_callback, params=None):
    """
    Generic jenkins call job
    """

    # First we check if the job exists
    if not request.jenkins.job_exists(job):
        # we create the job
        pass

    # We are going to reconfigure the job
    xml_config = request.jenkins.get_job_config(job)
    f = StringIO(xml_config)
    xml_object = etree.parse(f)
    endpoint = xml_object.parse('/project/properties/com.tikal.hudson.plugins.notification.HudsonNotificationProperty/endpoints/com.tikal.hudson.plugins.notification.Endpoint/url')
    if len(endpoint) == 1:
        endpoint.text = url_to_callback

    # We are going to add a publisher call to url

    # <properties>
    #   <com.tikal.hudson.plugins.notification.HudsonNotificationProperty plugin="notification@1.4">
    #     <endpoints>
    #       <com.tikal.hudson.plugins.notification.Endpoint>
    #         <protocol>HTTP</protocol>
    #         <url>http://localhost:6543/callback/corecommit?commit_hash=999</url>
    #       </com.tikal.hudson.plugins.notification.Endpoint>
    #     </endpoints>
    #   </com.tikal.hudson.plugins.notification.HudsonNotificationProperty>
    # </properties>

    xml_reconfig = etree.tostring(xml_object)
    request.jenkins.reconfig_job(job, xml_reconfig)

    request.jenkins.build_job(job, params)

