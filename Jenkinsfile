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

        stage('error') {
          steps {
            echo 'Step in Buzz Buzz stage'
          }
        }

      }
    }

    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Building in region $Region ..'
          }
        }

        stage('error') {
          steps {
            sleep 100
          }
        }

      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'Testing..'
          }
        }

        stage('Test_message') {
          steps {
            echo 'Testing steps 1'
          }
        }

      }
    }

    stage('Deploy') {
      parallel {
        stage('Deploy') {
          steps {
            echo 'Deploying....'
          }
        }

        stage('error') {
          steps {
            timestamps()
          }
        }

      }
    }

  }
  environment {
    name = 'Ganesh'
  }
}