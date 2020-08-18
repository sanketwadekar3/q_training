pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.6.9'
                }
            }
            steps {
                sh 'python3 cal.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}