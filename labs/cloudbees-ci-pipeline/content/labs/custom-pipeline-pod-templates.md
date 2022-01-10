---
title: "Custom Pipeline Pod Templates"
chapter: false
weight: 3
--- 

## Kubernetes Pod Templates Defined in Pipeline Script

In this lab we will create a custom Kubernetes Pod Template containing a NodeJS **container** and an additional Docker **container** for executing tests. We also want to use a different version of the **node** container than the one provided by the **nodejs-app** Kubernetes *Pod Template* [defined for us on our Managed Controller](https://go.cloudbees.com/docs/cloudbees-core/cloud-admin-guide/agents/#_editing_pod_templates_per_team_using_masters). In order to be able to control what `containers` and what container `image` version we use in our Pipeline, we will update the **Jenkinsfile** Pipeline script with an inline [Kubernetes Pod Template definition](https://github.com/jenkinsci/kubernetes-plugin#declarative-pipeline).

1. The [Jenkins Kubernetes plugin](https://github.com/jenkinsci/kubernetes-plugin#using-yaml-to-define-pod-templates) allows you to use standard Kubernetes Pod yaml configuration to define Pod Templates directly in your Pipeline script, either as a string or a file. We will do just that by creating a new `nodejs-pod.yaml` file and then adding a `yamlFile` parameter to the `agent` declaration with a value of the the repository relative path to that yaml file. The file provides the [Pod spec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#pod-v1-core) to be used for the Pod Template based agent. Navigate to your workshop **helloworld-nodejs** repository in your workshop GitHub Organization, make sure you are on the `development` branch, then click the **Add file** button towards the top right of the screen and then select **Create new file**. **IMPORTANT:** Make sure you are on the `development` branch (the ***Test*** stage will not execute for the `main` branch). ![Create Pod Template File](create-pod-template-file.png?width=50pc)
2. Name the file `nodejs-pod.yaml` and add the following content:
```
kind: Pod
metadata:
  name: nodejs-app
spec:
  containers:
  - name: nodejs
    image: node:17-alpine
    command:
    - sleep
    args:
    - 99d
  - name: testcafe
    image: testcafe/testcafe:1.18.0
    command:
    - sleep
    args:
    - 99d
  securityContext:
    runAsUser: 1000
```
*This is a standard Kubernetes Pod Specification.*

3. At the bottom of the screen enter a commit message, leave **Commit directly to the `development` branch** selected and click the **Commit new file** button.
4. Now we need to update our Pipeline to use that file. Open the GitHub editor for the **Jenkinsfile** Pipeline script in the **development** branch of your workshop **helloworld-nodejs** repository. ![Update Jenkinsfile](update-jenkinsfile.png?width=50pc)
5. Replace the `agent` section of the **Test** `stage` with the following - note that the value of the `yamlFile` parameter is the name of the pod template file we created:
```
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
```
Your complete `development` branch Jenkinsfile should match the following:
```
pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        container('nodejs') {
          echo 'Hello World!'   
          sh 'node --version'
        }
      }
    }
  }
}
```

6. Commit the changes and then navigate to the **development** branch of your **helloworld-nodejs** job on your CloudBees CI Managed Controller. The job will run successfully. Also, note the output of the `sh 'node --version'` step - it is `v17.x.x` instead of `v14.x.x`: ![Update Node Container Tag](pod-template-update-image-tag.png?width=50pc) Also notice that the final Kubernetes pod spec for the agent is printed out in the logs and is merge of a default template (with the **jnlp** container) and the pod spec from your **helloworld-nodejs** repository:

```yaml
---
apiVersion: "v1"
kind: "Pod"
metadata:
  annotations:
    buildUrl: "http://cbci-pipeline-controller.controllers.svc.cluster.local/cbci-pipeline-controller/job/pipelines/job/helloworld-nodejs/job/development/11/"
    runUrl: "job/pipelines/job/helloworld-nodejs/job/development/11/"
  labels:
    jenkins: "agent"
    jenkins/label-digest: "61f0f4a8bcfe17103cfdfc7664930d6f52ba5c90"
    jenkins/label: "pipelines_helloworld-nodejs_development_11-mv2mw"
    cloudbees.com/master: "cbci-pipeline-controller"
  name: "pipelines-helloworld-nodejs-development-11-mv2mw-c9lrm-0vccf"
spec:
  affinity:
    podAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: "com.cloudbees.cje.type"
              operator: "In"
              values:
              - "master"
              - "cjoc"
          topologyKey: "kubernetes.io/hostname"
        weight: 1
  containers:
  - args:
    - "99d"
    command:
    - "sleep"
    image: "node:17-alpine"
    name: "nodejs"
    volumeMounts:
    - mountPath: "/home/jenkins/agent"
      name: "workspace-volume"
      readOnly: false
  - args:
    - "99d"
    command:
    - "sleep"
    image: "testcafe/testcafe:1.18.0"
    name: "testcafe"
    volumeMounts:
    - mountPath: "/home/jenkins/agent"
      name: "workspace-volume"
      readOnly: false
  - env:
    - name: "JENKINS_SECRET"
      value: "********"
    - name: "JENKINS_AGENT_NAME"
      value: "pipelines-helloworld-nodejs-development-11-mv2mw-c9lrm-0vccf"
    - name: "JENKINS_WEB_SOCKET"
      value: "true"
    - name: "JENKINS_NAME"
      value: "pipelines-helloworld-nodejs-development-11-mv2mw-c9lrm-0vccf"
    - name: "JENKINS_AGENT_WORKDIR"
      value: "/home/jenkins/agent"
    - name: "JENKINS_URL"
      value: "http://cbci-pipeline-controller.controllers.svc.cluster.local/cbci-pipeline-controller/"
    image: "gcr.io/cloudbees-ops-gcr/ubi/unified-distribution/agent:2.319.2.4"
    name: "jnlp"
    resources:
      limits: {}
      requests:
        memory: "256Mi"
        cpu: "100m"
    volumeMounts:
    - mountPath: "/home/jenkins/agent"
      name: "workspace-volume"
      readOnly: false
  hostNetwork: false
  nodeSelector:
    kubernetes.io/os: "linux"
  restartPolicy: "Never"
  securityContext:
    runAsGroup: 1000
    runAsUser: 1000
  serviceAccountName: "jenkins"
  volumes:
  - emptyDir:
      medium: ""
    name: "workspace-volume"
```

### Finished Jenkinsfile for *Custom Pipeline Pod Templates* Lab
```
pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        container('nodejs') {
          echo 'Hello World!'   
          sh 'node --version'
        }
      }
    }
  }
}
```
