# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Gating Code with a CloudBees Feature Flag

In this lab, you will create a sidebar component and add it to the microblog. Since this component is *experimental*, we can gate it behind our previosuly created feature flag (`sidebar: new Rox.flag(false)`) that will initially hide it. Then using Rollout's dashboard, we will remotely configure the value of the flag, and will thus enable the sidebar.

### Adding a Sidebar to the Microblog

1. In Github, navigate to the root directory of the microblog-frontend repository.
2. Click `Branch: initRollout`
3. Type `newSidebar` then click **Create branch: newSidebar from initRollout** to finish creating a new branch.
4. Ensure you are within the newSidebar branch, then navigate to the `src/views/Posts.vue` file.

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
8. Now we're going to add a text component that will only be displayed when `show_sidebar` is evaluated to `true`. In line 6, make the following edits:
```html
 <h1 class="title">Posts <span v-if="show_sidebar"> - Show sidebar!</span></h1>
```
9. The new sidebar should only be shown if the `show_sidebar` function (or the `Flags.sidebar.isEnabled` call) returns `true`. To implement the new sidebar functionality gated behind this if logic, add a new line after line 7 and insert the following code:
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
11. The final The final `Post.vue` should be
<details><summary>this:</summary>

```html
<template>
  <div class="container">
    <hr class="hr is-invisible">
    <div class="box">

      <h1 class="title">Posts <span v-if="show_sidebar"> - Show sidebar!</span></h1>
      <hr class="hr">
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
  </div>
</template>

<script>
import Post from '@/components/Post.vue'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'
import { Flags } from '../utils/flags'

export default {
  name: 'posts',
  components: {
    Post
  },
  data: function () {
    return {
      message: '',
      posts: [],
      users: [],
      errors: [],
      show_sidebar: Flags.sidebar.isEnabled()
    }
  },
  created () {
    this.getPosts()
    this.getUsers()
  },
  computed: {
    ...mapGetters([
      'isLoggedIn'
    ]),
    ...mapState([
      'user'
    ])
  },
  methods: {
    getPosts: function () {
      axios.get(`${process.env.VUE_APP_BASE_API_URL}/posts/`)
        .then(response => {
          this.posts = response.data
        })
        .catch(error => {
          this.errors.push(error)
        })
    },
    getUsers: function () {
      axios.get(`${process.env.VUE_APP_BASE_API_URL}/users/`)
        .then(response => {
          this.users = response.data
        })
        .catch(error => {
          this.errors.push(error)
        })
    },
    addPost: function () {
      if (this.message.length > 1 && this.message.length <= 140) {
        axios.post(`${process.env.VUE_APP_BASE_API_URL}/posts/`, {
          user: this.user.url,
          message: this.message
        }, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
          }
        })
          .then(() => {
            this.getPosts()
            this.message = ''
          })
          .catch(e => {
            this.errors.push(e)
          })
      }
    }
  }
}
</script>
```
</details>

12. Create a commit message and select **Commit directly to the `newSidebar` branch** radio button.
13. Click **Commit new file**
14. **For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1)**

Otherwise, you may proceed to the next lab: [**Control the Value of a Flag with CloudBees Rollout**](../rolloutExperiment/rolloutExperiment.md) or choose another lab on the [main page](../../README.md#workshop-labs).
