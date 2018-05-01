<template>
    <div class="header">

        <div class="header-container">
            <div class="app-main-nav">
                <div class="main-nav-logo">
                    <img class="logo-main-nav" src="Acey_logo.png" alt="">
                </div>
                <div class="app-main-nav-links">
                    <router-link tag="div" class="app-main-nav-link" to="/dashboard">
                        <span>Dashboard</span>
                    </router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/create">
                        <span>Create</span>
                    </router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/profile">
                        <span>User's dashboard</span>
                    </router-link>
                </div>
                <div class="app-main-nav-userpart">
                    <div class="userpart-details">
                        <div class="userpart-username">{{username}}</div>
                        <div class="userpart-sum">{{sum}} ACEY</div>
                        <div class="userpart-button"></div>
                    </div>
                    <div class="userpart-userpic-container">
                        <img class="userpart-userpic" src="kekes.svg" alt="">
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>

<script>
    export default {
        data() {
            return {

            }
        },
        
        computed: {
            username() {
                return this.$store.state.auth.username
            },
            sum() {
                return this.$store.state.user.details.sum
            }
        }
    }
</script>