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
            }
            sh 'pytest app/tests/ -v -s -n 3'
                step([$class: 'CoberturaPublisher',
                      autoUpdateHealth: false, autoUpdateStability: false,
                      coberturaReportFile: 'coverage.xml',
                      failUnhealthy: false, failUnstable: false,
                      maxNumberOfBuilds: 0, onlyStable: false,
                      sourceEncoding: 'ASCII', zoomCoverageChart: false])
             
        }

        stage("deploy") {
            steps {
                echo 'deploying the app'
            }
        }
    }
}