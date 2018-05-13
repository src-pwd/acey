<template>
    <div class="dashboard">
        <div class="container">
            <div class="leaderboard-head first-create-desc"><span>Leaderboard</span></div>
            
            <div class="container-leaderboard">
                <div class="leaderboard-desc"><span>ID</span><span>Username</span><span>Rate</span></div>
                <leaderboard-element :details="element" :id="index" v-for="(element,index) in elements" :key="index"></leaderboard-element>
            </div>
        </div>
        <router-view></router-view>
    </div>
</template>


<script>
    import element from './element.vue'
    export default {
        components: {
            'leaderboard-element': element
        },
        data() {
            return {
                elements: []
            }
        },
        mounted() {
            this.fetchData()
        },
        computed: {
            getToken() {
                return this.$store.state.auth.jwt
            }
        },
        methods: {
            fetchData() {
                fetch('http://localhost:8000/api/leaderboard/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.elements = el
                    })
            }
        }
    }
</script>
