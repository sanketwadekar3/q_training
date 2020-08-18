pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 cal.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}
