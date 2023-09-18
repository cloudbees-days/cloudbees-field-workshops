---
title: "CloudBees Feature Management Setup"
chapter: false
weight: 3
--- 

**For instructor led workshops please go to the workshop slides before proceeding with this lab: https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-management/#1**

In this lab, you will set up a CloudBees Feature Management account and use it to manage feature flags through remote configurations created in the CloudBees Feature Management dashboard.

### Create a CloudBees Feature Management Account

1. Open the CloudBees Feature Management [sign-up form](https://rollout.io/sign-up/) in a _new tab_ within your browser. If you already have a CloudBees Feature Management account the [click here to login to your account](https://app.rollout.io/login) and proceed to step 3.
2. Fill out the form with your name, email, and a created password. After confirming your password, check the box agreeing to CloudBees Feature Management' Terms of Service (which can be viewed [here](https://docs.cloudbees.com/docs/cloudbees-common/latest/subscription-agreement/)), and click **Sign Up**.
3. After you have successfully created an account, the CloudBees Feature Management dashboard will be displayed. Create a new application by clicking the blue panel in the top left corner of the screen. ![New Application](images/new-application.png?width=70pc)
4. After creating a new application in the dashboard, click the **App Settings** panel seen on the left hand menu. From the resulting page, select the **Environments** tab.
5. Click **Add New Environment** and name it **Development**. ![Create Development Environment](images/create-dev-env.png?width=70pc)
6. Next, click **Generate Key**.
7. **Close** the subsequent **Development Key** pop-up window so that both _Production_ and _Development_ keys are displayed. Leave this CloudBees Feature Management dashboard tab open in the browser. Both keys will be referenced later in this lab.

### API Key Environment Variable

The CloudBees CI Pipeline that will automatically build and deploy your `mircroblog-frontend` application uses a different CloudBees Feature Management environment key depending on which branch is deployed. Later in the workshop, we'll learn how these separate environment keys can be used to apply the multi-environment view of the CloudBees Feature Management dashboard. This will allow a flag to have a separate and unique *Production* configuration from its *Development* environment counterpart. However, in this lab we will update a GitHub pull request between the `development` and `main` branch of your  `mircroblog-frontend` repository.

1. Open your browser to the Github Organization you created for the workshop and navigate to the `microblog-frontend` repository.
2. Change the branch from `main` to `development`. After changing branches to the `development` branch, click on the `.env.production` file.
3. Click the pencil icon to edit the file - again, making sure you are on the `development` branch. ![GitHub edit file](images/pencilEdit.png?width=70pc)
4. Switch back to the CloudBees Feature Management dashboard. Copy the environment **Key** for the **Production** environment by clicking on the **Key** value for that environment. ![Copy key](images/copy-key.png?width=70pc)
5. Navigate back to the Github tab with the `.env.production` file being edited.
6. Replace `YOUR_PRODUCTION_KEY_HERE` on **Line 1** by pasting your unique Production **Key** value that you copied.
7. At the bottom of the page, select **Commit directly to the `development` branch** radio button. Then click the **Commit changes** button.
8. Navigate back to the root directory of the `microblog-frontend` repository (`development` branch). Click the `.env.development` file. And then select the pencil icon on the following page to make an edit to the file.
9. Now, copy your **Development** environment **Key** value from the CloudBees Feature Management dashboard and then replace `YOUR_DEVELOPMENT_KEY_HERE` in the `.env.development` file with that value. Make sure you copied and replaced the value for the ***Development*** environment and the `.env.development` file on the `development` branch.
10. Select the **Commit the file directly to the `development` branch** radio button, and then click **Commit changes**.
![Commit changes](images/commitChanges.png?width=50pc)

### Create Feature Flags with CloudBees Feature Management

The `flags.js` file imports the relevant CloudBees Feature Management SDK and defines the feature flags (with the flags' `DEFAULT` values) that an application will use. The file contains a call to the `setup` function that establishes a connection to the CloudBees Feature Management dashboard. The CloudBees Feature Management dashboard interface will allow for remote configuration in future labs.

1. In Github, navigate to the root level of the `microblog-frontend` repository (ensure you are working on the `development` branch).
2. Change directories and select the `flags.js` file (`src\utils\flags.js`) by first clicking the `src` folder from root view, followed by the `utils` folder, and finally select the subsequent `flags.js` file. ![Open flags.js](images/open-flags-js.png?width=60pc)
3. We will later add a component to the **Posts view** of the microblog application that will be gated by this new `title` feature flag we are about to add. Click the pencil to edit the file.  ![Edit flags.js](images/editflags-js.png?width=60pc)
4. Next, define the `title` flag and its default value (`false`) by adding the following within the `const Flag` section after **Line 4**:
```javascript
export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}
```

{{%expand "expand for complete updated flag.js file" %}}

```javascript
import Rox from 'rox-browser'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}

async function initCloudBees () {
  const options = {
  }

  Rox.register('default', Flags)
  await Rox.setup(process.env.VUE_APP_CLOUDBEES_KEY, options)
}

initCloudBees().then(function () {
  console.log('Done loading CloudBees Feature Management')
})
```
{{% /expand%}}

5. Commit the changes by adding a comment (e.g. "added title flag"), select the **Commit directly to the `development` branch** radio button, and then click **Commit changes**.


### See the Deployed Microblog Website

Once you committed the `flags.js` file a job will be triggered on a CloudBees CI ***managed controller*** that was provisioned for you for this workshop. That job will build and deploy your `microblog-frontend` application.

1. Navigate to the `microblog-frontend` repository.
2. Click on the **Pull requests** tab and the click on the **New Feature** pull request. ![New Feature PR](new-feature-pr.png?width=50pc)
3. On the **Open** pull requests screen you will see that there is a CloudBees CI build in process. ![Build in progress](images/building.png?width=50pc)
   - **IMPORTANT:** If your build ends with any errors then click on the **Details** link for the **error** check. ![Error](images/pr-error.png?width=50pc)
   - In the **Checks** view, with the **error** check selected, expand the **Log** under **DETAILS**. ![Error log](images/error-log.png?width=50pc)
   - Scroll down and, in this example, you will see that we forgot a comma in the `/src/utils/flags.js` file. ![Missing comma](images/missing-comma.png?width=50pc)
   - To fix the syntax error click on the **Files changed** tab, scroll down to the `flags.js` file, then click on the 3 dots to bring up the menu to access and click the **Edit file** link. ![Edit file](images/edit-file.png?width=50pc)
   - Fix the error, in this case adding a comma after `sidebar: new Rox.Flag(false)`, and then click the **Commit changes** button. ![Fix error](images/fix-error.png?width=50pc)
   - Navigate back to the **Checks** view and you will see a new build was triggered. ![Waiting for checks](images/checks-waiting.png?width=50pc)
   - Once the build completes you should see that your error is fixed. 
4. Once the build has finished successfully you will see the branch deployed to the *staging* environment, click on the **View deployment** button. ![Deployment activity](images/view-deployment.png?width=50pc)
5. This is the microblog frontend application.
![Deployed site](images/microblogWebsite.png?width=50pc)


### Checking Communication with CloudBees Feature Management

1. In your browser, switch to CloudBees Feature Management dashboard.
2. On the left-hand side of the dashboard, select the **Audit Logs** view.
3. You should see both the `title` and `sidebar` flags have been added to the `default` namespace and communicated from the `development`code. This means they are available for remote configuration in the dashboard! There are also some default properties that have been added, but we'll add more in a future lab. ![Audit logs](images/auditLogs.png?width=70pc)
4. Finally, click on **Flags overview** in the left menu and you will see the two flags from your `flag.js` file, and an outline of their configurations (though we have none yet) defined across all environments. ![Flags](images/dashboard-flags.png?width=70pc)

### Setup Completed!
Congratulations! You have finished the setup of the CloudBees Feature Management Workshop.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-management/#gating-code-title">return to the workshop slides</a>**
