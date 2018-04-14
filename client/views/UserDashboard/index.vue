<template>
  <div class="container">
  <div class="user-container">
    <div class="user-dashboard">
      <div class="description-user-dashboard">
        <p class="description-user-name">{{ user.name }}</p>      
        <p class="description-user-id">Your id #{{ user.id }}</p>
        <p class="description-user-winrate">WINRATE {{ user.winRate }}</p>
        <p class="description-user-balance">BALANCE {{ user.balance }} ACEY</p>
      </div>
       <img src="userpic.png" alt="" class="userpic-user-dashboard">
    </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'UserDashboard',
    components: {},
    computed: {
      user() {
        console.log(this.$store.state.user)
        return this.$store.state.user
      },
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
