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
        stage('Deploy') {
            steps {
                sh 'sudo scp -tt -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no -r cal.py ec2-user@54.144.36.26'
                sh 'sudo ssh -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no ec2-user@ec2-54-144-36-26.compute-1.amazonaws.com'
            }
        }
    }
}
