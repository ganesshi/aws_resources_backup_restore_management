pipeline {
  agent any
  stages {
    stage('Buzz Buzz') {
      parallel {
        stage('Buzz Buzz') {
          steps {
            echo 'Buzz buzz stage...'
          }
        }

        stage('') {
          steps {
            echo 'Step in Buzz Buzz stage'
          }
        }

      }
    }

    stage('Build') {
      steps {
        echo 'Building in region $Region ..'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }

  }
}