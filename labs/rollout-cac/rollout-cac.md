# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> CloudBees Rollout - Feature Flags and GitOps

### Connecting to GitHub Cloud
1. Create an empty repository in your GitHub organization named "rollout-configuration-as-code"
2. Connect the Rollout app into the Github repository
  1. Go to **App Settings > Integrations tab** (from the left Panel)
  2. Click the **Connect** button
  <p><img src="images/app-integrations.png" />
3. In GitHub, select to integrate the Rollout GitHub app with your created repository.
<p><img src="images/github-app.png" />
4. After clicking **Install** you will be redirected back to the CloudBees Rollout dashboard to select your app and the repository
<p><img src="images/github-rollout-confirmation.png" />
5. Click connect and you are done

### Using CasC and GitOps
1. Copy sidebar experiment from Development environment into Production.
2. Modify the experiment in Development environment.
3. In GitHub, switch from `master` branch to our automatically created `Development` branch. Go look at your `experiments` folder, click on `default.sidebar.yml` and note the changes.
4. Within the Github code editor, modify default flag value and commit to `Development` branch.
5. In Rollout, notice that your default.sidebar experiment default value is updated for the Development environment.
6. In Github, merge `Development` and `Master` branches.
7. In Rollout, note the change to the Production environment.
