# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Gating Code with a CloudBees Feature Flag

In this lab, you will gate a component behind the already defined `title` feature flag. Later, using Rollout's dashboard, we will remotely configure the value of the flag, to either expose or hide this gated element at will.

### Adding a Posts Title to the Microblog

1. In Github, navigate to the root directory of your fork of the **microblog-frontend** repository. Ensure that you are within the `development` branch.
2. Navigate to the `Posts.vue` file by navigating to `src/views/Posts.vue`. 

<p><img src="images/srcViewsPost.gif" />

3. Click the pencil icon to edit the file.

<p><img src="images/PostsVuePencil.png" />

4. In order to reference our previously created feature flags, we use the `import` statement on **Line 50**. We need to create a function called `show_title` that will return  the boolean value returned from checking `Flags.title.isEnabled()`. To declare the `show_title` function and relate it to the value of our previously created feature flag, add it after the `show_sidebar` function after **Line 63**. The `show_title` function should be added to the `data` segment as seen below: 
```javascript
data: function () {
  return {
    message: '',
    posts: [],
    users: [],
    errors: [],
    show_sidebar: Flags.sidebar.isEnabled(),
    show_title: Flags.title.isEnabled()
  }
},
```

5. Now we're going to add a title component that will only be displayed when `show_title` is evaluated to `true`. In line 5, add the following edits:
```html
 <h1 class="title">Posts <span v-if="show_title"> - Show New Title!</span></h1>
```
6. The final The final `Post.vue` should be
<details><summary>this:</summary>

```html
<template>
  <div class="container">
    <hr class="hr is-invisible">
    <div class="box">

      <h1 class="title">Posts <span v-if="show_title"> - Show New Title!</span></h1>
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
      show_sidebar: Flags.sidebar.isEnabled(),
      show_title: Flags.title.isEnabled()
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

7. Create a commit message (e.g. "Added title component") and select **Commit directly to the `development` branch** radio button.
8. Click **Commit changes**

### Adding the Configuration Fetched Handler

The Configuration Fetched Handler allows us to control what happens whenever when a new configuration is fetched. In order for changes to be applied, an action has to take place, like a page refresh.
1. In Github, navigate to the root directory of the microblog-frontend repository.
2. Ensure you are on the `development` branch. Then, open the `flags.js` file (`src/utils/flag.js`).
3. Insert the `configurationFetchedHandler` constant **and** ensure it is called in `options` as seen in the `flag.js` file below:

<details><summary><code>flags.js</code></summary>

```javascript
import Rox from 'rox-browser'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
};

export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
};

const options = {
  configurationFetchedHandler: configurationFetchedHandler
};

Rox.register('default', Flags);
Rox.setupRox.setup(process.env.VUE_APP_ROLLOUT_KEY, options);
  
```
</details>

4. Create a commit message (e.g. "Inserted configurationFetchedHandler) and select **Commit directly to the `development` branch** radio button.
5. Click **Commit changes**.

### Checking

1. Navigate to CloudBees Core.
2. Navigate to `microblog-frontend`
3. Open Blue Ocean
4. Click `development` branch to see the pipeline.
5. Click deploy, and the last shell script. Open the URL 

* **For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1)**

Otherwise, you may proceed to the next lab: [**Control the Value of a Flag with CloudBees Rollout**](../rolloutExperiment/rolloutExperiment.md) or choose another lab on the [main page](../../README.md#workshop-labs).
