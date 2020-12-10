node {
    def env_vars = [
   'IN_DOCKER_CONTAINER=true']

    def source_dir = "${env.WORKSPACE}@script/"

    stage('Build Image') {
        dir(source_dir) {
        echo 'building image'
        sh 'docker build . --tag myimg'
        }
    }

    stage("test") {

            dir(source_dir) {
                docker.image('server/image'){
                    echo 'testing the app'
                    sh 'pytest app/tests/ -v -s -n 3'
                    echo 'tested the app'
                    }
            }
    }

    stage("deploy") {
        steps {
            echo 'deploying the app'
        }
    }

}



