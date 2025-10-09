pipeline {
    agent any

    // 1️⃣ Parameters to pass to Python script
    parameters {
        string(name: 'X_VALUE', defaultValue: '10', description: 'First number for sum_numbers()')
        string(name: 'Y_VALUE', defaultValue: '20', description: 'Second number for sum_numbers()')
    }

    // 2️⃣ Scheduled trigger (optional, runs daily at 9 AM)
    triggers {
        cron('0 9 * * *')
    }

    stages {
        // 3️⃣ Checkout code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vedant2000039/Jenkins-Hello-CI.git'
            }
        }

        // 4️⃣ Run Python unit tests
        stage('Run Tests') {
    steps {
        sh 'python3 -m unittest discover -s tests -p "*.py"'
    }
}


        // 5️⃣ Run Python script with parameters from Jenkins
        stage('Run Script with Parameters') {
            steps {
                sh """
                    export X_VALUE=${X_VALUE}
                    export Y_VALUE=${Y_VALUE}
                    python3 Hello.py
                """
            }
        }
    }

    // 6️⃣ Post-build actions (email notifications)
    post {
        success {
            echo "✅ Pipeline completed successfully!"

            emailext (
                subject: "✅ Jenkins Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <p>Hi Vedant,</p>
                    <p>The Jenkins build for <b>${env.JOB_NAME}</b> completed successfully.</p>
                    <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <br>
                    <p>Regards,<br>Jenkins CI Server</p>
                """,
                to: "vedant.yourmail@example.com"
            )
        }

        failure {
            echo "❌ Pipeline failed! Please check logs."

            emailext (
                subject: "❌ Jenkins Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <p>Hi Vedant,</p>
                    <p>The Jenkins build for <b>${env.JOB_NAME}</b> has <b>FAILED</b>.</p>
                    <p>Please check the logs at: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <br>
                    <p>Regards,<br>Jenkins CI Server</p>
                """,
                to: "vmulherkar@xtsworld.in"
            )
        }
    }
}
