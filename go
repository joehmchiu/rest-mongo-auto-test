pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Starting to build the App.'
      }
    }
    stage('Deploy') {
      steps {
        echo "installing..."
      }
    }
    stage('Test') {
      steps {
        echo "testing..."
      }
    }
    stage('Done') {
      steps {
        echo "Done!"
      }
    }
  }
}
