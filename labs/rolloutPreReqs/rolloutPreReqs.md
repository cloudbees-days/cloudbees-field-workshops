# Rollout Pre-Workshop Set-Up

## Create a Workshop Account

1. Navigate to the registration form. The URL will be provided by your instructor.
2. Fill out the form and make sure to save your password. If you don't already have the **Invite code** it will be provided by your instructor. <p><img src="images/registration-form.png" width=600/>
3. Click the **Sign up** button.

## Create a GitHub.com Account

Feel free to use an existing GitHub.com account, otherwise create one:
1. Visit https://github.com/join and fill in the required fields to create a user account.
2. Select "Unlimited public repositories for free" when choosing your plan.
3. Verify your email account to ensure you account is activated.  An activated account will be **required** for the rest of this workshop.

## Create a GitHub Personal Access Token

1. Click on [this link to automatically select the required **Personal access token settings**](https://github.com/settings/tokens/new?scopes=repo,read:user,user:email,admin:repo_hook,admin:org_hook)
2. Click on **Generate Token**
3. As the success message says: **Make sure to copy your new personal access token now. You won’t be able to see it again!**  

## Create a GitHub Organization

1. On GitHub navigate to **Organizations**: https://github.com/settings/organizations (after logging in) 
2. Click on **New Organization** <p><img src="images/setup-github-new-org.png" width=550/>
3. Fill in the **Organization Name**, **Billing Email**, and click on **Create Organization**<p><img src="images/setup-create-org.png" width=550/>
4. On the **Invite organization members** - just click the **Continue** button. On the next page, **Enter Organization Details**, either click **Submit** button or **skip this step** to finish creating the GitHub Organization.

>NOTE: Even though you have to provide an email for billing, you will NOT be charged anything as long as you choose the free option.

### Login to CloudBees Core

1. Goto to the Workshop URL provided by the instructor.
2. Enter the username and password you created earlier into the login screen.<p><img src="images/setup-login.png" width=400/>

### Create a Team Master

1. If not in CloudBees Team UI, click on the **Teams** link in the left menu. <p><img src="images/setup-classic-ui-Teams-link.png" width=400/>
2. Click on the **Create team** button in the center of your screen.<p><img src="images/setup-create-a-team.png" width=400/>
3. **Name this team** - enter a name for your team - **IMPORTANT: to ensure uniqueness, use your GitHub username** and then click **Next**.<p><img src="images/setup-name-this-team.png" width=450/>
4. **Choose an icon for this team** to help uniquely identify your team - select an icon and color for your team and then click **Next**.
5. **Add people to this team** - your user will show up as a **Team Admin** and we won't be adding any additional users right now, but feel free to look around and then click **Next**.
6. **Select the cluster endpoint to create the team in** - just stick with the default value `kubernetes` and click **Next**.
7. **Select team master creation recipe** - click on the drop-down to see the options, but just stick with the **Basic** recipe.
8. Finally, click the **Create team** button. <p><img src="images/setup-create-team.png" width=450/>
9. While your Core Team Master is being created (**it takes anywhere from 2-3 minutes to provision your Team Master**), move onto the next section.
    
## Run the Rollout Workshop Setup Pipeline
You should see the following Blue Ocean **Pipelines** screen with a Pipeline named **rollout-workshop-setup** for your Team:
**Note to self: Need to paste new image here**

1. Click on the `rollout-workshop-setup` Pipeline job.
2. On the next screen, click on the **Run** button in the middle of the screen. **Replace image**<p><img src="images/workshop-setup-run.png" width=600/>
3. Fill in the required parameters: <p><img src="images/workshop-setup-input-form.png" width=400/>
   1. ***githubPat*** - the GitHub Personal Access Token you created above.
   2. The GitHub username/account id you used to create the above GitHub Personal Access Token.
   3. The name of the GitHub Organization you created above specifically for this workshop
   4. The Kubernetes Namespace where your Team Master has been deployed - **only change the default value if you are instructed to do so.**
4. Once you have provided the above required input parameters click the **Run** button at the bottom of the parameters input form.
5. Blue Ocean will automatically switch to the Pipeline **Activity** screen, click anywhere on the Pipeline run row to see the Pipeline run and view the logs. But make sure you don't click on the **Stop** button to the right of the red box in the screenshot below.<p><img src="images/workshop-setup-activity.png" width=600/>
6. **Please let me know if this happens for you** Once the **rollout-workshop-setup** Pipeline job is completed, your Team Master will be restarted so you should see a **Connect lost: waiting** alert in the bottom right of your Blue Ocean screen. <p><img src="images/workshop-setup-connection-lost.png" width=600/> <p>You may also experience a **503 Service Temporarily Unavailable** screen - that is because the actual Kubernetes Pod that your Team Master is running in is being re-created. Your Team Master will return in a few minutes.
7. To confirm that the success of the pipeline job, navigate to your Github Organization that you created for this workshop, and refresh the page. You should see the following repositories that were copied during the pipeline job:
* pipeline-template-catalog
* pipeline-library
* microblog-frontend

**For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1).**

Otherwise, you may proceed to the next lab: [**CloudBees Rollout Workshop Set-Up**](../rolloutSetup/rolloutSetup.md) or choose another lab on the [main page](../../README.md#workshop-labs).