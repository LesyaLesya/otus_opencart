pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                echo 'Building docker image with tag tests'
                sh '${DOCKER_PATH} build -t tests .'
            }
        }
        stage('TestRun') {
            steps {
                echo 'Running tests in container'
                sh '''
                   if [ "$MARKER" == "all" ]
                   then
                   ${DOCKER_PATH} run --name my_container tests --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   else
                   ${DOCKER_PATH} run --name my_container tests --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES} -m ${MARKER}
                   fi
                '''
            }
        }
    }

    post {

        always {
            echo 'Copying allure report from container'
            sh '${DOCKER_PATH} cp my_container:/otus_opencart/allure-results .'

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
