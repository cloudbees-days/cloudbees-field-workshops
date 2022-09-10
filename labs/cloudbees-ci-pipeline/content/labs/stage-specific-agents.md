---
title: "Stage Specific Agents"
chapter: false
weight: 2
--- 

In this lab we will get an introduction to the [Jenkins Kubernetes plugin](https://github.com/jenkinsci/kubernetes-plugin/blob/master/README.md) that enables the use of dynamic and ephemeral agents with CloudBees CI on a Kubernetes cluster - allowing you to leverage the scaling capabilities of [Kubernetes to schedule build agents](https://kurtmadel.com/posts/cicd-with-kubernetes/autoscaling-jenkins-agents-with-kubernetes/).

CloudBees CI has out-of-the-box support for Kubernetes build agents, with the capability to create and manage Kubernetes agent templates - called Pod Templates - at both the [the Cloud Operations Center level](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/agents#_globally_editing_pod_templates_in_operations_center) to be shared by multiple controllers and at the [the Managed Controller level](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/agents#_editing_pod_templates_per_team_using_masters) for more granular agent configuration. The Kubernetes based agent is contained in a [Kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/), where a pod is a group of one or more containers (e.g. Docker container) sharing a common storage system and network. A pod is the smallest deployable unit of computing that Kubernetes can create and manage (you can read more about pods in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod/)).

{{% notice note %}}
One of the **containers** in a **Pod Template** must host the actual Jenkins build agent that communicates with the Jenkins controller (the `agent.jar` file that is used for communication between the CloudBees Managed Controller and the agent). By convention, this container always exists (and is automatically added to any Pod Templates that do not define a **Container Template** with the name ***jnlp*** ). Again, this special container has the ***Name*** `jnlp` and default execution of the Pipeline always happens in this `jnlp` container (as it did when we used `agent any` in our initial Declarative Pipeline) - unless you declare otherwise with a special Pipeline step provided by the Kubernetes plugin - [the container step](https://github.com/jenkinsci/kubernetes-plugin#pipeline-support). If needed, this automatically provided `jnlp` container may be overridden by specifying a **Container Template** with the ***Name*** `jnlp` - but that **Container Template** must be able to connect to the Managed Controller via a JNLP or websocket connection with a version of the Jenkins `agent.jar` that works with the the Managed Controller Jenkins version or the Pod based agent will fail to connect to the Managed Controller. You can learn more about the `jnlp` container and additional functionality in the [Jenkins Kubernetes Plugin documentation on GitHub](https://github.com/jenkinsci/kubernetes-plugin#pipeline-support).
{{% /notice %}}

We will use the Kubernetes plugin [Pipeline container block](https://jenkins.io/doc/pipeline/steps/kubernetes/#container-run-build-steps-in-a-container) to run Pipeline `steps` inside a specific container configured as part of a Jenkins Kubernetes Agent Pod template. In our initial Pipeline, we used `agent any` which required at least one Jenkins agent configured to *Use this node as much as possible* - resulting in the use of a Pod Template that only had a `jnlp` container. But now we want to use Node.js in our Pipeline. [Jenkins CasC](https://github.com/jenkinsci/configuration-as-code-plugin) was used to pre-configure the [CloudBees Kube Agent Management plugin](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/agents#_editing_pod_templates_per_team_using_masters) to include a [Kubernetes Pod Template at the Managed Controller level](https://github.com/cloudbees-days/cloudbees-ci-config-bundle/blob/pipeline-workshop/jenkins.yaml#L33) to provide a Node.js container. 

1. In the **pipelines** folder on your controller, click on the **simple-pipeline-job** link and then click on the **Pod Templates** link. ![Controller Pod Templates](controller-pod-templates.png?width=50pc) 
2. The **Available pod templates** screen will show you what pod templates are available to use on your controller and includes the ***Label*** to use for the agent and lists the ***Containers*** configured for the template. Note the label, container name and image for the **nodejs-app** template.  ![Available Pod Templates](available-pod-templates.png?width=50pc) 
3. Navigate to and click on the `Jenkinsfile` file in the **development** branch of your **insurance-frontend** repository and click on the **Edit this file** button (pencil) and replace the global `agent` section with the following:
```
  agent none
```

4. Next, in the **Say Hello** `stage` add the following `agent` section right above the `steps` section so that we will get the Kubernetes Pod Template configured for your Managed Controller with the **Container Template** that includes the `us-east1-docker.pkg.dev/core-workshop/workshop-registry/node:14-alpine` Docker(container) image above: 
```
    agent { label 'nodejs-app' }
```
{{%expand "expand for complete Jenkinsfile" %}}
```
pipeline {
  agent none
  stages {
    stage('Say Hello') {
      agent { label 'nodejs-app' }
      steps {
        echo 'Hello World!'   
        sh 'java -version'
      }
    }
  }
}
```
{{% /expand%}}

5. Commit that change to the `development` branch and navigate to your **insurance-frontend** job on your Managed Controller. The build logs should be almost the same as before because we are still using the default `jnlp` container. ![Build with Agent Template](build-agent-template.png?width=50pc) 
6. Let's change that by replacing the **Say Hello** `stage` with the following **Test** `stage` so the steps run in the **nodejs** `container`. Edit the `Jenkinsfile` file in the **development** branch of your forked **insurance-frontend** repository so the entire pipeline looks like the following:

```
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

  All of the Pipeline steps within the `container` block will run in the container specified by the **Name** of the **Container Template** - and in this case that **Container Template** is using the `us-east1-docker.pkg.dev/core-workshop/workshop-registry/node:14-alpine` container image as we saw above. Commit the changes and the **insurance-frontend** job will run - it will result in an error because the `nodejs` container does not have Java installed (and why should it). Hover over the failed stage in the **Stage View** of your development branch job and click on the **Logs** button.   ![Open Logs](stage-view-logs-button.png?width=50pc) Next, expand the last step - `sh 'java -version'` - to see the error. ![Java Error](agent-java-error.png?width=50pc) 
7. We will fix the error in the **Test** `stage` we added above by replacing the `sh 'java -version'` step with the `sh 'node --version'` step and moving the `sh 'java -version` step above the `container` block in the `Jenkinsfile` file in the **development** branch of your forked **insurance-frontend** repository so the entire pipeline looks like the following:
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
8. Commit the changes and the **insurance-frontend** job will run and it will complete successfully with the following output: ![Agent Success](agent-java-success.png?width=50pc) 

{{% notice note %}}
The sh 'java -version' step before the `container('nodejs')` completed successfully this time because it used the default `jnlp` container to execute any steps not in the `container` block. You could also explicitly run pipeline steps within the `jnlp` container by wrapping them with `container('jnlp')`.
{{% /notice %}}

### Finished Jenkinsfile for *Stage Specific Agents* Lab
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
