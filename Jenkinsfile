pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
        sh 'pip install paho-mqtt'
      }
    }
    stage('hello') {
      steps {
        sh 'python subscribe.py'
      }
    }
  }
}
