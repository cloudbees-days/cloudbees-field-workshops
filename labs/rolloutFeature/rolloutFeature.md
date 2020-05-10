# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Gating Code with a CloudBees Rollout Flag

## Using a Feature Flag in Code
In this lab, you will gate a component behind the `title` feature flag, defined in the previous lab. Later, using Rollout's dashboard, we will remotely configure the value of the flag, to either expose or hide this title element at will.

### Adding a Title to the Microblog Post

1. In Github, navigate to the root directory of the microblog-frontend repository. Ensure that you are on the `development` branch.
2. Navigate to the `Posts.vue` file (`src/views/Posts.vue`) by clicking the `src` folder, `views` folder, followed by `Posts.vue`, consecutively. 

<p><img src="images/srcViewsPost.gif" />

3. Click the pencil icon to edit the file.

<p><img src="images/PostsVuePencil.png" />

4. In order to use the feature flags created in our `flags.js` file, we included the `import` statement on **Line 50**. Now, we'll create a function called `show_title` that will return the `boolean` value from `Flags.title.isEnabled()`.
To add an additional function, first insert a comma `,` at the end of the `show_sidebar` definition on **Line 63**. Then add a new line after the comma, and define the `show_title` function as seen in the `data` segment below: 
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

5. Now we're going to add a new title component gated behind a feature flag. This will allow the element to only be displayed when the `show_title` function is evaluated to `true`. Insert the following code on **Line 5**.:
```html
 <h1 class="title">Posts <span v-if="show_title"> - Show New Title!</span></h1>
```
6. Expand the following to review:
<details><summary>Updated <code>Post.vue</code></summary>

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
8. Click **Commit changes**.

### Adding the Configuration Fetched Handler

The Configuration Fetched Handler provides a mechanism to alert when the Rollout SDK has loaded updated configuration from local storage or via an asynchronous network call. It allows us to control what happens whenever a new configuration is fetched. In order for changes to be applied, an action has to take place, like a page refresh.
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
