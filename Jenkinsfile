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
        stage('run backend server ') {
            steps {
                script {
                    sh 'pip install selenium'
                    sh 'pip install pymysql'
                    sh 'nohup python rest_app.py &'

                }
            }
        }
        stage('run backend server') {
            steps {
                script {
                    sh 'nohup python web_app.py &'

                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    sh 'nohup python backend_testing.py &'

                }
            }
        }
        stage('run frontend testing') {
            steps {
                script {
                    sh 'nohup python frontend_testing.py &'

                }
            }
        }
        stage('run combined testing') {
            steps {
                script {
                    sh 'nohup python combined_testing.py &'

                }
            }
        }
        stage('run clean environmant ') {
            steps {
                script {
                    sh 'nohup python clean_environment.py &'

                }
            }
        }
    }
}
