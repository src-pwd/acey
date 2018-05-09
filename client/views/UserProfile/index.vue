<template>
  <div class="container">
    <div class="user-container">
        <div class="user-block-left-part">
          <div>act rate{{userInfo.activity_rate}}</div>
          <div>bets{{userInfo.bets}}</div>
          <div>events{{userInfo.events}}</div>
          <div>info{{userInfo.info}}</div>
          <div>rate{{userInfo.rate}}</div>
          <div>sum{{userInfo.sum}}</div>
        </div>
        <div class="user-block-right-part">
          <img class="userpart-userpic" src="kekes.svg" alt="">
        </div>
      
    </div>
    <div class="button-container">
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'UserProfile',
    components: {},
    mounted() {
      console.log(this.imgSource)
    },
    computed: {
      isLogged() {
        return this.$store.state.auth.loggedIn
      },
      userInfo() {
        return this.$store.state.user.details
      }
  
    },
    watch: {
      isLogged() {
        if (this.isLogged == false)
          this.$router.push('/')
      }
    },
    methods: {
      logout() {
        this.$store.commit("removeToken")
        this.$store.commit("loggingOut")
      }
  
    }
  }
</script>

<style lang="scss">
  .user-container {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-flow: row;
    margin-top: 80px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-flow: row;
    justify-content: center;
  }
</style>
