pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/ThanujaSanjuka/FastAPI_Student_web.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-student .'
            }
        }
        stage('Deploy App') {
            steps {
                // පරණ කන්ටේනර් එකක් රන් වෙනවා නම් ඒක අයින් කරන්න
                sh 'docker rm -f fastapi-container || true'
                // අලුත් කන්ටේනර් එක background එකේ (-d) රන් කරන්න
                sh 'docker run -d --name fastapi-container -p 8000:8000 fastapi-student'
            }
        }
    }
}
