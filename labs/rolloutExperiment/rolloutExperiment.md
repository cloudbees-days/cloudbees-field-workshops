## Control the Value of a Feature Flag
1. Navigate to the Rollout Dashboard.
2. On the left-hand side of the screen, click Production, and then Experiments from the expanded list. Then, click "Create a New Experiment" button.
<p><img src="images/ProdCreateNewExp.png" />

3. In the pop-up, ensure the "default.sidebar" flag is selected from the drop-down menu before clicking "Set Audience."
<p><img src="images/CreateNewSidebarExp.png" />

4. Right now, the sidebar is not shown because the value of the feature flag is set to `False` by default. Click on the drop-down menu next to then and select `True`. Finally, to update the `sidebar` flag's boolean value, click "Update Audience" button.
<p><img src="images/UpdateAudience.gif" />
	
5. Navigate back to the micro-blog and verify that the sidebar is now visible.
6. Congratulations! You have completed this lab and are ready.

TODO:
* Add next lab link for step 6
* Add image for micro-blog with sidebar shown to step 5