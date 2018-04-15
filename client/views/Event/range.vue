<template>
<div>
    <div class="range-items">
        <div v-for="item in options" :key="item.id" class="range-board" :class="selected === item ? 'active': ''" @click="chooseOption(item)">
            <div>Sum from:{{item.sum_from}}</div>
            <div>Sum to:{{item.sum_to}}</div>
            <div>Total sum:{{item.total_sum}}</div>
            <div>Total users:{{item.total_users}}</div>
        </div>
       
    </div>
     <div class="row-block-button">
            <div ><button @click="voteFor">voteeeeee</button></div>
        </div>
        </div>
</template>


<script>
    export default {
        mounted() {
            this.fetchData()
        },
        computed: {
            username() {
                return this.$store.state.auth.username
            }
        },
        methods: {
            fetchData() {
                fetch('http://localhost:8000/api/options/', {
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
                        console.log(this.options)
                
                    })
                    fetch('http://localhost:8000/api/users/', {
                        method: "GET", // or 'PUT'
                        headers: new Headers({
                            "Content-Type": "application/json"
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                       
                        console.log(el)
                    })
            },
            chooseOption(item) {
                console.log(item)
                this.selected = item
            },
            voteFor() {
                var payload = {
                    "option": this.selected.id,
                    "bettor": this.username,
                    "sum": 0
                }
                this.$store.dispatch("predictionBet", payload).then(()=>{
                        this.$router.push('/dashboard')                    
                })
                
            }
        },
        data() {
            return {
                options: [],
                selected: null
            }
        }
    }
</script>

<style lang="scss">
    .range-items {
        display: flex;
        justify-content: center;
        flex-flow: row;
    }
    
    .range-board {
        display: flex;
        flex-flow: column;
        padding: 50px;
    }
    
    .active {
        border: 1px solid orange;
    }
    
    .row-block-button {
        padding-top: 50px;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        flex-flow: row;
        justify-content: center;
    }
</style>