import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='b95982ee54de4033a2081f8718bc46cb')

server.create_job('empty1', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)
my_job = server.get_job_config('cool-job')
print(my_job)
server.build_job('empty1')
server.reconfig_job('empty1', jenkins.RECONFIG_XML)
server.delete_job('empty1')
