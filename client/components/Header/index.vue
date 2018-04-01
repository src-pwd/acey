<template>
    <div class="header">
       
        <div class="container">
            <div class="app-main-nav">
                 <img class="logo" src="/static/Acey_logo.png" alt="">
                <router-link to="dashboard">Dashboard</router-link>
                <router-link to="create">Create</router-link>
                <router-link to="user_dashboard">User's dashboard</router-link>
            </div>
    
        </div>
    
    </div>
</template>

<script>
    export default {
        data() {
            return {
    
            }
        }
    }
</script>


<style lang="scss" scoped>
    .logo {
        display: block;
        width: 200px;
        height: 200px;
    }
</style>
