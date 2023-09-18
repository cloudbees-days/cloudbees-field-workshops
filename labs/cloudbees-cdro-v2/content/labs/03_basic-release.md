---
title: "Basic release"
chapter: false
weight: 3
--- 

One of the primary objects in the CloudBees CD/RO application is the release. This is where you can map out the whole delivery process for a given software release. 

With a release pipeline in place you can be certain that all the operations occur in the correct order every single time.

## Creating a release from a template

When you're first logged in you'll see something that looks like this.

![Release screen](basic-release/1.png)

This is where you'll see all the release across everyone's projects. You can filter this down using the set of filters at the top. We'll come back to this in a minute.

First we'll go to the **Service Catalog** which you'll find in the top navigation.

![Service catalog](2.png)

The service catalog is a collection of pre-made content that can be instantiated by anyone with permissions.

To get started with this lab you'll click create on the **1. Basic Release** item.

![Service catalog form](3.png)

Fill out the form with your desired release name. For your convenience in finding yours you may want to name it something like `my-username Release`.

With that complete, you can navigate back to the release list by opening the "burger" menu at the top left and navigating to the **Release Orchestration > Releases** item.

![Navigate to releases](4.png)
![Release list](5.png)

If you'd like to make it easier to keep track of your specific release, you can use the project filter at the top.

![Filter releases](6.png)
![Filtered releases](7.png)

Now you can click on the name of your release, and it'll bring you into the release. 

![First release](8.png)

A release is made up of a bunch of tasks spread across multiple stages. In this case, you can see that your release has 3 different stages: **Release Readiness**, **Quality Assurance**, and **Production**.

You can have as many stages as you want. Typically, you'll have a stage to represent each of the different environments that are involved in the release process. In the next couple of labs we'll dive into the environment modeling capabilities.  

Let's look at what steps are already setup in this release.

## Release overview

In the **Release Readiness** stage there are two data gathering tasks. 

1. Grab the changelogs from the application source code in GitHub
2. Pull the static code analysis results of the latest SonarQube scan

If you were using a tool like Jira for issue tracking, you would likely also want to pull information about the stories surrounding this release.

Next is the exit gate on the **Release Readiness** stage. You can expand this by clicking the dark gray box on the right side of the stage.

![Closed exit gate](9.png)
![First exit gate](10.png)

This is the exit gate where the criteria to allow the release to continue past this stage is defined. The criteria can be both automatic and manual.

Here you can see there is one called **No Code Smells** which is pulling information from the **Get latest SonarQube scan results** task and ensuring there were no code smells.

Like the exit gate, you can also define an entry gate on each stage to specify the criteria for when the release can enter the stage.

Next there are two stages, **Quality Assurance** and **Production** that each currently have a single task. These tasks are mocking where we'll eventually add a deployment step. Currently, they are just a simple `echo "Replace me"` command.

![First release](8.png)
![Mock deployment](11.png)

## Running the release

Now that you've looked through your current release, go ahead and run it. Over on the right side of the screen, you'll see a floating green button with a play icon in it.

![Start release](12.png)

Once you click **Start release** a modal will pop up where you could pass in parameters and select which stages you want to run.

![Start release form](13.png)
![Start release form](14.png)

Let's leave the default options and run through all the stages. Go ahead and click **Run**.

![First release run](15.png)

This will take you to your release run. It should quickly execute. You should see that everything has turned green and each stage will have a checkmark showing that it was successfully completed.

You can check out the summary for each stage by clicking the **Summary** button towards the top of each stage.

![Release readiness summary](16.png)

To do a deeper dive on the data from a given task you can click on the task. You can see the logs as well as the properties that are pulled from any external tools.

![Release readiness summary](17.png)
![Release readiness summary](18.png)

## Making a change
Our release pipeline isn't going to be winning any awards at the moment. Besides the fact that the deployments are just mocked out at the moment, there aren't any sort of checks between the QA deployment and the production deployment.

Currently, if the deployment into QA failed, it would still go on to attempt the deployment into production. That is not what we want!

What we'll do is add an approval to the entry gate into the **Production** stage to ensure the production deployment only occurs when it is safe to do so.

_Note: You may want to get to a point where there are no manual approvals, everything is fully automated. This is easy to do. You need to add validators like we have on the exit gate of the **Release Readiness** stage which pull data from your tests. The key is to make sure that you have sufficient tests that you feel confident in deploying to production._

To add this entry gate, expand the entry gate panel on the left side of the **Production** stage.

![New entry gate](20.png)

You can call this entry gate whatever you would like. In the screenshot you can see it called `Manual approval`. Then select the rule type of **Approval**.

![New entry gate](21.png)

Then click on the **Define** button to configure the approval.

![New entry gate](22.png)
![New entry gate](23.png)

Go ahead and assign this approval to yourself. You can add a message if you'd like as well.

You may notice when you go to assign yourself that you can assign both users and groups. Often times you'll want to assign a specific team rather than a person. You can specify the minimum number of users who need to approve it as well to ensure more than one set of eyes is looking at it.

![New entry gate](24.png)

Go ahead and click **OK**.

With that you've successfully made your release a bit more practical.

![Updated release](25.png)

## Rerunning the release
With your new change in place, go ahead and kick off your release again. 

After having run your release before, you'll notice the floating green "play" button is now blue and a vertical dots icon. You can click **Run pipeline** to kick it off with a fresh set of settings, or you can do **Previous run** to reuse whatever settings you used previously.

In our case, we just used the default settings so either one will work identically.

![Rerun release](26.png)

The release will start running and you'll quickly see that it is paused while waiting for the manual approval.

![Rerun release](27.png)

Before responding to the approval, let's take a quick look at a separate view where you can always see which releases are waiting on you. On the top bar, go ahead and click on the **My work** item.

![My work](28.png)
![My work page](29.png)

This list will have an always up-to-date list of all the manual tasks requiring your input.

Alright, now back to the release run. If you didn't open the **My Work** page in a new tab, you can click on the **Go to** arrow on the right side of the list item to bring you back.

Go ahead and click on the approval where it says **Response required**. Then click the item in the dropdown to bring up the approval modal.

![Approval](30.png)
![Approval](31.png)

And with that approval complete, your release should successfully complete. 
![Complete release](32.png)

## Automatic auditing

Before we move on to the next lab, let's take a quick peak at the automatic auditing that has happened on this release.

Go to the actions menu in the top right of the release run and click on **Audit Reports**.
![Audit report item](33.png)

Here you can see all the information that is automatically gathered for each and every release run. You don't have to do anything to configure this, it just happens automatically. You can export this and share it with your auditors.

![Audit report](34.png)
![Audit report](35.png)
![Audit report](36.png)

And with that, we're on to the next lab where we'll take a look at the basics of **Deployment Automation**.



<script defer src="../scripts/replacer.js" type="module"></script>

