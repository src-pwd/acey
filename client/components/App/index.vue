<template>
<div id="app">
    <div class="page-layout">
        <header-c :title="title" v-if="isRlyLogged"></header-c>
        <div class="main-content">
          <transition name="fade">
                  <router-view></router-view>            
          </transition>
        </div>
            <!-- <footer-c class="footer" v-if="isLogged"></footer-c>-->
    </div>
</div>
</template>
<script>

import { mapActions, mapState } from 'vuex'
import Header from 'components/Header'
import Footer from 'components/Footer'
  import fetch from 'isomorphic-fetch'

export default {
  name: 'App',
  methods: {
    ...mapActions(['handleResize', 'openSidebar', 'closeSidebar'])
  },
  data() {
    return { 
      skert: false
    }
  },
  computed: {
    ...mapState({
        obfuscatorActive: state => {
            return state.ui.obfuscatorActive
        },
        title: state => {
          return state.route.meta.title
        },
        jwt: state => {
          return state.auth.jwt
        }
        
    }),
     getToken() {
                return this.$store.state.auth.jwt
            },
      isRlyLogged() {
        return this.$store.state.auth.loggedIn 
      }
  },
  mounted() {
    console.log(this.isRlyLogged)
  },

  components: {
     'header-c' :Header,
     'footer-c' :Footer
  },
  created() {
    window.addEventListener('resize', this.handleResize)
    
  },
  beforeUpdate() {
      this.$store.dispatch('inspectToken')
  }
}
</script>

<style lang="scss">
// You can import all your SCSS variables using webpack alias
@import '~scss_vars';
@import './style.scss';
</style>
