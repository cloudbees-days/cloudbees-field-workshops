## User Targeting in CloudBees Rollout

The goal of this lab is to use a property from our code, and allow users in the Rollout dashboard to create a ruleset such that the `sidebar` element is only visible to users that have successfully logged in.

1. First we need to make sure the `isLoggedIn` function from the `store` available to the `flag.js` file. Navigate to the microblog-frontend repository in Github. In the `src\utils\flags.js` file, add the following import line:
```javascript
import { store } from '../store'
```

2. In order to allow the Rollout dashboard to use the `isLoggedIn` function to target specific users in a configuration, we need pass the property to the dashboard in a similar manner that we used `Rox.register` for the sidebar flag. Before the `Rox.register` line, add the following line:
```javascript
Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn)
```

3. The final `flags.js` should be:

** ADD FINAL FLAGS.JS 

4. Create a commit message (e.g. added setCustomBooleanProperty) and select "Commit directly to the `master` branch" radio button.

5. In the Rollout dashboard, click the Target Groups option from the navigation panel on the left.

6. On the subsequent page, click Create New Target Group.

7. Now that the property is made visible to the Rollout dashboard, we can use this to define a segmented user group. Fill the pop-up window with the appropriate information:
* Name: LoggedInUsers
* Condition
** Property: isLoggedIn
** Value: Is True

** Insert image of finished pop up here

8. Click Create Group. Then open the Production drop-down menu on the left and select Experiments. Click the `sidebar` experiment.

9. We will now modify our `sidebar` experiment to incoporate the following logic:
* IF (a user is logged in), THEN display `sidebar` by setting the flag to `true`
* ELSE set the flag to `false` that will hide the `sidebar` element.

10. Click Add New Condition. This should create a new condition next to the `if` statement. In the drop down menu (currently displaying All Users), select `Target Group`, then `matches any of`, and finally `LoggedInUsers`. Since we want the `sidebar` to show for this target group, select `true` for the condition after the `then` statement.

11. Ensure the `else` statement is set to `false` and the finished experiment configuration should be the same as the below iamge:

** Insert image

12. Click Update Audience

13. Navigate to the microblog to test the configuration logic. Log in and ensure the sidebar is visible. Afterward log out to check the latter half of the configuration logic as the sidebar should be hidden.

14. Next Lab