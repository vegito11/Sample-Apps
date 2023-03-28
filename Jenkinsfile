 env.REPO_NAME = "Sample-Apps"
 env.BRANCH_NAME = "node-app"
 env.IMAGE_NAME = "nodeapp"
 env.HOST_PORT = "30080"
 env.APP_PORT = "8080"

 node("ci"){
     
     cleanWs()

     println("Started the Node-App Build Pipeline from Github 🦤🦉 .... ")

     stage("Checkout Git Repo"){
         sshagent(credentials: ['github_ssh_key']) {
         sh """
             ssh-keyscan -t rsa,dsa github.com >> ~/.ssh/known_hosts
             git clone -b ${BRANCH_NAME} --single-branch git@github.com:vegito11/${REPO_NAME}.git
         """
         }
     }

     stage('Commit Info') {
         // Get the commit information
         dir(REPO_NAME){
             env.commitHash = sh(returnStdout: true, script: 'git rev-parse HEAD').trim().substring(0,8)
             commitMessage = sh(returnStdout: true, script: 'git log --format=%B -n 1').trim()
             commitAuthor = sh(returnStdout: true, script: 'git log --format=%an -n 1').trim()
         }
     
         println("Commit Hash: ${commitHash}")
         println("Commit Message: ${commitMessage}")
         println("Commit Author: ${commitAuthor}")
     }

     stage("Build Images"){
         
         sh """
             cd $REPO_NAME;
             docker build -t vegito/${IMAGE_NAME}:${commitHash} .
         """
     }

     stage("Push Docker Image"){
         withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
             sh """
                 docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}
                 docker push vegito/${IMAGE_NAME}:${commitHash}
             """

         }
     }

     stage("Deploy App"){
         
         sh """
             docker stop ${IMAGE_NAME} || true
             docker rm -f ${IMAGE_NAME} || true
             docker run -d -p ${HOST_PORT}:${APP_PORT} --name ${IMAGE_NAME} vegito/${IMAGE_NAME}:${commitHash}
         """        
     }
 }