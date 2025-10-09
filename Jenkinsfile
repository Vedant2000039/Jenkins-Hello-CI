pipeline {
    agent any
    
    triggers {
        // Run every day at 9:00 AM
        cron('0 9 * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }

        stage('Run Tests'){
            steps{
                sh 'python3 -m unittest discover -s tests'
            }
        }
        stage('Run Script') {
            steps {
                sh 'python3 Hello.py'
            }
        }
    }

    post{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
