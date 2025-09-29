pipeline {
    agent any

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
