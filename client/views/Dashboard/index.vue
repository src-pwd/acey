<template>
    <div class="dashboard">
        <div v-for="element in events">
            <dashboard-element :details="element"></dashboard-element>
        </div>
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
        mounted() {
            console.log(this.getToken)
        },
        computed: {
            getToken() {
                return this.$store.state.auth.jwt
            }
        },
        methods: {
            fetchData() {
                fetch('http://localhost:8000/api/events/', {
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
