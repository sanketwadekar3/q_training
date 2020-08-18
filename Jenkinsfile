pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_cal.py'
            }
        }
    }
}
