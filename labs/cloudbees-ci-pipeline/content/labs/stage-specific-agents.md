---
title: "Stage Specific Agents"
chapter: false
weight: 2
--- 

In this lab we will get an introduction to the [Jenkins Kubernetes plugin](https://github.com/jenkinsci/kubernetes-plugin/blob/master/README.md) that enables the use of dynamic and ephemeral agents with CloudBees CI on a Kubernetes cluster - allowing you to [leverage the scaling capabilities of Kubernetes to schedule build agents](https://kurtmadel.com/posts/cicd-with-kubernetes/autoscaling-jenkins-agents-with-kubernetes/).

CloudBees Core has out-of-the-box support for Kubernetes build agents and allow Kubernetes agent templates - called Pod Templates - to be defined at either [the Operations Center level](https://go.cloudbees.com/docs/cloudbees-core/cloud-admin-guide/agents/#_globally_editing_pod_templates_in_operations_center) to be shared by multipe controllers or at [the Managed Controller level](https://go.cloudbees.com/docs/cloudbees-core/cloud-admin-guide/agents/#_editing_pod_templates_per_team_using_masters). The Kubernetes based agent is contained in a [Kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/), where a pod is a group of one or more containers sharing a common storage system and network. A pod is the smallest deployable unit of computing that Kubernetes can create and manage (you can read more about pods in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod/)).

>NOTE: One of the **containers** in a **Pod Template** must host the actual Jenkins build agent that communicates with the Jenkins controller (the `agent.jar` file that is used for communication between the CloudBees Managed Controller and the agent). By convention, this container always exists (and is automatically added to any Pod Templates that do not define a **Container Template** with the name ***jnlp*** ). Again, this special container has the ***Name*** `jnlp` and default execution of the Pipeline always happens in this `jnlp` container (as it did when we used `agent any` in our initial Declarative Pipeline) - unless you declare otherwise with a special Pipeline step provided by the Kuberentes plugin - [the container step](https://github.com/jenkinsci/kubernetes-plugin#pipeline-support). If needed, this automatically provided `jnlp` container may be overridden by specifying a **Container Template** with the ***Name*** `jnlp` - but that **Container Template** must be able to connect to the Managed Controller via a JNLP or websocket connection with a version of the Jenkins `agent.jar` that works with the the Managed Controller Jenkins version or the Pod based agent will fail to connect to the Managed Controller. You can learn more about the `jnlp` container and additional functionality in the [Jenkins Kubernetes Plugin documentation on GitHub](https://github.com/jenkinsci/kubernetes-plugin#pipeline-support).

We will use the Kubernetes plugin [Pipeline container block](https://jenkins.io/doc/pipeline/steps/kubernetes/#container-run-build-steps-in-a-container) to run Pipeline `steps` inside a specific container configured as part of a Jenkins Kubernetes Agent Pod template. In our initial Pipeline, we used `agent any` which required at least one Jenkins agent configured to *Use this node as much as possible* - resulting in the use of a Pod Template that only had a `jnlp` container. But now we want to use Node.js in our Pipeline. [Jenkins CasC](https://github.com/jenkinsci/configuration-as-code-plugin) was used to pre-configure the [CloudBees Kube Agent Management plugin](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/agents#_editing_pod_templates_per_team_using_masters) to include a [Kubernetes Pod Template at the Managed Controller level](https://github.com/cloudbees-days/cloudbees-ci-config-bundle/blob/pipeline-workshop/jenkins.yaml#L33) to provide a Node.js container. 

1. Go to the top-level of your Managed Controller, click on the **Manage Jenkins** link and then scroll down and click on the **Kubernetes Pod Templates** item. ![Controller Pod Templates](controller-pod-templates.png?width=50pc) 
2. On the next screen, click on the **Pod Template details...** button for the ***Kubernetes Pod Template*** with the **Name** **'nodejs-app'**.  ![Kubernetes Node.js Agent Template](k8s-nodejs-agent-template.png?width=50pc) 
Take note of the ***Labels*** field with a value of ***nodejs-app*** and the **Container Template** ***Name*** field with a value of ***nodejs*** - both of these are important and we will need those values to configure our Pipeline to use this **Pod Template** and **Container Template** in your `Jenkinsfile`. Also note the **Docker image** being specified: `node:8.12.0-alpine`.
3. Navigate to and click on the `Jenkinsfile` file in the **development** branch of your **helloworld-nodejs** repository.
4. Click on the **Edit this file** button (pencil) and replace the global `agent` section with the following:
```
  agent none
```

5. Next, in the **Say Hello** `stage` add the following `agent` section right above the `steps` section so that we will get the Kubernetes Pod Template configured for your Managed Controller with the **Container Template** that includes the `node:8.12.0-alpine` Docker(container) image above: 
```
    agent { label 'nodejs-app' }
```
6. Commit that change to the `development` branch and navigate to your **helloworld-nodejs** job on your Managed Controller. The build logs should be almost the same as before because we are still using the default `jnlp` container. ![Build with Agent Template](build-agent-template.png?width=50pc) 
7. Let's change that by replacing the **Say Hello** `stage` with the following **Test** `stage` so the steps run in the **nodejs** `container`. Edit the `Jenkinsfile` file in the **development** branch of your forked **helloworld-nodejs** repository so the entire pipeline looks like the following:

```groovy
pipeline {
  agent none
  stages {
    stage('Test') {
      agent { label 'nodejs-app' }
      steps {
        container('nodejs') {
          echo 'Hello World!'   
          sh 'java -version'
        }
      }
    }
  }
}
```

  All of the Pipeline steps within the `container` block will run in the container specified by the **Name** of the **Container Template** - and in this case that **Container Template** is using the `node:8.12.0-alpine` container image as we saw above. Commit the changes and the **helloworld-nodejs** job will run - it will result in an error because the `nodejs` container does not have Java installed (and why should it). Hover over the failed stage in the **Stage View** of your development branch job and click on the **Logs** button.   ![Open Logs](stage-view-logs-button.png?width=50pc) Next, expand the last step - `sh 'java -version'` - to see the error. ![Java Error](agent-java-error.png?width=50pc) 
8. We will fix the error in the **Test** `stage` we added above by replacing the `sh 'java -version'` step with the `sh 'node --version'` step and moving the `sh 'java -version` step above the `container` block in the `Jenkinsfile` file in the **development** branch of your forked **helloworld-nodejs** repository so the entire pipeline looks like the following:
```
pipeline {
  agent none
  stages {
    stage('Test') {
      agent { label 'nodejs-app' }
      steps {
        sh 'java -version'
        container('nodejs') {
          echo 'Hello World!'   
          sh 'node --version'
        }
      }
    }
  }
}
```
9. Commit the changes and the **helloworld-nodejs** job will run and it will complete successfully with the following output: ![Agent Success](agent-java-success.png?width=50pc) 

>**NOTE:** The sh 'java -version' step before the `container('nodejs')` completed successfully this time because it used the default `jnlp` container to execute any steps not in the `container` block.

### Finished Jenkinsfile for *Stage Specific Agents*
**Important**: For the finished Jenkinsfile for this stage, remove the `sh 'java -version'` step and make sure you copy the Pipeline as below and replace yours. 

```
pipeline {
  agent none
  stages {
    stage('Test') {
      agent { label 'nodejs-app' }
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
