---
title: "Gating Code with Feature Flags"
chapter: false
weight: 1
--- 

## Using a Feature Flag with CloudBees Feature Management
In this lab, you will *gate* a component behind the `title` feature flag defined in the previous lab by using CloudBees Feature Management's dashboard. We will then remotely configure the value of the flag to control whether the title element is visible or hidden.

### Adding a Title to the Microblog Post

1. In Github, navigate to the root directory of the `microblog-frontend` repository. Ensure that you are on the `development` branch.
2. Navigate to the `Posts.vue` file (`src/views/Posts.vue`) by clicking the `src` folder, `views` folder, followed by `Posts.vue`, consecutively. ![Add title flag to Posts.vue](images/edit-postsvue-add-title-flag.png?width=50pc)
3. Click on the pencil icon to edit the file.
4. This file is already using the `sidebar` flag and its state is checked using the `show_sidebar` function that gates the component as seen on **Line 7**. To use this and the `title` feature flags created in the `flags.js` file, we've included the `import` statement on **Line 50**. Now, we'll create a function called `show_title` that will return the `boolean` value from `Flags.title.isEnabled()`. To add this functionality, first insert a comma `,` at the end of the `show_sidebar` definition on **Line 63**. Then, add a new line after the comma, and define the `show_title` to check the `title` flag state using `Flags.title.isEnabled()` as seen in the `data` segment below:
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

5. Now we're going to add a new title component gated behind our `title` feature flag. This will allow the element to _only_ be displayed when `Flags.title.isEnabled()` is `true`. Update the code on **Line 5** to gate the *Show New Title!* text behind the `show_title` flag:
```html
 <h1 class="title">Posts <span v-if="show_title"> - Show New Title!</span></h1>
```

{{%expand "expand for complete updated Post.vue file" %}}
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
{{% /expand%}}

7. Create a commit message (e.g. "Gating new title feature") and select the **Commit directly to the `development` branch** radio button. Click **Commit changes**.

### Adding the Configuration Fetched Handler

The **Configurationed Fetch Handler** provides a mechanism to alert the CloudBees Feature Management SDK in your application when an updated configuration, from local storage or via an asynchronous network call, has loaded. It allows us to control what happens when a new configuration is fetched, and can be used for troubleshooting by logging the `fetchedResults`. For the changes in a client-side defined feature flag, an action has to take place (like a page refresh) in order for the new configuration to be applied.

1. In Github, navigate to the root directory of the `microblog-frontend` repository on the `development` branch.
2. Open the `flags.js` file (navigating to `src/utils/flags.js`), and select the pencil icon to edit the file.
3. We will trigger a page refresh when a **new** configuration is retrieved **from the network**. We can also assist in any troubleshooting by adding `console.log` statements. Define the `configurationFetchedHandler` constant with its boolean logic cases and then add it to the `options` constant used to configure the `Rox.setup` call as seen in the `flags.js` file below:

```javascript
import Rox from 'rox-browser'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}

export const configurationFetchedHandler = fetcherResults => {
  console.log('The configuration status is: ' + fetcherResults.fetcherStatus)
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  } else if (fetcherResults.fetcherStatus === 'ERROR_FETCH_FAILED') {
    console.log('Error occured! Details are: ' + fetcherResults.errorDetails)
  }
}

async function initCloudBees () {
  const options = {
    configurationFetchedHandler: configurationFetchedHandler
  }

  Rox.register('default', Flags)
  await Rox.setup(process.env.VUE_APP_CLOUDBEES_KEY, options)
}

initCloudBees().then(function () {
  console.log('Done loading CloudBees Feature Management')
})
```
4. Enter a commit message (e.g. "Inserted configurationFetchedHandler"), select **Commit directly to the `development` branch** radio button and click **Commit changes**.

### Checking Microblog Website

1. Navigate back to the **New Feature** pull request and once the build has finished successfully you will see the branch deployed to the *preview* environment, click on the **View deployment** button.
2. On the microblog website, open the console from your browser's developer tools and then refresh the page. Check the log to view the messages from the `configurationFetchedHandler`.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-management/#18">return to the workshop slides</a>**
