pipeline {
    agent {
        docker {
            image 'python:3.12' 
            args '-u root:root'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/Hello-CI.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python Hello.py'
            }
        }

        stage('Archive Output') {
            steps {
                sh 'echo "Build finished at $(date)" > build_log.txt'
                archiveArtifacts artifacts: 'build_log.txt', followSymlinks: false
            }
        }
    }
}
