pipeline {
    agent any
    stages {

        stage("build") {
            steps {
                echo 'building the app'
            }
        }

        stage("test") {
            steps {
                echo 'testing the app'
                sh 'pytest app/tests/ -v -s -n 3'
            }
        }

        stage("deploy") {
            steps {
                echo 'deploying the app'
            }
        }
    }
}