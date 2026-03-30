pipeline {
    agent any

    stages {
        stage('Source Stage') {
            steps {
                echo 'Pulling the latest code from GitHub...'
                // This tells Jenkins to grab the code from your Git repository
                checkout scm
            }
        }

        stage('Build Stage') {
            steps {
                echo 'Building the Docker Image...'
                // Jenkins runs the Docker build command
                bat 'docker build -t student-feedback-app .'
            }
        }

        stage('Deploy Stage') {
            steps {
                echo 'Deploying directly via Docker...'
                // Stop the old container if it exists
                bat 'docker stop student-feedback-container || exit 0'
                // Remove the old container if it exists
                bat 'docker rm student-feedback-container || exit 0'
                // Run the new container
                bat 'docker run -d --name student-feedback-container -p 5000:5000 student-feedback-app'
            }
        }
    }
}