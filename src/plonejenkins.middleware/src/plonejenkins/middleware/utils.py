from datetime import datetime
from lxml import etree


def add_log(request, who, message):
    print who + " " + message + str(datetime.now())


def jenkins_job(request, job, url_to_callback, params=None):

    # We are going to reconfigure the job
    xml_config = request.jenkins.get_job_config(job)
    xml_object = etree.XML(xml_config)


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

