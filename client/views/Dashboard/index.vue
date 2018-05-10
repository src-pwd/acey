<template>
    <div class="dashboard">
            <dashboard-element :details="element" v-for="element in events" :key="element.id"></dashboard-element>
        <router-view></router-view>
    </div>
</template>

<script>
    import element from './element.vue'
    export default {
        components: {
            'dashboard-element': element
        },
        data() {
            return {
                events: []
            }
        },
        created() {
            
            this.fetchData()
        },
        computed: {
            getToken() {
                return this.$store.state.auth.jwt
            }
        },
        methods: {
            fetchData() {
                fetch('http://app.acey.it/api/events/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.events = el
                    })
            }
        }
    }
</script>
