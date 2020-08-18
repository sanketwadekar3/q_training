pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                sh 'python3 cal.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}