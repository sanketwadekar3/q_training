pipeline {
    agent any
    //CheckoutSCM step is used to get the files from git repository to jenkins
    stages {
        stage('CheckoutSCM') {
            steps {
                checkout scm
            }
        }
        //First stage is Build
        //This is used to install python and then create virtual environment
        //Then activate virtual environment and install the requirements
        stage('Build') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install python3.6'
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip3 install -r requirements.txt'
            }
        }
        //Second stage is Test
        //This is used to Unit test the python file
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_cal.py'
            }
        }
        //Third stage is Deploy
        //This is used for dynamically copy files from jenkins to another ec2 instance
        //Then SSH into the another ec2 instance
        //Then install python and create virtual environment and activate it
        //Then install the requirements and test the python file using unittest
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