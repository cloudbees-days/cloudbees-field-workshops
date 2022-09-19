---
title: "Self-service catalog"
chapter: false
weight: 8
--- 

Now we have created the release in two ways.  First we started with a basic release from the service catalog, then we created a pipeline and used that to start our release.  The first way was nice because we just used the **Service Catalog** to start the release, but we needed to customized it a lot.  The second way was nice because it gave us a nice way to see what the release pipeline would look like and a easy way to modify it before starting the release.

Next, lets combine both methods together to give us a nice way to start a release by selecting the pipeline we want to use for the release and automatically add an application.  We have been using DSL more and more through this workshop and here we will use DSL to define our new **Service Catalog** item.

Again I have provided some DSL code so you don't need to write it all your self.

## Getting familiar with the DSL

Almost everything in the platform can be described as DSL. In fact, on most objects like releases, application models, environment models, permissions, and more you can click on the action menu and click **DSL Export** to get the code.

When on the page for your release, you'll see a menu item at the top that says **DSL Editor** where you can directly see the DSL for this release pipeline.

![Grabbing the DSL](1.png)
![DSL editor](2.png)

As you navigate around, you'll see the different tasks that you've created. For instance, below is the manual approval we added in Lab 1. 

![Manual approval DSL](3.png)

One thing you'll probably notice is that there are a lot of null values. This can be useful to see all the fields that are available to you, however when we export this we'll have an option to remove the blank fields so that we are only left with the fields that have been modified.

An important note is that this is two-way bound. As you make changes in the DSL and save it, that will reflect in the **Release Editor** view. When you add tasks as we did in the previous labs, that will reflect in the DSL. 

It is beyond the scope of this workshop, but you can also [sync DSL with a git repository](https://docs.cloudbees.com/docs/cloudbees-cd/latest/configure/source-code-synchronization) to enable a GitOps approach for managing the configuration of your environment. 


## Creating the self-service catalog with DSL

I have already create some DSL you can use for your new catalog item as follows:

```groovy
def CurrentUser = getProperty("/myUser/userName").value

catalog CurrentUser, {
  iconUrl = null
  projectName = CurrentUser

  catalogItem 'Create Release From Pipeline', {
    description = '''<xml>
    <title>
      Create a new released based on pipeline templates
    </title>

    <htmlData>
      <![CDATA[
        Create a new release from existing pipeline templates
      ]]>
    </htmlData>
  </xml>'''
    buttonLabel = 'Create'
    catalogName = CurrentUser
    dslString = '''def StartDate = (new Date())
  def StartDateStr = (String) StartDate.format( "yyyy-MM-dd" )
  def EndDateStr = (String) (StartDate+14).format( "yyyy-MM-dd" )

  release args.releaseName, {
    projectName = args.targetProject

    plannedStartDate = StartDateStr
    plannedEndDate = EndDateStr
    
    pipelineProjectName = args.templateProject
    pipelineName = args.templateRelease
    
    Release_Name = args.releaseTag
    String[] tags = args.releaseTag.replaceAll("[.]", "").split(",");
    for (String tagItem: tags) {
      tag tagItem
    }

    deployerApplication 'Workshop App', {
        processName = 'Deploy Application'
        deployerConfiguration 'QA', {
            deployerTaskName = 'Deploy to QA'
            environmentName = 'QA'
            processName = 'Deploy Application'
            stageName = "Quality Assurance"
        }
        deployerConfiguration 'PROD', {
            deployerTaskName = 'Deploy to Production'
            environmentName = 'QA'
            processName = 'Deploy Application'
            stageName = "Production"
        }
    }


  }'''
    endTargetJson = '''{
    "source": "parameter",
    "object": "release",
    "objectName": "releaseName",
    "objectProjectName": "targetProject",
    "objectId": "id"
  }'''
    iconUrl = 'icon-pipeline.svg'
    projectName = CurrentUser
    useFormalParameter = '1'

    formalParameter 'templateProject', defaultValue: 'Default', {
      label = 'Template Project'
      orderIndex = '1'
      required = '1'
      type = 'project'
    }

    formalParameter 'templateRelease', defaultValue: 'pipeline_Base', {
      label = 'Template Release'
      orderIndex = '2'
      projectFormalParameterName = 'templateProject'
      required = '1'
      type = 'pipeline'
    }

    formalParameter 'targetProject', defaultValue: CurrentUser, {
      label = 'Target Project'
      orderIndex = '3'
      required = '1'
      type = 'project'
    }

    formalParameter 'releaseName', {
      label = 'Release Name'
      orderIndex = '4'
      required = '1'
      type = 'entry'
    }

    formalParameter 'releaseTag', {
      label = 'Release Tags'
      orderIndex = '5'
      required = '1'
      type = 'entry'
    }

    formalParameter 'applicationName', defaultValue: 'Workshop App', {
      expansionDeferred = '0'
      label = 'Application Name'
      orderIndex = '6'
      projectFormalParameterName = 'targetProject'
      required = '1'
      type = 'application'
    }

  }

}
```

Now this DSL can give us a release based on a release pipeline just like we did in the last module, but it also lets us specify an application.  With that information it will have enough to generate a new release just like last time.

If you were to go to the DSL IDE by going to the "burger menu" and going to **DevOps Essential > DSL IDE** you can paste this code and run it. This should run just fine.

![DSL IDE](6.png)
![DSL IDE](7.png)
![DSL IDE](8.png)

This is good though, we have all the pieces we need. Now it is time to templatize this DSL.

## Creating the self-service catalog in the UI

First you'll need to navigate to the **Service Catalog** by clicking on the item in the top navigation.

![SSC Link](9.png)

Next, you'll need to click on the plus button in the top right to create a new catalog. Then click **Create new...**. Then give it the same name as your username, and make sure it is targeting your project. Then hit **OK**.

![New SSC](10.png)
![New SSC](11.png)
![New SSC](12.png)

This will then bring you into the catalog editor where it'll prompt you to create your first catalog item. Go ahead and create one with the following values:

| Field       | Value                                                                                       |
|-------------|---------------------------------------------------------------------------------------------|
| Name        | Welcome App Release                                                                         |
| Description | _(optional) This will give you a basic release across QA + Production for the Welcome App._ |

Then go ahead and click **Done**.


![New SSC](13.png)
![New SSC](14.png)

This then brings you to the list of catalog items within the catalog. There is just the one you've created and it still requires a definition. Go ahead and click on **Requires Definition** to get into the editor.
![New SSC](15.png)

Up at the top you can configure options such as what the button label appears as, what icon the catalog item shows, and additional information you may want to convey to the end user. You're free to choose whichever you would like. We're going with the **Create** label and the **CloudBees CD** icon.

![New SSC](16.png)

Next is the item definition. You can see on the left side, you can choose whether this will run some DSL, run a plugin procedure, or run a custom procedure. In this case we're going to go with the DSL that we templatized earlier.

There is this **End Target JSON** field which enables you to directly link to the resource that is created by the template once it is created. Here you'll want to select the **Use Formal Parameters** option and then paste in the following:

```json
{
      "source": "property",
      "object": "release",
      "objectName": "$[/myUser/ReleaseName]",
      "objectProjectName": "$[/myUser/userName]"
}
```

![New SSC](17.png)

At the bottom is where it wants the DSL for the resources it will create. In this case, we'll copy the templatized DSL from up above. For your convenience, here it is again:

```groovy
def CurrentUser = getProperty("/myUser/userName").value
def UserProject = "${CurrentUser}"

def ReleaseName = args.releaseName

def StartDate = (new Date())
def StartDateStr = (String) StartDate.format("yyyy-MM-dd")
def EndDateStr = (String) (StartDate + 14).format("yyyy-MM-dd")

release ReleaseName, {
  plannedEndDate = EndDateStr
  plannedStartDate = StartDateStr
  projectName = UserProject

  pipeline 'pipeline_Base', {
    releaseName = ReleaseName

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
          subproject = UserProject
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
        subproject = UserProject
        taskType = 'DEPLOYER'
      }
    }

    stage 'Production', {
      colorCode = '#2ca02c'
      pipelineName = 'pipeline_Base'
      gate 'PRE', {
        task 'Manual approval', {
          gateType = 'PRE'
          instruction = 'Validate that everything is good before deploying into production.'
          notificationEnabled = '1'
          notificationTemplate = 'ec_default_gate_task_notification_template'
          subproject = UserProject
          taskType = 'APPROVAL'
          approver = [
            UserProject,
          ]
        }
      }

      gate 'POST', {
        }

      task 'Deploy to Production', {
        deployerRunType = 'serial'
        subproject = UserProject
        taskType = 'DEPLOYER'
      }
    }

    // Custom properties

    property 'ec_counters', {

      // Custom properties
      pipelineCounter = '10'
    }
  }

  deployerApplication 'Workshop App', {
    processName = 'Deploy Application'

    deployerConfiguration 'QA', {
      deployerTaskName = 'Deploy to QA'
      environmentName = 'QA'
      processName = 'Deploy Application'
      stageName = 'Quality Assurance'
    }

    deployerConfiguration 'PROD', {
      deployerTaskName = 'Deploy to Production'
      environmentName = 'Production'
      processName = 'Deploy Application'
      stageName = 'Production'
    }
  }
}
```
![New SSC](18.png)

Go ahead and click **OK** once all of that is copied over.

Then you'll be back in the catalog editor with your newly defined item. Except there is one thing we're still missing. Towards the top of the DSL block we have a variable that is reference an input parameter.

```groovy
def ReleaseName = args.releaseName
```

In order for this to work properly, you'll need to add the parameter to the catalog item. You do this by clicking on the action menu for the catalog item and going to **Parameters**. Then click on the button to add a new parameter.

![New SSC](19.png)
![New SSC](20.png)
![New SSC](21.png)

Here you'll need to define the parameter with the right name to ensure it matches what the DSL is looking for.

| Field | Value        | Description                                                    |
|-------|--------------|----------------------------------------------------------------|
| Name  | releaseName  | This is the identifier which is what needs to match in the DSL |
| Label | Release Name | This is the visual name which shows up in the form             |

Go ahead and click **OK** once you've entered these in.

![New SSC](22.png)
![New SSC](23.png)
![New SSC](24.png)

Now your catalog item is ready to go. You can switch back over to the usable catalog list by clicking on **View catalog** at the top.
![New SSC](25.png)

Now you can create a new release from this template:
![New SSC](26.png)





<script defer src="../scripts/replacer.js" type="module"></script>
