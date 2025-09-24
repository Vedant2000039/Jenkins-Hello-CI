pipeline {
    agent any   // Run on any available Jenkins agent

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 Hello.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment simulated - Hello CI project complete!'
            }
        }
    }
}
