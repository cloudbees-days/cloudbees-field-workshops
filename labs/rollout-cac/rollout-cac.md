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
1. In the Rollout dashboard, disable the side experiment in Development environment by toggling `Active` to `Killed`.

<p><img src="images/sidebar_killed.png" />

2. In GitHub, go look at your `experiments` folder, click on `WHATS_THE_NAME_OF_THIS.yml` and note the structure.
3. Then, switch from `master` branch to our automatically created `Development` branch and note the differences in your `experiments` folder, especially the addition of `default.sidebar.yml` with `enabled: false` on line 5.
4. Within the Github code editor, modify `default.sidebar.yml` by deleting the line `enabled: false` and commit to `Development` branch. Your YAML should closely resemble this:

```YAML
# This file was edited by rollout.io
# URL: https://app.rollout.io/ex/<YOUR_EXPERIMENT_URL>
type: experiment
name: sidebar
flag: default.sidebar
conditions:
  - group:
      name: LoggedInUsers
    value: true
value: false
```

5. In Rollout, notice that your default.sidebar experiment is now reactivated on the Development environment.

Now that you are satisfied with the experiment in your Development environment, you want to include this experiment in your Production environment.

6. In Github, merge `Development` to `master` branch with an appropriate commit message.
7. In Rollout, note the sidebar experiment is now added to the Production environment.

*Final screenshot of Prod env with `WHATS_THE_NAME_OF_THIS.yml` and `default.sidebar.yml`*

You have successfully completed the introductory Rollout workshop!

Please return to the [main page](../../README.md#workshop-labs) for other workshops and labs.
