<template>
  <div class="container">
  <div class="user-container">
    <div class="user-dashboard">
    </div>
    <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'UserProfile',
    components: {},
    computed: {
       isLogged() {
        return this.$store.state.auth.loggedIn
      }
      
    },
    watch: {
    isLogged () {
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
  .user-dashboard {
    display: flex;
    flex-flow: row;
  }
  
  .description-user-dashboard {
    width: 50%;
  }
  .user-container {
    width: 700px;
    margin-top: 100px;
    margin-left:auto;
    margin-right: auto;
  }
  p.description-user-name {
    font-size: 40px;
    color: white;
}

.description-user-dashboard {
  & > p {
    font-size: 20px;
    color: white;
  }
}

.userpic-user-dashboard {
  border-radius: 150px;
  margin-left: 200px;
}

.description-user-balance {
  color: orange !important;
}
</style>
