pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/keidar/Project2.git'
            }
        }
        stage('run rest app server ') {
            steps {
                script {
                    sh 'nohup python rest_app.py &'

                }
            }
        }
 
        stage('run backend testing') {
            steps {
                script {
                    sh 'python backend_testing.py'

                }
            }
        }
        stage('run clean environmant ') {
            steps {
                script {
                    sh ' python clean_environment.py'

                }
            }
        }
    }
}
