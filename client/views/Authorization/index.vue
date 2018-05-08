<template>
<div>
<img class="authorization-logo" src="Acey_logo.png">
  <div class="container">
    <div class="main-acey-logoform">
      <div class="main-acey-logoform-left-part">
      
        <div class="main-acey-logoform-tabs">
         <div class="main-acey-logoform-tab" :class="selectedLogin ? 'active' : ''" @click="selectedLogin = true"><span>LOGIN</span></div>
          <div class="main-acey-logoform-tab" :class="!selectedLogin ? 'active' : ''" @click="selectedLogin = false"><span>REGISTER</span></div>
        </div>
         
        <div class="main-acey-logoform-inputs">
          <div class="login-form" v-if="selectedLogin">
          <label class="main-acey-logoform-input-label" for="">Username</label>
            <input type="text" class="username-input main-acey-logoform-input" placeholder="Enter Username" :value="username" @input="changeUsername">
          <label class="main-acey-logoform-input-label" for="">Password</label>
          <input type="text" class="password-input main-acey-logoform-input" placeholder="Enter Password" :value="password" @input="changePassword">
          <button class="confirm-button" @click="loginUser">
            LOGIN
          </button>
          </div>
          
          <div class="registration-form" v-else>
          <p>New to ACEY?</p>
          <label class="main-acey-logoform-input-label" for="">Username</label>
            <input type="text" class="username-input main-acey-logoform-input" :value="username" placeholder="Your username" @input="changeUsername">
          <label class="main-acey-logoform-input-label" for="">Password</label>
          <input type="text"  class="username-input main-acey-logoform-input" :value="password" placeholder="Your password" @input="changePassword">
          
          <label class="main-acey-logoform-input-label" for="">E-mail</label>
          <input type="email"  class="username-input main-acey-logoform-input" :value="email" placeholder="yourmail@com.it" @input="changeEmail"> 
          <button class="confirm-button" @click="registerUser">
            REGISTER 
          </button>
          </div>
        </div>
  
  
      </div>
      <div class="main-acey-logoform-right-part">
        <img src="Acey_In.gif" class="logoform-right-part-pic" alt="">
  
      </div>
  
    </div>
  </div>
  </div>
</template>

<script>
  
  export default {
    computed: {
      username() {
        return this.$store.state.auth.username
      },
      password() {
        return this.$store.state.auth.password
      },
      email() {
        return this.$store.state.auth.email
      },
      isLogged() {
        return this.$store.state.auth.loggedIn
      }
  
  
  },

  watch: {
    isLogged () {
      this.$router.push('/dashboard')
    }
  },
    methods: {
      handleOptionChange(e) {
        return e.target.value === '0' ? false : true
      },
      changeUsername(e) {
        this.$store.commit('updateUsername', e.target.value)
      },
      changePassword(e) {
        this.$store.commit('updatePassword', e.target.value)
      },
      changeEmail(e) {
        this.$store.commit('updateEmail', e.target.value)
      },
      registerUser() {
        this.$store.dispatch('register')
        this.selectedLogin = true
      },
      loginUser() {
        this.$store.dispatch('obtainToken')
      }   
    },
    data( ) {
      return {
        loginReg: true,
        selectedLogin: true,
      }
    }
  }
</script>
