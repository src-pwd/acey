<template>
  <div class="container user-container">
    <div class="user-about">
      <p class="user-title">About</p>
      <div class="user-about-main">
        <p class="user-about-name"> <span>Name</span> {{ userInfo.user.username }} </p>
        <p class="user-about-mail"> <span>E-mail</span> {{ userInfo.user.email }} </p>
        <div class="user-userpic-container">
          <img class="userpart-userpic" src="kekes.svg" alt="">
        </div>
      </div>
  
    </div>
    <div class="user-achievments">
      <p class="user-title">Total</p>
      <p class="user-achievements-winrate"><span>Win rate</span> {{userInfo.win_rate}} </p>
      <p class="user-achievements-bets"><span>Bets</span> {{userInfo.bets}} </p>
      <p class="user-achievements-events"><span>Events</span> {{userInfo.events}} </p>
    </div>
    <div class="user-balance">
      <p class="user-title">Balance</p>
      <div class="user-balance-container">
        <span class="user-balance-sum">{{userInfo.sum}}</span>
        <div class="user-balance-img-container">
          <img src="acey_token.png">
        </div>
      </div>
    </div>
    <div class="user-balance">
      <div class="button-container">
        <button @click="logout">Logout</button>
      </div>
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
        // return this.$store.state.user.details
        return ({
          "user": {
            "username": "Andryuha",
            "email": "awda@gmail.com",
            "password": "pbkdf2_sha256 $36000$tA4KdsQQ0anK$Yo00zEKj9FVOz1P5n4GAVq+m+7frOelZ0kp9Pw4FIoU=",
            "first_nam e": "",
            "last_name": "",
            "date_joined": "2018-03- 08T06:02:00.043809+02:00",
            "last_login": null
          },
          "profile_picture": null,
          "rate": 0,
          "info": "Crypto Andryuha",
          "sum": 49809,
          "bets": 12,
          "events": 3,
          "activity_rate": null,
          "win_rate": 20
        })
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