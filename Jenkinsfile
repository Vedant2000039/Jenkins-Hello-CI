pipeline {
    agent {
        docker { 
            image 'python:3.12'
            args '-u root:root'
        }
    }
    
    options {
        skipDefaultCheckout() // disables automatic checkout
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout 'main' branch from GitHub
                git branch: 'main', url: 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Hello-CI project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running hello.py...'
                sh 'python hello.py' // make sure file name matches
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment simulated - Hello CI project complete!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully! 🎉'
        }
        failure {
            echo 'Pipeline failed! ❌ Check logs for errors.'
        }
    }
}
