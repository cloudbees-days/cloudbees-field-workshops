---
title: "CloudBees CI Setup"
chapter: false
weight: 3
--- 

In this lab you will provision a CloudBees managed controller (Jenkins instance) with the initial configuration provided by CloudBees CI CasC.

*If you haven't already received the link for the CloudBees CI Workshop cluster, then ask your instructor for it.

## Provision a CloudBees CI Managed Controller

### Create a CloudBees CI Account

1. Navigate to the CloudBees CI Workshop registration form. The URL will be provided by your instructor.
2. Fill out the form, using your GitHub username as your CloudBees CI username, the same email you used to sign-up for the CloudBees Workshop Slack workspace, and make sure to save your password. <p>![Create Account](registration-form.png?width=40pc)
3. Click the **Create Account** button.

### Login to CloudBees CI

1. Goto to the Workshop URL provided by the instructor.
2. Enter the username and password you created earlier into the login screen and click the **Sign in** button.<p>![CloudBees CI Login](setup-login.png?width=40pc)

## Create a CloudBees CI Managed Controller (Jenkins instance)

1. Click on the **Create Team** link near the top of the page.<p>![Create Team](create-team-link.png?width=70pc)
2. Fill out the form and click the **Build** button.<p>![Create Team form](create-team-form.png?width=70pc)
3. **IMPORTANT** - While your CloudBees CI managed controller (Jenkins instance) is being provisioned (**it takes a few minutes for Operations Center to provision your managed controller on Kubernetes**), move onto the next section.

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#16).**