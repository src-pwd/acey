<template>
    <div class="container event-container">
        <div class="event-desc">
            <div class="event-name"><span>Name</span>{{ details.name }}</div>
            <div class="event-description"><span>Description</span>{{ details.description }}</div>
            <div class="event-expired"><span>Expired</span>{{ details.expired }}</div>
            <div class="event-expired"><span>Created</span>{{ details.created }}</div>
    
        </div>
        <div v-if="details.type === 'Prediction'">
            <div class="prediction-options">
                <div v-for="option in options" class="option">
                    <div class="option-text total_users">Total users {{option.total_users}}</div>
                    <div class="option-text total_sum">Total ACEY {{option.total_sum}}</div>
                    <div class="option-text sum_from">From {{option.sum_from}}</div>
                    <div class="option-text sum_to">To {{option.sum_to}}</div>
                </div>
            </div>
            <input name="bet-name" type="text" class="range-bet-head" :value="name" @input="changeName" placeholder="Enter your ACEY">
            <button class="save-button">Predict!</button>
        </div>
        <div v-if="details.type === 'AccuratePrediction'">
    
        </div>
        <div v-if="details.type === 'Parlay'">
    
        </div>
    </div>
</template>


<script>
    const eventsList = [// {
    //     "id": 1,
    //     "creator": "Andryuha",
    //     "name": "TestimDalbshe",
    //     "status": "New",
    //     "type": "Parley",
    //     "created": "2018-03-08T06:03:05.983434+02:00",
    //     "expired": "2018-03-24T01:59:00+02:00",
    //     "description": "Taki Dila",
    //     "currency_pair": "BTC/ETH",
    //     "exchange": "Bitrex",
    //     "total_users": 8,
    //     "total_sum": 228
    // },
    {
        "id": 8,
        "creator": "Andryuha",
        "name": "ETC",
        "status": "New",
        "type": "Prediction",
        "created": "2018-03-12 20:13:12",
        "expired": "2019-09-29 12:00:00",
        "expires": "5 month",
        "description": "ETC 09.2019",
        "currency_pair": "awdwa",
        "exchange": "awfw",
        "total_users": 1,
        "total_sum": 100
    },
    {
        "id": 11,
        "creator": "Andryuha",
        "name": "BTC > 100.000",
        "status": "New",
        "type": "Parley",
        "created": "2018-03-14 04:19:57",
        "expired": "2021-09-29 12:00:00",
        "expires": "5 month",        
        "description": "BTC will hit 100.000 until 2021.",
        "currency_pair": "awdaw",
        "exchange": "awdwaf",
        "total_users": 2,
        "total_sum": 0
    },
    {
        "id": 12,
        "creator": "Lyosik",
        "name": "Accurate price BTC",
        "status": "New",
        "type": "AccuratePrediction",
        "created": "2018-03-14 21:57:26",
        "expired": "2019-05-29 12:00:00",
        "expires": "2 month",        
        "description": "What price will be BTC this time next year",
        "currency_pair": "BTC/XRP",
        "exchange": "Binance",
        "total_users": 1,
        "total_sum": 23
    },
    {
        "id": 13,
        "creator": "andrey_shishkin",
        "name": "NEM would be more than 9k",
        "status": "New",
        "type": "Parley",
        "created": "2018-04-03 01:11:04",
        "expired": "2021-02-02 00:58:00",
        "expires": "7 month",                
        "description": "blablabla",
        "currency_pair": "ETH/BTC",
        "exchange": "Bittrex",
        "total_users": 0,
        "total_sum": 0
    },
    {
        "id": 14,
        "creator": "andrey_sh",
        "name": "EOS Price",
        "status": "New",
        "type": "Parley",
        "created": "2018-04-03 01:13:49",
        "expired": "2021-02-02 00:58:00",
        "expires": "3 month",        
        
        "description": "EOS price would reach 9k before may",
        "currency_pair": "EOS/BTC",
        "exchange": "Bittrex",
        "total_users": 0,
        "total_sum": 0
    },
    {
        "id": 15,
        "creator": "andrey_sh",
        "name": "EOS Price",
        "status": "New",
        "type": "Parley",
        "created": "2018-04-03 01:14:23",
        "expired": "2021-02-02 00:58:00",
        "expires": "9 month",        
        
        "description": "EOS price would reach 9k before may",
        "currency_pair": "EOS/BTC",
        "exchange": "Bittrex",
        "total_users": 0,
        "total_sum": 0
    }
    ]
    //hardcode ^^^  
    const prediction = [{
        "id": 8,
        "creator": "Andryuha",
        "name": "ETC",
        "status": "New",
        "type": "Prediction",
        "created": "2018-03-12 20:13:12",
        "expired": "2019-09-29 12:00:00",
        "description": "ETC 09.2019",
        "currency_pair": "awdwa",
        "exchange": "awfw",
        "total_users": 1,
        "total_sum": 100,
        "options": [{
                "id": 2,
                "event": 8,
                "total_users": 2,
                "total_sum": 133,
                "sum_from": 23,
                "sum_to": 123
            },
            {
                "id": 3,
                "event": 8,
                "total_users": 0,
                "total_sum": 0,
                "sum_from": 11,
                "sum_to": 22
            }
        ]
    }]
    
    
    
    //preds: 
    export default {
        mounted() {
            this.fetchData()
        },
        methods: {
            fetchData() {
                let lel = eventsList.filter(el => el.id == this.$route.params.id)[0]
                this.details = lel
                this.options = prediction[0].options
                
                
                fetch('http://localhost:8000/api/accuratepredictions/',{
                    method: 'GET'
                }).then(el => el.json().then(el => console.log(el)))
            }
        },
        data() {
            return {
                details: {},
                options: []
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
        
        .range-bet-head {
        margin-right: auto;
        margin-left: 40%;
        width: 200px;
        padding-left: 20px;
        font-size: 24px;
        background-color: #1a1a1a;
        color: white;
        border: none;
        &:active {
            outline: none;
            border-bottom: 2px solid orange;
        }
    }
    
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