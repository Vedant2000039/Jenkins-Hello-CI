pipeline {
    agent any
    triggers {
        // Run every day at 9:00 AM
        cron('* * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }
        stage('Run Script') {
            steps {
                sh 'python3 Hello.py'
            }
        }
    }
}
