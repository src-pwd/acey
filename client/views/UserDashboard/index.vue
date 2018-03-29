<template>
  <div>
    <h1>User Dashboard </h1>
    <div class="user-dashboard">
      <div class="description-user-dashboard">
        zdarova krasiviye
        <p>user id: #{{ user.id }}</p>
        <p>name: {{ user.name }}</p>
        <p>WINRATE: {{ user.winRate }}</p>
        <p>BALANCE: {{ user.balance }} ACEY</p>
      </div>
      <img :src="userpic" alt="" class="userpic-user-dashboard">
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
      userpic() {
        return userpic
      }
    }
  }
</script>

<style>
  .user-dashboard {
    display: flex;
    flex-flow: row;
  }
  
  .userpic-user-dashboard {}
  
  .description-user-dashboard {
    width: 50%;
  }
</style>
