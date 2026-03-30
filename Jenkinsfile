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
                echo 'Triggering Ansible Deployment...'
                // Using the absolute path to force Jenkins to find WSL
                bat 'C:\\Windows\\System32\\wsl.exe ansible-playbook -i ansible/inventory ansible/deploy.yml'
            }
        }
    }
}