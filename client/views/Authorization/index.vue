<template>
  <div class="container">
    <div class="main-acey-logoform">
      <div class="main-acey-logoform-left-part">
          <label class="main-acey-logoform-tabs-label"> Don't have account? </label> 
      
        <div class="main-acey-logoform-tabs">
         <div class="main-acey-logoform-tab" :class="selectedLogin ? 'active' : ''" @click="selectedLogin = true"><span>Login</span></div>
          <div class="main-acey-logoform-tab" :class="!selectedLogin ? 'active' : ''" @click="selectedLogin = false"><span>Register</span></div>
        </div>
         
        <div class="main-acey-logoform-inputs">
          <div class="login-form" v-if="selectedLogin">
            <input type="text" class="username-input" placeholder="username" :value="username" @input="changeUsername">
          <input type="text" class="password-input" placeholder="password" :value="password" @input="changePassword">
          <button class="confirm-button" @click="loginUser">
            LOGIN
          </button>
          </div>
          <div class="registration-form" v-else>
            <input type="text"  class="username-input" :value="username" placeholder="username" @input="changeUsername">
          <input type="text"  class="username-input" :value="password" placeholder="password" @input="changePassword">
          <input type="email"  class="username-input" :value="email" placeholder="email" @input="changeEmail"> 
          <button class="confirm-button" @click="registerUser">
            REGISTER 
          </button>
          </div>
          
        </div>
  
  
      </div>
      <div class="main-acey-logoform-right-part">
        <img src="Acey_In.gif" alt="">
  
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



<style lang="scss">
  .container {
  }
  
  .main-acey-logoform {
    padding-top: 100px;
    max-width: 1000px;
    max-height: 900px;
    display: flex;
    flex-flow: row;
    &-left-part {
      display: flex;
      flex-flow: column;
      width: 50%;
    }
    &-right-part {}
    &-tabs {
      display:flex;
      flex-flow: row;
    }
    
    &-tabs-label {
      font-size: 15px;
      padding-bottom: 30px;
    }
    
    &-tab {
      text-align: center;
    height: 50px;
    padding: 50px;
    border-bottom: 1px solid white;
}  
  &-tab.active {
    border-top: 3px solid orange;
    
  }


  }
  .login-form, .registration-form > input{
     
  }
  
  .username-input, .password-input {
    width: 400px;
      background-color: #1a1a1a;
      color: #fff;
      border: none;
      height: 100px;
      font-size: 24px;
      
  }
  
  .confirm-button {
    border: 1px solid orange;
    padding: 30px;
  }
  

  
</style>

