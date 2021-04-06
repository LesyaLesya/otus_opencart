pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                echo 'Building docker image with tag tests'
                sh '/usr/local/bin/docker build -t tests .'
            }
        }
        stage('TestRun') {
            steps {
                echo 'Running tests in container'
                sh '''
                   if [ "$TESTS" == "ALL_TESTS" ]
                   then
                   /usr/local/bin/docker run --name my_container tests --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   elif [ "$TESTS" == "MAIN_PAGE" ]
                   then
                   /usr/local/bin/docker run --name my_container tests/test_main_page.py --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   elif [ "$TESTS" == "ADMIN_PAGE" ]
                   then
                   /usr/local/bin/docker run --name my_container tests/test_admin_page.py --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   elif [ "TESTS" == "CATALOGUE_PAGE" ]
                   then
                   /usr/local/bin/docker run --name my_container tests/test_catalogue_page.py --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   elif [ "TESTS" == "HEADER_PAGE" ]
                   then
                   /usr/local/bin/docker run --name my_container tests/test_header_page.py --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   elif [ "TESTS" == "LOGIN_PAGE" ]
                   then
                   /usr/local/bin/docker run --name my_container tests/test_login_page.py --url ${URL} --browser-name ${BROWSER_NAME} --browser-version ${BROWSER_VERSION} --executor ${EXECUTOR} -n ${NODES}
                   else
                   /usr/local/bin/docker run --name my_container tests/test_product_page.py --login ${LOGIN} --passw ${PASSW} -n ${NODES}  -m ${MARKER}
                   fi
                '''
            }
        }
    }

    post {

        always {
            echo 'Copying allure report from container'
            sh '/usr/local/bin/docker cp my_container:/otus_opencart/allure-results .'

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
            sh '/usr/local/bin/docker system prune -f'
            sh '/usr/local/bin/docker image rm tests'


            cleanWs()
        }
    }
}
