---
title: "Environments"
chapter: false
weight: 5
--- 

Application modeling is only one part of managing deployment automation with CloudBees CD/RO. The other main part is environment modeling. 

With application modeling you describe what the processes are that can be run against an application. Now with the environment modeling you are defining where these processes can occur.

It is important that these two be separate or else there would be a lot of repetition of effort. With this setup you only need to define the application processes once and then point them at the target environments. Properties from the environment can then be passed along to the application process during runtime.

In the previous lab we took a look at the application modeling process and setup a microservice definition. As part of this we created our first environment in which we would deploy our application.

## Reviewing the environment we've created

Let's take a look at the environment we created in the previous lab in more detail. On the *Hierarchy Menu* on the left side of the screen, you can click on the "Environment: QA" link at the bottom. This will bring you to the environment page. 

![Click on environment](click-environment.png)

Here are the resources you defined in the environment creation form. There is the `default` Kubernetes cluster definition on the right and the *Utility Agent* named `k8s-agent` on the left. If there were more components involved in this environment they could be easily added. This is more prevalent in traditional applications where you may be targeting multiple different servers.

In our case, since we're using Kubernetes, we don't need to worry about individual servers.
![Environment page](env-1.png)

### Environment runs

One of the challenges of maintaining many environments is keeping track of what has actually been going on in those environments.

CD/RO makes this easy with the **Runs on this environment** view. Here you can see all of the application runs that have taken place in this environment.

If you click on the **Runs on this environment** button on the secondary menu, you should see the application run that you performed from the previous lab. You could click into if you wanted to in order to review those details.

![Environment runs](env-2.png)


### Environment inventory

One of the other challenges of maintaining many environments is actually knowing what is installed in those environments.

This is where the **Inventory** view comes into play. The inventory shows you what applications are installed in the environment, which version is installed, and when that occurred.

If you navigate to this view by clicking the **Inventory** button on the secondary menu, you should see something like the following.

![Environment inventory](env-3.png)


## Adding a production environment

Now that we've got this fully functional QA environment, let's create another environment that we can deploy our application into.

We'll call this our **Production** environment.

To get started, let's go back to the application view by first going to the "Environment editor view" and clicking the `Application: Welcome App` link in the bottom of the *Hierarchy Menu*.

![Environment editor](env-4.png)

You can also navigate there via the main menu (aka the *burger menu*) by going to Applications under Deployment Automation.

![App menu](app-burger-menu.png)

To add a new environment, click the large plus button on the right side of the QA environment.

![New environment button](prod-1.png)

You'll now see a familiar "New environment" block with a "New cluster" block inside of it. We are essentially going to repeat our steps from the previous lab.

![New environment block](prod-2.png)

First, click on the "New Cluster" button in the inner block. This will pop up the New environment modal. Like before, you'll just click "Next", leaving the default option of "New environment".

![New environment modal](prod-3.png)

This will look remarkably similar to before. We'll just replace the values of QA that we used previously with that of Production.

| Field                   | Value                   | Description                                                                                                                            | 
|-------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Environment name        | `Production`            | The name to identify your environment                                                                                                  |
| Project                 | Select your project     | The project inside which this environment will be stored                                                                               |
| Environment description | *Optional*              | A field to give textual details about this environment                                                                                 |
| Cluster name            | `default`               | A name to identify this cluster                                                                                                        |
| Cluster description     | *Optional*              | A field to give textual details about this cluster                                                                                     |
| Configuration provider  | `Kubernetes (via Helm)` | The type of environment you're defining                                                                                                |
| Configuration name      | `helm`                  | A reference to a configuration that lets CD/RO know where to use Helm                                                                  |
| Namespace               | `my-username-prod`      | The Kubernetes namespace where your application will be deployed. You should update this to be YOUR_USERNAME-prod.                     |
| Kubeconfig context      |                         | This allows you to target a specific cluster if your configuration is pointed at multiple. For this workshop you can leave this blank. |
| Utility resource name   | `k8s-agent`             | This is the name to identify the utility resource                                                                                      |
| Resource                | `k8s-agent`             | This is the agent which will communicate with the Kubernetes cluster                                                                   |

![New environment form](prod-4.png)

Next we need to map this new environment to the application. 


![Map new environment](prod-5.png)

Drag the arrow into the Kubernetes cluster within the Production environment.
![Map environment](prod-6.png)

You'll have a popup asking you to confirm the mapping. Go ahead and click "OK".

![Map environment - confirm](prod-7.png)

Now you're ready to deploy into the production environment. Like before, you can click the "Deploy" button, but this time select the Production environment.

![Deploy app into prod](prod-8.png)

This should successfully deploy into the production environment.

![Production deploy success](prod-9.png)


One question may be occurring to you: Didn't we hardcode the URL for the application?

That is right! Right now we've deployed our application into two different environments, yet we have the same URL set for both. That's not what we want!

This is where we'll bring in some environment properties.

## Environment specific properties

We're going to make some modifications that will allow us to deploy to each environment with some key differences including different URLs and different environment variables passed into the deploy.

### Adding subdomain environment variable
First, you'll add a property to the two environments that specifies a subdomain. Then you'll update the application model to use this subdomain so each deployment can actually be accessed.

We'll start with the QA environment. You can add a property by clicking on the menu with the three dots on the QA environment box. 

![Add a property](envvars-1.png)
![Add a property](envvars-2.png)
![Add a property](envvars-3.png)

Go ahead and fill it out with the properties:

| Property | Value |
| --- | --- |
| subdomain | `my-username-qa` |

You can leave all the other values default and save it by clicking **OK**.

![New property](envvars-4.png)

Now go ahead and do the same for the production environment, except use these properties:

| Property | Value              |
| --- |--------------------|
| subdomain | `my-username-prod` |

![New property](envvars-5.png)

And with that, we're ready to update the application model.

### Updating the app model

Let's go back to the application model. Go ahead and click on the **Details** option in the menu for the **hello-app** model.

![Update app details](envvars-6.png)
![Update app details](envvars-7.png)

We'll update the values block to interpolate some values rather than using the hardcoded values we started with. To make sure you get all the values right, you can copy the following block.

```yaml
ingress:
  hosts:
    - host: $[/myEnvironment/subdomain].cdro-workshop.cb-demos.io
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls:
    - secretName: insurance-frontend-tls
      hosts:
        - $[/myEnvironment/subdomain].cdro-workshop.cb-demos.io

name: "$[/myJob/launchedByUser]"
environment: "$[/myEnvironment/name]"
```

What we're doing here is using the `$[propertyName]` syntax to access the values of particular properties. There are a bunch of properties we can access throughout the platform, but in this case we want to reference a few related to this particular environment and deployment.

| Property                      | Description                                                                        |
|-------------------------------|------------------------------------------------------------------------------------|
| `$[/myEnvironment/subdomain]` | Accesses the `subdomain` property on the environment targeted by a deployment run. |
| `$[/myEnvironment/name]`      | Accesses the name of the environment targed by a deployment run.                   |
| `$[/myJob/launchedByUser]`    | Grabs the name of the user who kicked off the run.                                 | 


You can do this by using the syntax of `$[propertyName]` to access the value of a particular property. There are a bunch of properties we could access throughout the platform, but in this case we want to reference the current environment we're running against.

## Running the deployments
With these new settings in place, go ahead and deploy into the QA environment.

![New run](rerun-1.png)
![New run](rerun-2.png)
![New run](rerun-3.png)

This should run fairly quickly. Once it is complete, you can access your application at: `my-username-qa.cdro-workshop.cb-demos.io`

<div id="qa-env-link"></div>

![QA new run](rerun-4.png)

Now go ahead and do the same for the production environment. You'll be able to access the production application at: `my-username-prod.cdro-workshop.cb-demos.io`
<div id="prod-env-link"></div>

![Production new run](rerun-5.png)


After deploying both applications you should now see:
1. You can now access the two different deployments on different URLs
2. Your username should appear in the **Deployed by** field
3. The **Environment** field should reflect the environment it is running in


## Up next

In the next lab you'll be integrating the application and environment models you've worked on over the past 2 labs into the release from the first lab.


<script defer src="../scripts/replacer.js" type="module"></script>
<script defer src="../scripts/env-access-buttons.js" type="module"></script>
