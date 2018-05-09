<template>
    <div class="container event-container">
        <div class="event-desc">
            <div class="event-name"><span>Name</span>{{ details.name }}</div>
            <div class="event-description"><span>Description</span>{{ details.description }}</div>
            <div class="event-expired"><span>Expired</span>{{ details.expired }}</div>
            <div class="event-expired"><span>Created</span>{{ details.created }}</div>
        </div>
        <div v-if="details.type === 'Prediction'">
            <range />
        </div>
        <div v-if="details.type === 'AccuratePrediction'">
            <accuracy />
        </div>
        <div v-if="details.type === 'Parley'">
            <parlay />
        </div>
    </div>
</template>


<script>
    import accuracy from "./accuracy"
    import range from "./range"
    import parlay from "./parlay"
    
    export default {
        components: {
            accuracy,
            range,
            parlay
        },
        mounted() {
           
            this.fetchData();   
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
                            "Content-Type": "application/json",
                            "Authorization": "JWT " + this.getToken
                        })
                    })
                    .then(response => {
                        return response.json()
                    })
                    .then((el) => {
                        this.details = el.find(x => x.id == this.$route.params.id)
                    })
            }
        },
        data() {
            return {
                details: {},
            }
        }
    
    }
</script>

<style lang="scss">
    .event-container {
        width: 1100px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .event-desc {
        font-size: 25px;
        color: white;
        margin-top: 100px;
        &>div>span {
            color: gray;
            padding-right: 100px;
        }
    }
    
    
    /* .event {
                    
                    &-name {
                        
                    }
                    &-id {
                        
                    }
                    &-desc {
                        
                    }
                    &-expiredv{
                        
                    }
                } */
    
   
    
    .prediction-options {
        margin-top: 50px;
        display: flex;
        flex-flow: row;
        justify-content: center;
    }
    
    .option {
        height: 200px;
        width: 200px;
        border: 1px solid orange;
        border-radius: 7px;
        padding: 30px;
        margin: 30px;
    }
    
    .option-text {
        font-size: 20px;
    }
    
    .save-button {
        display: flex;
        flex-flow: row;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        outline: 0;
        background-color: transparent;
        border-radius: 7px;
        height: 30px;
        color: orange;
        width: 90px;
        margin-bottom: 50px;
    }
</style>