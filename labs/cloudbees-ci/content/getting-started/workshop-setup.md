---
title: "Workshop Setup"
chapter: false
weight: 2
---

In this lab you will setup a work environment for the CloudBees CI workshop.  Ask the instructor for the URL of the server you will be using for the CloudBees CI Workshop.

<a href="https://youtu.be/AZetQJYIKU4" target="_blank">Instructor led video of lab.</a>

Today's URL for the CloudBees CI Workshop environment will be provided by your instructor.

## Create a GitHub.com Account

Feel free to use an existing GitHub.com account or create a new one:
1. In a new browser tab or window, visit https://github.com/join and fill in the required fields to create a user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

## Create a GitHub Personal Access Token

1. Click on [this link to automatically select the required **Personal access token settings**](https://github.com/settings/tokens/new?scopes=repo,read:user,user:email,admin:repo_hook,admin:org_hook,delete_repo)
2. Enter a name for your **New personal access token** (PAT) and notice that all the necessary **scopes** have already been checked off for you by using the link from above. <p><img src="create-pat.png" width=600/>
3. Click on **Generate Token** button at the bottom of the page.
4. Save your new GitHub personal access token. As the success message says: **Make sure to copy your new personal access token now. You won’t be able to see it again!**  

### Create a CloudBees CI Account

1. Navigate to the CloudBees CI Workshop registration form. The URL will be provided by your instructor.
2. Fill out the form, using your GitHub username as your CloudBees CI username, and make sure to save your password. <p>![Create Team](registration-form.png?width=50pc)
3. Click the **Create Account** button.

### Login to CloudBees CI

1. Goto to the Workshop URL provided by the instructor.
2. Enter the username and password you created earlier into the login screen.<p>![CloudBees CI Login](setup-login.png?width=40pc)

### Create a CloudBees CI Managed Controller (Jenkins instance)

1. Click on the **Create Team** link near the top of the page.<p>![Create Team](create-team-link.png?width=70pc)
2. In the left navigation menu, click on the **Build with parameters** link.<p>![Build with parameters](create-team-build-link.png?width=40pc)
3. Fill out the form and click the **Build** button.<p>![Create Team form](create-team-form.png?width=40pc)
4. **IMPORTANT** - While your CloudBees CI managed controller (Jenkins instance) is being provisioned (**it takes a few minutes to provision your managed controller (Jenkins instance)**), move onto the next section.

## Create a GitHub Organization

1. On GitHub navigate to **Organizations**: https://github.com/settings/organizations (after logging in) 
2. Click on **New Organization** <p><img src="setup-github-new-org.png" width=550/>
3. Fill in the **Organization Name**, **Billing Email**, and click on **Create Organization**<p><img src="setup-create-org.png" width=550/>
4. On the **Invite organization members** - just click the **Continue** button. On the next page, **Enter Organization Details**, either click **Submit** button or **skip this step** to finish creating the GitHub Organization.

>NOTE: Even though you have to provide an email for billing, you will NOT be charged anything as long as you choose the free option.
    
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#16).**
