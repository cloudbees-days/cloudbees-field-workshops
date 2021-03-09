---
title: "Pre-Workshop Setup"
chapter: false
weight: 2
--- 
#### <i class="fas fa-clock"></i> The pre-workshop setup should take you approximately 10 minutes to complete.

If you are attending a CloudBees led workshop then these setup steps should be completed before the start of the workshop event.

## GitHub Setup

### Create a GitHub.com Account

Feel free to use an existing GitHub.com account or create a new one:
1. In a new browser tab or window, visit [https://github.com/join](https://github.com/join) and fill in the required fields to create a GitHub.com user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

### Create a GitHub Organization

We highly recommend creating a new GitHub Organization for the CloudBees CI Pipeline Workshop. We will be using a GitHub App based credential to enable authentication and authorization between your GitHub.com Organization for the workshop and CloudBees CI.
1. Ensure that you are logged into GitHub.com and then navigate to this [link to create a new (and free) GitHub Organization](https://github.com/account/organizations/new?coupon=&plan=team_free). 
2. Enter a unique ***Organization account name***, a valid ***Contact email***, select **My personal account** for ***This organization belongs to*** and then click on the **Next** button.<p>![GitHub Org Set up](github-org-set-up.png?width=40pc) 
3. On the **Welcome to GitHub** screen just click the **Complete setup** button.<p>![GitHub Org Set up](github-org-welcome.png?width=50pc) 
4. On the final page you don't have to fill anything in/answer any questions (unless your really want to) and just scroll to the bottom of the page and click the **Submit** button.

>NOTE: Even though you have to provide an email for billing, **you will NOT be charged anything** as long as you choose the free option.

### Install the CloudBees CI Pipeline Workshop GitHub App

1. Ensure that you are logged into GitHub.com and then navigate to [https://github.com/apps/cloudbees-ci-pipeline-workshop](https://github.com/apps/cloudbees-ci-pipeline-workshop).<p>![GitHub App](cbci-pipeline-github-app.png?width=60pc)
2. Click on the **Install** button.
3. Next, select the GitHub Organization you created above for the CloudBees CI Pipeline Workshop.<p>![GitHub App](github-app-select-org.png?width=50pc)
4. On the next screen, select **All repositories** and click the **Install** button.<p>![GitHub App](github-app-install.png?width=50pc)
5. You may be prompted for your GitHub password. Enter your GitHub.com password, for the GitHub account you are using for this workshop, to complete the installation of the CloudBees CI Workshop GitHub App into your workshop specific GitHub Organization.
6. The CloudBees CI Pipeline Workshop GitHub App is now installed on your workshop GitHub Organization. <p>![GitHub App Installed](installed-now.png?width=50pc)
7. A few minutes after you install the CloudBees CI Workshop GitHub App you should see the following repositories created in your workshop GitHub Organization.
   - https://github.com/cloudbees-days/cloudbees-ci-config-bundle
   - https://github.com/cloudbees-days/pipeline-library
   - https://github.com/cloudbees-days/pipeline-template-catalog
   - https://github.com/cloudbees-days/node-js ![GitHub App Installed](forked-repos.png?width=50pc)

>NOTE: These repositories were created from GitHub template repositories in the [CloudBees Field Workshops GitHub Organization](https://github.com/cloudbees-days).

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#core-overview-title">return to the workshop slides</a>**
