---
title: "Workshop Setup"
chapter: false
weight: 2
---

In this lab you will setup a work environment for the CloudBees CI Workshop.  

If you haven't already received the link for the CLoudBees CI Workshop cluster, then ask your instructor for it.

## GitHub

### Create a GitHub.com Account

Feel free to use an existing GitHub.com account or create a new one:
1. In a new browser tab or window, visit [https://github.com/join](https://github.com/join) and fill in the required fields to create a GitHub.com user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

### Create a GitHub Organization

We recommend creating a new GitHub Organization for the CloudBees CI Workshop. We will be using a GitHub App based credential for authentication and authorization between GitHub.com and  CloudBees CI.
1. Ensure that you are logged into GitHub.com and then navigate to your [Organizations Settings page](https://github.com/settings/organizations). 
2. Click on **New Organization** <p><img src="setup-github-new-org.png" width=550/>
3. Fill in the **Organization Name**, **Billing Email**, and click on **Create Organization**<p><img src="setup-create-org.png" width=550/>
4. On the **Invite organization members** - just click the **Continue** button. On the next page, **Enter Organization Details**, either click **Submit** button or **skip this step** to finish creating the GitHub Organization.

>NOTE: Even though you have to provide an email for billing, **you will NOT be charged anything** as long as you choose the free option.

### Install GitHub App

1. Ensure that you are logged into GitHub.com and then navigate to [https://github.com/apps/cloudbees-ci-workshop](https://github.com/apps/cloudbees-ci-workshop).<p>![GitHub App](cbci-github-app.png?width=70pc)
2. Click on the 

## CloudBees CI

### Create a CloudBees CI Account

1. Navigate to the CloudBees CI Workshop registration form. The URL will be provided by your instructor.
2. Fill out the form, using your GitHub username as your CloudBees CI username, and make sure to save your password. <p>![Create Account](registration-form.png?width=40pc)
3. Click the **Create Account** button.

### Login to CloudBees CI

1. Goto to the Workshop URL provided by the instructor.
2. Enter the username and password you created earlier into the login screen and click the **Sign in** button.<p>![CloudBees CI Login](setup-login.png?width=40pc)

### Create a CloudBees CI Managed Controller (Jenkins instance)

1. Click on the **Create Team** link near the top of the page.<p>![Create Team](create-team-link.png?width=70pc)
2. In the left navigation menu, click on the **Build with parameters** link.<p>![Build with parameters](create-team-build-link.png?width=70pc)
3. Fill out the form and click the **Build** button.<p>![Create Team form](create-team-form.png?width=70pc)
4. **IMPORTANT** - While your CloudBees CI managed controller (Jenkins instance) is being provisioned (**it takes a few minutes to provision your managed controller (Jenkins instance)**), move onto the next section.
    
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#16).**
