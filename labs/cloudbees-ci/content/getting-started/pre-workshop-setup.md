---
title: "Pre-Workshop Setup"
chapter: false
weight: 2
--- 

If you are attending a CloudBees led workshop then these setup steps should be completed before the start of the workshop event.

## GitHub Setup

### Create a GitHub.com Account

Feel free to use an existing GitHub.com account or create a new one:
1. In a new browser tab or window, visit [https://github.com/join](https://github.com/join) and fill in the required fields to create a GitHub.com user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

### Create a GitHub Organization

We highly recommend creating a new GitHub Organization for the CloudBees CI Workshop. We will be using a GitHub App based credential to enable authentication and authorization between your GitHub.com Organization for the workshop and CloudBees CI.
1. Ensure that you are logged into GitHub.com and then navigate to your [Organizations Settings page](https://github.com/settings/organizations). 
2. Click on **New Organization** button.<p><img src="setup-github-new-org.png" width=550/>
3. Select the **Free** plan by clicking on the **Join for free** button.<p>![GitHub Org Free](github-org-free.png?width=60pc)
4. On the next screen, enter a unique ***Organization account name***, a valid ***Contact email***, select **My personal account** for ***This organization belongs to*** and then click on the **Next** button.<p>![GitHub Org Set up](github-org-set-up.png?width=40pc) 
5. On the **Welcome to GitHub** screen just click the **Complete setup** button.<p>![GitHub Org Set up](github-org-welcome.png?width=50pc) 
6. On the final page you don't have to fill anything in/answer any questions (unless your really want to) and just scroll to the bottom of the page and click the **Submit** button.

>NOTE: Even though you have to provide an email for billing, **you will NOT be charged anything** as long as you choose the free option.

### Install the CloudBees CI Workshop GitHub App

1. Ensure that you are logged into GitHub.com and then navigate to [https://github.com/apps/cloudbees-ci-workshop](https://github.com/apps/cloudbees-ci-workshop).<p>![GitHub App](cbci-github-app.png?width=60pc)
2. Click on the **Configure** button.
3. Next, select the GitHub Organization you created for the CloudBees CI Workshop.<p>![GitHub App](github-app-select-org.png?width=50pc)
4. On the next screen, select **All repositories** and click the **Install** button.<p>![GitHub App](github-app-install.png?width=50pc)
5. You may be prompted for your GitHub password. Enter your GitHub.com password, for the GitHub account you are using for this workshop, to complete the installation of the CloudBees CI Workshop GitHub App into your workshop specific GitHub Organization.
6. The CloudBees CI Workshop GitHub App is now installed on your workshop GitHub Organization. <p>![GitHub App Installed](installed-now.png?width=50pc)
7. Shortly after you install the CloudBees CI Workshop GitHub App on your workshop GitHub Organization you should see the following 4 repositories forked into your Organization.
   1. https://github.com/cloudbees-days/cloudbees-ci-config-bundle
   2. https://github.com/cloudbees-days/pipeline-library
   3. https://github.com/cloudbees-days/pipeline-template-catalog
   4. https://github.com/cloudbees-days/simple-java-maven-app<p>![GitHub App Installed](forked-repos.png?width=50pc)
    
