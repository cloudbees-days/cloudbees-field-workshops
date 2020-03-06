In this lab, we will gate features in our front-end code using Rollout's feature flag library.

Then, customized busienss logic can be set in the Rollout dashboard to trigger values for the flags.

src/views/Posts.vue: 

```html
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
```

Add the following below the import:
```javascript
import { Flags } from '../utils/flags'
```

src/views/components/Nav.vue

Insert the following below line 14:
```html
<b-navbar-item v-if="isDev">
        <span @click="rolloutOverride">DEV</span>
</b-navbar-item>
```

Insert the following below import:
```javascript
import Rox from 'rox-browser'

export default {
  methods: {
    logout () {
      this.$store.dispatch('logout')
    },
    rolloutOverride: () => {
      Rox.showOverrides()
    }
  },
  data () {
    return {
      isDev: process.env.NODE_ENV === 'development'
    }
  },
  created () {
    if (this.$store.state.isLoggedIn) {
      this.$store.dispatch('grabUser')
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn'
    ]),
    ...mapState([
      'user'
    ])
  }
}
```
