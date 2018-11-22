pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
python3 manage.py migrate'''
      }
    }
    stage('Testing') {
      steps {
        sh '''#!/bin/bash
python3 manage.py test
'''
      }
    }
    stage('Deploy') {
      steps {
        sh 'BUILD_ID=dontKillMe nohup python3 manage.py runserver & '
      }
    }
  }
}