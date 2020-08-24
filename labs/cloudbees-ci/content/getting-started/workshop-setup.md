---
title: "Workshop Setup"
chapter: false
weight: 2
---

In this lab you will setup a work environment for the CloudBees CI Workshop.  

If you are attending a CloudBees led workshop then these setup steps should be completed before the start of the workshop event.

## GitHub Setup

### Create a GitHub.com Account

Feel free to use an existing GitHub.com account or create a new one:
1. In a new browser tab or window, visit [https://github.com/join](https://github.com/join) and fill in the required fields to create a GitHub.com user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

### Create a GitHub Organization

We recommend creating a new GitHub Organization for the CloudBees CI Workshop. We will be using a GitHub App based credential for authentication and authorization between GitHub.com and CloudBees CI.
1. Ensure that you are logged into GitHub.com and then navigate to your [Organizations Settings page](https://github.com/settings/organizations). 
2. Click on **New Organization** <p><img src="setup-github-new-org.png" width=550/>
3. Fill in the **Organization Name**, **Billing Email**, and click on **Create Organization**<p><img src="setup-create-org.png" width=550/>
4. On the **Invite organization members** - just click the **Continue** button. On the next page, **Enter Organization Details**, either click **Submit** button or **skip this step** to finish creating the GitHub Organization.

>NOTE: Even though you have to provide an email for billing, **you will NOT be charged anything** as long as you choose the free option.

### Install GitHub App

1. Ensure that you are logged into GitHub.com and then navigate to [https://github.com/apps/cloudbees-ci-workshop](https://github.com/apps/cloudbees-ci-workshop).<p>![GitHub App](cbci-github-app.png?width=70pc)
2. Click on the **Configure** button.
3. Next, select the GitHub Organization you created for the CloudBees CI Workshop.<p>![GitHub App](github-app-select-org.png?width=70pc)
4. On the next screen, select **All repositories** and click the **Install** button.<p>![GitHub App](github-app-install.png?width=70pc)
5. You may be prompted for your GitHub password. Enter your password to complete the installation of the CloudBees CI Workshop GitHub App into your workshop specific GitHub Organization.
    
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#16).**
