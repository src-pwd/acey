<template>
    <div class="container event-container">
        <div class="event-desc">
            <div class="event-name">{{ details.name }}</div>
            <div class="event-description">{{ details.description }}</div>
        </div>
        <div class="event-exchange-flex-container">
            <div class="event-exchange-container">
                <div class="event-exchange">Exchange <span>{{ details.exchange }}</span></div>
                <div class="event-pair"><span>{{ details.currency_pair }}</span></div>
                <div class="event-expired">Expired in <span>{{ expiredDay }}</span> days</div>
            </div>
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
            },
            expiredDay() {
                let oneDay = 24 * 60 * 60 * 1000;
                let firstDate = new Date(this.details.expired) || ''
                let secondDate = new Date(this.details.created) || ''
                return Math.round(Math.abs((firstDate.getTime() - secondDate.getTime()) / (oneDay)));
            },
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
