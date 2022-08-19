pipeline {
    agent { docker { image 'public.ecr.aws/sam/build-python3.9' } }
    stages {
        stage('build') {
            steps {
                sh 'sam build'
                sh 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}