<template>
<div id="app">
    <div class="page-layout">
            <header-c :title="title"></header-c>
            <div class="main-content">
                    <router-view></router-view>
            </div>
    </div>
</div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import Header from 'components/Header'
export default {
  name: 'App',
  methods: {
    ...mapActions(['handleResize', 'openSidebar', 'closeSidebar'])
  },
  computed: {
    ...mapState({
        obfuscatorActive: state => {
            return state.ui.obfuscatorActive
        },
        title: state => {
          return state.route.meta.title
        }
    })
  },
  components: {
     'header-c' :Header
  },
  created: function () {
    window.addEventListener('resize', this.handleResize)
  }
}
</script>

<style lang="scss">
// You can import all your SCSS variables using webpack alias
@import '~scss_vars';
@import './style.scss';</style>
