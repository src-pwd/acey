<template>
    <div class="range-items">
        <div
            v-for="item in options"
            :key="item.id" class="range-board"
            :class="selected === item ? 'active': ''"
            @click="chooseOption(item)"
            >
           <div>Sum from:{{item.sum_from}}</div>
           <div>Sum to:{{item.sum_to}}</div>
           <div>Total sum:{{item.total_sum}}</div>
           <div>Total users:{{item.total_users}}</div>
            
        </div>
    </div>
    
</template>


<script>
    export default {
        mounted() {
            this.fetchData()
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
            },
            chooseOption(item) {
                console.log(item)
                this.selected = item
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
</style>