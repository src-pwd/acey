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
                    <div class="app-main-nav-link">
                        <span>Leadersboard</span>
                        <span class="soon-header-sticker">SOON</span>
                    </div>
                </div>
                <router-link tag="div" class="app-main-nav-link app-main-nav-userpart" to="/profile">
                    <div class="userpart-details" v-if="profileRoute"> 
                        <div class="userpart-username">{{username}}</div>
                        <div class="userpart-sum">{{sum}} ACEY</div>
                        <div class="userpart-button"></div>
                    </div>
                    <div class="userpart-details-raw" v-else>
                        <div class="userpart-username-raw">{{username}}</div>
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
        }
    }
</script>