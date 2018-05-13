<template>
    <div class="header">
        <div class="header-container">
            <div class="app-main-nav">
                <div class="main-nav-logo">
                    <img class="logo-main-nav" src="Acey_logo.png" alt="">
                </div>
                <div class="app-main-nav-links">
                    <router-link tag="div" class="app-main-nav-link" to="/dashboard">
                        <span>Predictions</span>
                    </router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/create">
                        <span>Creators Tool</span>
                    </router-link>
                    <router-link tag="div" class="app-main-nav-link" to="/leaderboard">
                        <span>Leaderboard</span>
                    </router-link>
                </div>
                <router-link tag="div" class="app-main-nav-link app-main-nav-userpart" to="/profile">
                    <div class="userpart-token">
                        <span class="userpart-token-sum-desc">Avaliable balance</span>
    
                        <span class="userpart-token-sum">{{ sum ? sum : '138' }}</span>
                        <div class="userpart-token-img-container">
                            <img class="userpart-token-img" src="acey_token.png">
                        </div>
                    </div>
                    <div class="userpart-userpic-container">
                        <img class="userpart-userpic" src="kekes.svg" alt="">
                    </div>
                </router-link>
            </div>
    
        </div>
    
    </div>
</template>

<script>
    export default {
        data() {
            return {
                showInfo: false
            }
        },
        mounted() {
            this.$store.dispatch('getUserInfo')
        },
        computed: {
            username() {
                return this.$store.state.auth.username
            },
            sum() {
                return this.$store.state.user.details.sum
            },
            profileRoute() {
                return this.$route.fullPath === "/profile"
            }
        },
        watch: {
            sum() {
                return this.sum
            }
        }
    }
</script>