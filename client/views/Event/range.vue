<template>
    <div>
        <div class="range-items">
            <div v-for="item in options" :key="item.id" class="range-board" :class="selected === item ? 'active': ''" @click="chooseOption(item)">
                <div>From {{item.sum_from}}</div>
                <div>To {{item.sum_to}}</div>
                <div class="range-item-bottombar">
                    <font-awesome-icon :icon="sumo" />{{item.total_sum}} ACEY
                    <font-awesome-icon :icon="users" />{{item.total_users}}</div>
            </div>
        </div>
        <div class="range-items-pay">
           <label class="range-items-pay-label">
            Your investment
           </label>
           <br>
            <input class="range-items-pay-input" v-model="sum" placeholder="your investment"/>
            <span class="range-items-pay-currency"> ACEY</span>    
        </div>
        <div class="row-block-button">
            <div><button class="vote-range-button" @click="voteFor">vote</button></div>
        </div>
    </div>
</template>


<script>
    import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
    import {
        faUser
    } from '@fortawesome/fontawesome-free-solid'
    import {
        faDatabase
    } from '@fortawesome/fontawesome-free-solid'
    
    export default {
        components: {
            FontAwesomeIcon
        },
        mounted() {
            this.fetchData()
        },
        computed: {
            username() {
                return this.$store.state.auth.username
            },
            sumo() {
                return faDatabase
            },
            users() {
                return faUser
            },
        },
        methods: {
    
            fetchData() {
                fetch('http://app.acey.it/api/options/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.options = el.filter(l => l.event == this.$route.params.id)
                    })
                fetch('http://app.acey.it/api/users/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                    })
            },
            chooseOption(item) {
                this.selected = item
            },
            voteFor() {
                var payload = {
                    "option": this.selected.id,
                    "bettor": this.username,
                    "sum": this.sum
                }
                this.$store.dispatch("predictionBet", payload).then(() => {
                    this.$router.push('/dashboard')
                })
    
            }
        },
        data() {
            return {
                options: [],
                selected: null,
                sum: 0
            }
        }
    }
</script>
