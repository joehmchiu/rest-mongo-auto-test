pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Starting to build the App.'
        sh "ls -ltrhR"
      }
    }
    stage('Deploy') {
      steps {
        echo "installing..."
        sh "cd bin"
        sh "ansible-playbook -i hosts auto-rest.yml -vvv"
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
