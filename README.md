# Jenkins deploy the App on Kubernetes

## Agenda of Project
Create a job chain by using build pipeline plugin in jenkins that deploy the app on the kubernetes where we use Kubernetes resources like Pods, ReplicaSet, Deployment, PVC and Service.

## Tools knowledge Required
- GitHub Account
- Kubernetes setup on Redhat8
- Jenkins image that is launched by docker

## Implementation
- Create container image that’s has Jenkins installed using Dockerfile
- When we launch this image, it should automatically starts Jenkins service in the container.
- Create a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins 

### Job1 : Kubectl web deploy (GitHub)
Pull the Github repo automatically when some developers push repo to Github.

### Job2 : Automatically launch deployment according to code
- By looking at the code or program file, Jenkins should automatically start the respective language interpreter installed image container to deploy code on top of Kubernetes ( eg. If code is of PHP, then Jenkins should start the container that has PHP already installed )
- Expose your pod so that testing team could perform the testing on the pod
- Make the data to remain persistent ( If server collects some data like logs, other user information )

### Job3: Testing and sending mail of success
- Test your app if it is working or not. Send the mail of success if it is working

### Job4 : Monitoring jenkins
- If it is fail then automaticaly launch the jenkins server
