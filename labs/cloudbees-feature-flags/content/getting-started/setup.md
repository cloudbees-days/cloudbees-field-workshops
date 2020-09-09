---
title: "CloudBees Feature Flags Setup"
chapter: false
weight: 3
--- 

**For instructor led workshops please go to the workshop slides before proceeding with this lab: https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-flags/#1**

In this lab, you will set up a CloudBees Feature Flags account and use it to manage feature flags through remote configurations created in the CloudBees Feature Flags dashboard.

### Create a CloudBees Feature Flags Account

1. Open the CloudBees Feature Flags [sign-up form](https://app.rollout.io/signup) in a _new tab_ within your browser.
2. Fill out the form with your name, email, and a created password. After confirming your password,  check the box agreeing to CloudBees Feature Flags' Terms of Service (which can be viewed [here](https://docs.cloudbees.com/docs/cloudbees-common/latest/subscription-agreement/)), and click **Sign Up**.
3. After you have successfully created an account, the CloudBees Feature Flags dashboard will be displayed. On the far left side of the dashboard, click the **App Settings** panel. From the resulting page, select the **Environments** tab.
4. Click **Add New Environment** and name it **Development**. Then click **Generate Key**.
5. **Close** the subsequent **Development Key** pop-up window so that both _Production_ and _Development_ keys are displayed. Leave this CloudBees Feature Flags dashboard tab open in the browser. Both keys will be referenced later in this lab.
![Environment Key](images/RolloutEnvKey.png?width=50pc)

### Environment Variable

The CloudBees CI Pipeline, that will automatically build and deploy your `mircroblog-frontend` application, uses a different CloudBees Feature Flags environment key depending on which branch is deployed. Later in the workshop, we'll learn how these separate environment keys can be leveraged to apply the multi-environment view of the CloudBees Feature Flags dashboard. This will allow a flag to have a particular *Production* configuration, while using a completely different ruleset for the code connected to the *Development* environment.

1. Switch tabs to your Github organization created for the workshop and navigate to your copy of the `microblog-frontend` repository.
2. Change the branch from `main` to `development`. All work, until some components of Lab 5, will take place on the `development` branch. After changing branches, click on the `.env.production` file.
3. Click the pencil icon to edit the file - again, making sure you are on the `development` branch.
![GitHub edit file](images/pencilEdit.png?width=50pc)
1. Switch back to your CloudBees Feature Flags tab with the dashboard in view. Copy the `<ROLLOUT_ENV_KEY>` associated with the _Production_ environment. Navigate back to the Github tab with the `.env.production` file being edited.
2. Replace `YOUR_PRODUCTION_KEY_HERE` on **Line 1** by pasting your unique Production `<ROLLOUT_ENV_KEY>`.
3. At the bottom of the page, select **Commit directly to the `development` branch** radio button. Then click the **Commit changes** button.
4. Navigate back to the root directory of the microblog-frontend repository (`development` branch). Click the `.env.development` file. And then select the pencil icon on the following page to make an edit to the file.
5. Now, copy your _Development_ `<ROLLOUT_ENV_KEY>` from the CloudBees Feature Flags dashboard. Then replace `YOUR_DEVELOPMENT_KEY_HERE` in the `.env.development` file by pasting the unique Development CloudBees Feature Flags key.
6. Select the **Commit the file directly to the `development` branch** radio button, and then click **Commit changes**.
![Commit changes](images/commitChanges.png?width=50pc)

### Create Feature Flags with CloudBees Feature Flags

The `flags.js` file imports the relevant CloudBees Feature Flags SDK and defines the feature flags (with its `DEFAULT` values) that an application will use. The file contains a call to the `setup` function that establishes a connection to the CloudBees Feature Flags dashboard. The CloudBees Feature Flags dashboard interface will allow for remote configuration in future labs.

1. In Github, navigate to the root level of the `microblog-frontend` repository (Ensure you are working on the `development` branch).
2. Change directories and select the `flags.js` file (`src\utils\flags.js`) by first clicking the `src` folder from root view, followed by the `utils` folder, and finally select the subsequent `flags.js` file.
3. We will later add a component to the **Posts view** of the microblog application that is gated by a `title` feature flag. Click the pencil to edit the file. Define the `title` flag and its default value (`false`) by adding the following within the `const Flag` section after **Line 4**:
```javascript
export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}
```

**After this edit, the `flags.js` should be**
<details><summary>this:</summary>

```javascript
import Rox from 'rox-browser'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}

async function initRollout () {
  const options = {
  }

  Rox.register('default', Flags)
  await Rox.setup(process.env.VUE_APP_ROLLOUT_KEY, options)
}

initRollout().then(function () {
  console.log('Done loading Rollout')
})
```
</details>

4. Commit the changes by adding a comment (e.g. "added title flag"), and select the **Commit directly to the `development` branch** radio button. And then click **Commit changes**.

### Adding .vuejs Marker File

1. Navigate to the root level of the `microblog-frontend` repository on the `development` branch. Click the **Create a new file** button.
2. Name the file `.vuejs` (don't forget the leading period).
3. Leave the file blank, commit the file by adding a comment (e.g. "New .vuejs file"). Ensure the **Commit directly to the `development` branch** radio button is enabled. Then select **Commit new file**.

### See Deployed Microblog Website

Once you commit the `.vuejs` **marker file** a job will be triggered on the CloudBees CI ***managed controller*** that was provisioned for you for this workshop. That job will build and deploy the `microblog-frontend` repository.

1. Refresh the GitHub page for your `microblog-frontend` repository and you will eventually see a new **Environments** section on the right side of the page. Click on the **staging** link. ![Environments staging link](images/gitHubEnvironments.png?width=50pc)
2. On the **Deployments / Activity log** page, once the the **staging** environment is **Active**, click on the **View deployment** button. ![Deployment activity](images/deploymentsActivity.png?width=50pc)
3. Open the URL in a new tab (that follows the format: `http://development.YOUR_ORG_NAME-microblog-frontend.workshop.labs.cb-sa.io`). This is the microblog!
![Deployed site](images/microblogWebsite.png?width=50pc)

### Checking Communication with CloudBees Feature Flags

1. Switch tabs to CloudBees Feature Flags.
2. On the left-hand side of the dashboard, click the **Development** panel and then select the **Audit Logs** view from the drop down options.
3. You should see both the `default.title` and the `default.sidebar` flags added from the code are available for remote configuration in the dashboard! There are also some default properties that have been added, but we'll add more to use in a future lab. ![Audit logs](images/auditLogs.png?width=50pc)

### Lab 1 Completed!
Congratulations! You have finished Lab 1 of the CloudBees Feature Flags Workshop.

**For instructor led workshops please return to the workshop slides: https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-flags/#14.**
