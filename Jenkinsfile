pipeline {
    agent any

    stages {
        stage('TestRun') {
            steps {
                echo 'Run tests via docker-compose'
                sh '${DOCKER_PATH} -f docker-compose.tests.yml up'
            }
        }

    }

    post {

        always {
            echo 'Copying allure report from container'
            sh '${DOCKER_PATH} -f docker-compose.tests.yml run tests /bin/sh -c "allure generate allure-results --clean -o allure-report"'

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
            sh '${DOCKER_PATH} system prune -f'
            sh '${DOCKER_PATH} image rm tests'


            cleanWs()
        }
    }
}
