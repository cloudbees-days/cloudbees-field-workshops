---
title: "Pipelines and Releases"
chapter: false
weight: 7
--- 

Now that you've spent all the time getting your release just right, you aren't going to want to create it from scratch again the next time you need a release.

You started your release from an existing self-service catalog item. In this lab, you're going to look at another way of building the steps in the release.  For this lab we are going to build a *pipeline*.  Pipelines are kind of like releases in that they will allow us to orchestrate several steps over many stages.  We can even have entry and exit gates to the different stages.  Pipelines however do not keep track of planned start and end dates or support the deployer task.  Once we define a release we can use it as the basis for our new releases.

Normally, you could define a pipeline similar to the way we built the stages in our release.  For this lab and to save you the trouble of building the pipeline over by providing the DSL code here for you to use.

# Building the Pipeline from DSL

The DSL code to create our release as a pipeline is as follows:

```groovy
def CurrentUser = getProperty("/myUser/userName").value
pipeline 'pipeline_Base', {
  projectName = CurrentUser

  formalParameter 'ec_stagesToRun', {
    expansionDeferred = '1'
  }

  stage 'Release Readiness', {
    colorCode = '#289ce1'
    pipelineName = 'pipeline_Base'
    gate 'PRE', {
      }

    gate 'POST', {
      task 'No Code Smells', {
        gateCondition = '$[/javascript myStageRuntime.tasks[\'Get latest SonarQube scan results\'].job.getLastSonarMetrics.code_smells != null || myStageRuntime.tasks[\'Get latest SonarQube scan results\'].job.getLastSonarMetrics.code_smells < 1]'
        gateType = 'POST'
        subproject = CurrentUser
        taskType = 'CONDITIONAL'
      }
    }

    task 'Git changelog', {
      actualParameter = [
        'branch': 'main',
        'commit': '',
        'config': '/projects/CloudBees/pluginConfigurations/cb-bot',
        'depth': '',
        'gitRepoFolder': '/tmp/demo-app',
        'mirror': 'false',
        'overwrite': 'true',
        'pathspecs': '',
        'referenceFolder': '',
        'repoUrl': 'https://github.com/cloudbees-days/cdro-workshop-demo-app',
        'resultPropertySheet': '/myJob/clone',
        'shallowSubmodules': 'false',
        'submodules': 'false',
        'tag': '',
      ]
      stageSummaryParameters = '[{"name":"cloneData","label":"cloneData"}]'
      subpluginKey = 'EC-Git'
      subprocedure = 'Clone'
      taskType = 'PLUGIN'
    }

    task 'Get latest SonarQube scan results', {
      actualParameter = [
        'config': '/projects/Default/pluginConfigurations/SonarQube',
        'resultFormat': 'propertysheet',
        'resultSonarProperty': '/myJob/getLastSonarMetrics',
        'sonarMetricsComplexity': 'all',
        'sonarMetricsDocumentation': 'all',
        'sonarMetricsDuplications': 'all',
        'sonarMetricsIssues': 'all',
        'sonarMetricsMaintainability': 'all',
        'sonarMetricsMetrics': 'all',
        'sonarMetricsQualityGates': 'all',
        'sonarMetricsReliability': 'all',
        'sonarMetricsSecurity': 'all',
        'sonarMetricsTests': 'all',
        'sonarProjectKey': 'demo-app',
        'sonarProjectName': 'demo-app',
        'sonarProjectVersion': '',
        'sonarTaskId': '',
        'sonarTimeout': '',
      ]
      subpluginKey = 'EC-SonarQube'
      subprocedure = 'Get Last SonarQube Metrics'
      taskType = 'PLUGIN'
    }
  }

  stage 'Quality Assurance', {
    colorCode = '#ff7f0e'
    pipelineName = 'pipeline_Base'
    gate 'PRE', {
      }

    gate 'POST', {
      }

    task 'Deploy to QA', {
      deployerRunType = 'serial'
      subproject = CurrentUser
      taskType = 'DEPLOYER'
    }
  }

  stage 'Production', {
    colorCode = '#2ca02c'
    pipelineName = 'pipeline_Base'
    gate 'PRE', {
      task 'Manual approval', {
        gateType = 'PRE'
        notificationEnabled = '1'
        notificationTemplate = 'ec_default_gate_task_notification_template'
        subproject = CurrentUser
        taskType = 'APPROVAL'
        approver = [
          CurrentUser,
        ]
      }
    }

    gate 'POST', {
      }

    task 'Deploy to Production', {
      deployerRunType = 'serial'
      subproject = CurrentUser
      taskType = 'DEPLOYER'
    }
  }
}
```

If you were to go to the DSL IDE by going to the "burger menu" and going to **DevOps Essential > DSL IDE** you can paste this code and run it. This should run just fine.

![DSL IDE](1.png)
![DSL IDE](2.png)
![DSL IDE](3.png)

The operations here are idempotent, meaning you can run them over and over without issue. It will make sure that the described state is the state in the system.

In this case, we've used DSL and created a new pipeline.  We can see this pipeline by going to the "burger menu" and going to **Release Orchestration > Pipelines**.

![DSL Template](4.png)
![DSL Template](5.png)

Now I can use this pipeline to create releases.  Since the deployer tasks are generic I can release any application with this pipeline.  I will need to define the applications, environments and processes for each release though.  Let's try that now then we will see how we cand automate even that.

## Starting a Release from a Pipeline

To start our release based on our new pipeline lets go to the "burger menu" and going to **Release Orchestration > Releases** and creating a new release, by clicking on the ![New Release Button](6.png)

![Releases](7.png)
![New Release Button](6.png)

The **New Release** dialog screen will popup.  We are going to be selecting **Create new...**

![New Release Step1](8.png)

Next you will be prompted to provide some more information about the release as follows:

![New Release Step2](9.png)

Fill in this form for your release and click **Next**.  

![New Release Step3](10.png)

We are going to create our release from the pipeline we just created from DSL.  You can use the drop down at the top left to filter down to your project (`my-username`) and select your `pipeline_Base`

![New Release](11.png)

Click **OK** then **OK** and we have a new release.

![New Release](12.png)

We could start this release, but we haven't defined what applications will be deployed, which environments they will be deployed to and what process to use to deploy them.  Let's do that now.

## Defining what we want to deploy

To define what we are deploying in the **Deployer** tasks in this release we will fist need to define what applications this release will be deploying.  To do that we will first click on the ![Applications Icon](13.png)

![Application Dialog](14.png)

Now we have our application associated with the release

![Application selected](15.png)

Now lets define the environments and processes by clicking on ![envs and configs](16.png)

![Application Map1](17.png)

Select a stage then add an environment

![Application Map2](18.png)

Select a stage then add a process

![Application Map2](19.png)

![Application Map2](20.png)

Repeate the process for the next stage.

![Application Map2](21.png)

OK, now we are ready to run our new release.  Click on the **Run** button ![runbutton](22.png)

![Application Map2](23.png)

# Up Next

That was a lot of work to start a release.  We did make things more repeatable and maintainable, but moving most of our logic to the **pipeline**.  We still had a lot of work to do once we started the release.  Let's make that simpler next by creating a **Service Catalog** 