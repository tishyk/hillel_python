node {
    def myGradleContainer = docker.image('gradle:python:3.7-buster')
    myGradleContainer.pull()

    stage('prep') {
        git url: 'https://github.com/tishyk/hillel_python.git'
    }

    stage('build') {
      myGradleContainer.inside("-v ${env.HOME}/.gradle:/home/gradle/.gradle") {
        sh 'cd complete && /opt/gradle/bin/gradle build'
      }
    }

    stage('sonar-scanner') {
      def sonarqubeScannerHome = tool name: 'sonar', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
      withCredentials([string(credentialsId: 'sonar', variable: 'sonarLogin')]) {
        sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://sonarqube:9000 -Dsonar.login=${sonarLogin} -Dsonar.projectName=gs-gradle -Dsonar.projectVersion=${env.BUILD_NUMBER} -Dsonar.projectKey=GS -Dsonar.sources=complete/src/main/ -Dsonar.tests=complete/src/test/ -Dsonar.language=python -Dsonar.python.binaries=."
      }
    }
}
