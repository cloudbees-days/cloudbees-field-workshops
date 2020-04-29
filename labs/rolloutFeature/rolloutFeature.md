# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Gating Code with a CloudBees Feature Flag

### Adding a Sidebar to the Microblog
1. In Github, navigate to the root directory of the microblog-frontend repository.
2. Click `Branch: initRollout`
3. Type `newSidebar` then click "Create branch: newSidebar from initRollout" to finish creating a new branch.
4. Ensure you are within the newSidebar branch, then navigate to the `src/views/Posts.vue` file by clicking the `src`, `views`, and `Posts.vue` links, consecutively.
<p><img src="images/srcViewsPost.gif" />

5. Click the pencil icon to edit the file.
TODO: ADD RED CALLOUT BOX TO BELOW PNG
<p><img src="images/PostsVuePencil.png" />

6. In order to reference our previously created feature flag, we must import the `Flags` constant from the `flags.js` file. On line 28, add the following statement:
```javascript
import { Flags } from '../utils/flags'
```
7. Now, we need to create a function called `show_sidebar` that will return  the boolean value associated with our `sidebar` feature flag. That return value is accessed by `Flags.sidebar.isEnabled()`. To declare the `show_sidebar` function and relate it to the value of our previously created feature flag, add it to the end of the `data: function ()` block starting at line 34. Don't forget to add a comma ater the `errors` function, as seen in in the finished snippet below:
```javascript
data: function () {
  return {
    message: '',
    posts: [],
    users: [],
    errors: [],
    show_sidebar: Flags.sidebar.isEnabled()
  }
},
```
8. Now we're going to add a sidebar component that is gated behind our `sidebar` feature flag. In line 6, make the following edits:
```html
 <h1 class="title">Posts <span v-if="show_sidebar"> - Show sidebar!</span></h1>
```
9. The new sidebar should only be shown if the `show_sidebar` function (or the `Flags.sidebar.isEnabled` call) returns `true`. To implement the new sidebar functionality gated behind this if logic, add a new line after lines 7 and insert the following code:
```html
  <div class="columns" v-if="show_sidebar">
    <div class="box column is-three-quarters">
      <div class="box">
        <b-field label="What's going on today?"
          class="is-marginless"
        >
          <b-input v-model="message" maxlength="140" type="textarea"/>
        </b-field>
          <b-button type="is-dark" @click="addPost">Submit</b-button>
      </div>
      <hr class="hr">
      <Post v-for="post in posts" :key="post.id" :post="post"/>
    </div>
    <div class="box column">
      <h3 class="is-size-4 has-text-weight-bold">Users list</h3>
      <ul>
        <li v-for="user in users" :key="user.url">
          <a :href="user.url">{{user.username}}</a>
        </li>
      </ul>
    </div>
  </div>
```
10. Now, **either** the sidebar **or** the existing "What's going on today" component should be displayed, **but not both**. This means we need to gate the existing component behind an `else` statement. We can accomplish this with one `v-else` edit to remaining of the html:
```html
  <div class="box" v-else>
    <div class="box">
      <b-field label="What's going on today?"
                   class="is-marginless"
      >
        <b-input v-model="message" maxlength="140" type="textarea"/>
      </b-field>
      <b-button type="is-dark" @click="addPost">Submit</b-button>
      </div>
      <hr class="hr">
        <Post v-for="post in posts" :key="post.id" :post="post"/>
    </div>
  </div>
```
11. Create a commit message and select "Commit directly to the `newSidebar` branch" radio button.
12. Complete this lab by clicking "Commit new file."


* TODO:
MAKE SURE PIPELINE RUNS WITH NEW ROLLOUT FEATURE FLAGS AND COMPONENT
CHECK NEW MICROBLOG TO ENSURE SIDEBAR DOES NOT SHOW UP

* LATER
* ROX DEVS for LOCAL DEVELOPMENT
* SHOULD WE CHANGE sidebar flag value to default to true, so that when changes are made, any errors are readily apparent?