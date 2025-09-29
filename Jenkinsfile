pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Explicitly clone your GitHub repo
                git branch: 'main', url: 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }
        stage('Run Script') {
            steps {
                // Run your Python script
                sh 'python3 Hello.py'
            }
        }
    }
}
