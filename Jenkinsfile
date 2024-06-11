pipeline {


environment {
    PATH = "$PATH:/usr/local/bin"
  }
    agent any

    stages {
        stage('TestRun') {
            steps {
                echo 'Run tests via docker-compose'
                sh 'docker-compose -f docker-compose.tests.yml up'
            }
        }

    }

    post {

        always {
            echo 'Copying allure report from container'
            sh 'docker-compose -f docker-compose.tests.yml run tests /bin/sh -c "allure generate allure-results --clean -o allure-report"'

            script {
                allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                ])
            }
            echo 'Deleting container and image'
            sh 'docker system prune -f'
            sh 'docker image rm tests'


            cleanWs()
        }
    }
}
