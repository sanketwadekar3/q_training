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
                sh '''
                sudo scp -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-app/cal.py ec2-user@184.72.93.180:/home/ec2-user
                sudo scp -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-app/test_cal.py ec2-user@184.72.93.180:/home/ec2-user
                sudo scp -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-app/requirements.txt ec2-user@184.72.93.180:/home/ec2-user
                sudo ssh -i "/var/lib/jenkins/sanket.pem" -o StrictHostKeyChecking=no ec2-user@184.72.93.180
                sudo apt-get update
                sudo apt-get install python3.6
                python3 -m venv env
                . env/bin/activate
                pip3 install -r requirements.txt
                python3 -m unittest test_cal.py
                '''
            }
        }
    }
}
