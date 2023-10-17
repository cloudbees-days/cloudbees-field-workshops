---
title: "Microservice Deployment"
chapter: false
weight: 4
--- 

Deploying an application is a standard part of most release pipelines. One of the challenges you want to avoid is duplicating effort by redefining the process of deploying your application over and over.

CloudBees CD/RO has application and environment modeling capabilities which avoid this problem. It allows you to define the process once and use it over and over.

An application model allows you to define all of the processes you may run in relation to a given application. This can include processes such as deploying, removing, upgrading, etc.

Similar to object-oriented programming, this approach gives you the full context of what actions are available to you against a given application.


## Reviewing the application

In this lab, you'll be going through the process of creating and running an application deployment model for the following application.

![Demo application](demo-app.png)

This application is a simple webpage, but it will take in a couple of environment variables, specifically `$NAME` and `$ENVIRONMENT`. This will illustrate which environment it was deployed to and by whom.

There are many ways to deploy an application, especially one as simple as this. For this exercise we'll be employing [Helm](https://helm.sh), a Kubernetes package manager, to perform the deployment.

### 30-second Helm primer

CloudBees CD/RO will abstract away the need to run individual Helm commands, but it is helpful to know what Helm is doing behind the scenes.

[Helm](https://helm.sh) is effectively a template engine and state manager for Kubernetes resources.

It takes something that looks like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    application: my-app
spec:
  replicas: 1
```

And turns it into:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "chart.fullname" . }}
  labels:
    {{- include "chart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
```

It takes this template and runs it against a `values.yaml` file which includes the values to inject as well as values passed in via the command line.

It then applies these generated resources into the cluster in what it calls a **release**. 

It keeps track of the configuration state from each of the releases so you can perform upgrades or rollback without issue.

## Creating the application model

First you'll need to navigate to the **Applications** page. 

![Applications page nav](applications-page-nav.png)

Then you'll click on the New button in the top right.

![New application button](new-application-button.png)

Then **Create New**

![Create new application](create-new-app.png)

Then proceed to fill out the form. You can call the application `Workshop App` and target the project you created in the pre-reqs. Then select **Microservice** for the application type.

![New application form](new-application-form.png)

Now you have a blank microservice application model.

![Blank application model](fresh-app-model.png)

As you can see, there are two big components standing out here. There is the microservice model block on the left (in pink). There is the environment model on the right (in purple).

### Defining the microservice component

First we'll start with the microservice definition on the left. This is where you'll specify the Helm chart you want to deploy as well as any values you need to pass in.

To begin, click on the blue "Add microservice" button which will bring up the necessary form.
![New microservice button](new-microservice-button.png)


We'll create a new microservice from scratch. You can just click next and leave the default option selected.
![New microservice form](new-microservice-form-1.png)

Next you need to fill out the definition form.

| Field | Value | Description | 
| --- | --- | --- |
| Name | `hello-app` | The name to identify your application |
| Description | *optional* | A field to help understand the context of this application |
| Definition type | `Helm` | The type of microservice deployment you want to run |
| Definition source | `Git repository` | The source for where to look for the target Helm chart. It could be a Helm registry, but for this workshop we're using a Git repo. |
| Configuration Name | `cb-bot-Workshop` | The credentials to use for the Git connection when pulling the repository. In this case, we'll be using a shared GitHub service account since the repository is public. |
| Git repository | https://github.com/cloudbees-days/cdro-workshop-demo-app | The target repository where it will look for the Helm chart |
| Remote branch | `main` | The branch in GitHub it will checkout |
| Release name | `hello-app` | The name Helm will use to track your app release |
| Chart | `./chart` | The name or path to the chart we'll be using. In this case, since we're using a Git repo, we are passing in the path. |
| Chart Version |  | If you wanted to specify a particular version of a Helm chart you can do so. In our case, we'll be leaving it blank to use the latest. |
| Additional options | `--create-namespace` | If you want to pass in arguments like you do using the Helm cli, you can pass them in here  |
| Values | *Below* | You can also pass in values in YAML form. This is what we'll be doing for the workshop. |

**Values** - You'll want to make sure the subdomain is targeting your username.
```yaml
ingress:
  hosts:
    - host: my-username.cdro-workshop.cb-demos.io
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls:
    - secretName: insurance-frontend-tls
      hosts:
        - my-username.cdro-workshop.cb-demos.io

name: "my-username"
environment: "QA"
```

![New microservice form - part 2](new-microservice-form-2.png)

Now hit "OK" and the microservice component will be created.
![Created microservice](new-microservice-done.png)


### Defining the environment

Now, before we're able to deploy our newly-defined application, we need to define an environment to deploy it into.

Get started by clicking the blue "+" button on the right side.
![New cluster](new-environment-1.png)

*It should be noted that we aren't creating a new Kubernetes cluster, but rather a new environment definition based on a cluster.*

Similar to the application definition, you can just click "Next" and leave the default option of "New environment" on this page.
![New cluster - part 2](new-environment-2.png)

Now you'll define the cluster environment.

| Field | Value | Description | 
| --- | --- | --- |
| Environment name | `QA` | The name to identify your environment |
| Project | Select your project | The project inside which this environment will be stored |
| Environment description | *Optional* | A field to give textual details about this environment |
| Utility resource name | k8s-agent |

![New cluster - part 3](new-environment-3.png)

Next you'll define the cluster reference.

| Field | Value | Description | 
| --- | --- | --- |
| Cluster name | `default` | A name to identify this cluster |
| Cluster description | *Optional* | A field to give textual details about this cluster |
| Configuration provider | `Kubernetes (via Helm)` | The type of environment you're defining |
| Configuration name | `k8s-Workshop` | A reference to a configuration that lets CD/RO know where to use Helm |
| Namespace | `my-username-qa` | The Kubernetes namespace where your application will be deployed. You should update this to be YOUR_USERNAME-qa. |
| Kubeconfig context |  | This allows you to target a specific cluster if your configuration is pointed at multiple. For this workshop you can leave this blank. |
| Utility resource name | `k8s-agent` | This is the name to identify the utility resource |
| Resource | `k8s-agent-0` | This is the agent which will communicate with the Kubernetes cluster  |

![New cluster - part 3](new-environment-4.png)

The last step in configuring our microservice application is to map the microservice (hello-app) to your environment (QA).  To do that click on the ![Add mapping](AddMapping.png) button and map your application

| Mapping Tile | Mapped Application |
|--------|--------|
| ![mapping](mappingTile.png) | ![mapped](mappedApplication.png) |


## Running the deployment

![Environment created](environment-created.png)

Now you're ready to deploy the application.

Go ahead and click the "Deploy" button in the bottom right. This will launch a modal where you can specify which application process to run and which environment to target.

In this case, you'll select `Deploy Application` as the process and `QA` as the environment (*these should be the only options presented*). When you're ready, hit "OK".

![Deployment - part 1](deploy-1.png)

It will bring you to the application run page where you can see the steps updating live as they are happening.

![Deployment - part 2](deploy-2.png)

After a short time, you should see a view like this where all of the stages are complete.

![Deployment - part 3](deploy-3.png)

You can click the top list item to see more detail on the overall run and you can also click the individual steps to see specific details from just that step.

### Visiting our application

Now we can visit the application we just deployed by visiting the URL from the values definition of our application. This will be in the form of [https://my-username.cdro-workshop.cb-demos.io](https://my-username.cdro-workshop.cb-demos.io).

You should see the name of your username and the environment QA listed. 

![Deployment app](deployed-app.png)


In the next lab we'll be diving deeper into the environments and setting up environment specific variables.

<script defer src="../scripts/replacer.js" type="module"></script>
