<template>
    <div>
        <router-link v-for="element in details" :key="element.id" tag="div" :to="'/option' + '/' + element.id" :id="element.id" class="dashboard-element-block">
            <div class="parlay-dashboard-block">
                <div class="parlay-info">Bet{{element.bet_sum}}</div>
                <div class="parlay-info">Bettor{{element.bettor}}</div>
                <div class="parlay-info">Createed{{element.created}}</div>
                <div class="parlay-info">Creator{{element.creator}}</div>
                <div class="parlay-info">Event{{element.event}}</div>
                <div class="parlay-info">Id{{element.id}}</div>
                <div class="parlay-info">Coef{{element.koefficient}}</div>
                <div class="parlay-info">Status{{element.status}}</div>
                <div class="parlay-info">min{{element.min_sum}}</div>
                <div class="parlay-info">max{{element.max_sum}}</div>
            </div>
        </router-link>
        <router-view></router-view>
    </div>
</template>



<script>
    import voteparlay from './voteparlay'
    export default {
        data() {
            return {
                details: {},
                sum: 0
            }
        },
        mounted() {
            this.fetchData()
        },
        methods: {
            fetchData() {
                fetch('http://localhost:8000/api/parleys/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.details = el
                    })
            }
        }
    
    }
</script>

<style lang="scss">
    
</style>