from jenkinsapi.jenkins import Jenkins


class InsertJobs:

    def get_server_instance(self):
        jenkins_url = 'http://jenkins_host:8080'
        server = Jenkins(jenkins_url, username='foouser',
                         password='foopassword')
        return server

    def get_job_details(self):
        server = self.get_server_instance()
        
        pass
