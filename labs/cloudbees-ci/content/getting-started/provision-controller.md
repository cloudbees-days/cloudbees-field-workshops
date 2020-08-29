---
title: "CloudBees CI Setup"
chapter: false
weight: 3
--- 

CloudBees CI for modern platforms takes advantage of Kubernetes to providing dynamic provisioning of team specific Jenkins instances we refer to as ***managed controllers***. In this lab you will provision a CloudBees ***managed controller*** (Jenkins instance) with an initial configuration provided by CloudBees CI Configuration-as-Code.

>NOTE: If you haven't already received the link for the CloudBees CI Workshop cluster, then ask your instructor for it.

## Provision a CloudBees CI Managed Controller

### Create a CloudBees CI Account

1. Navigate to the CloudBees CI Workshop registration form. The URL will be provided by your instructor.
2. Fill out the form, using your GitHub username as your CloudBees CI username, the same email you used to sign-up for the CloudBees Workshop Slack workspace, and make sure to save your password. <p>![Create Account](registration-form.png?width=40pc)
3. Click the **Create Account** button.

### Login to CloudBees CI

1. Goto to the Workshop URL provided by the instructor.
2. Enter the username and password you created earlier into the login screen and click the **Sign in** button.<p>![CloudBees CI Login](setup-login.png?width=40pc)

## Create a CloudBees CI Managed Controller (Jenkins instance)

1. Click on the **Create Team** link near the top of the page. ![Create Team](create-team-link.png?width=70pc)
2. Fill out the form and click the **Build** button. ![Create Team form](create-team-form.png?width=70pc)
3. After the **Create Team** setup job completes you should see the following repositories forked into the GitHub Organization.
   - https://github.com/cloudbees-days/cloudbees-ci-config-bundle
   - https://github.com/cloudbees-days/pipeline-library
   - https://github.com/cloudbees-days/pipeline-template-catalog
   - https://github.com/cloudbees-days/pipeline-policies
   - https://github.com/cloudbees-days/simple-java-maven-app ![GitHub App Installed](forked-repos.png?width=50pc)
4. **IMPORTANT** - While your CloudBees CI managed controller is being provisioned (**it takes a few minutes for Operations Center to provision your managed controller on Kubernetes**), move onto the next section.

>NOTE: There are a number of ways to create a managed controller. We take a very opinionated way to provision attendees managed controllers for this workshop in order to pre-configure the components that you will interact with during the workshop.

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#16).**