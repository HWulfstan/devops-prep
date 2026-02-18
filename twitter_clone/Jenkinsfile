pipeline {
    agent { label 'docker-agent' }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t twitter_clone .'
            }
        }
    }
}
