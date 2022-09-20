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

Now your catalog item is ready to go. You can switch back over to the usable catalog list by clicking on **Serive catalog** at the top.
![New SSC](25.png)

Now you can create a new release from this template:
![New SSC](26.png)





<script defer src="../scripts/replacer.js" type="module"></script>
