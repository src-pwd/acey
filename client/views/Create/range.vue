<template>
    <div class="container range-create">
    <p class="first-create-desc">2. Configure your prediction</p>
        <h1 class="prediction-type">Range</h1>
        <div class="range-bet-head-container">
            <label for="bet-name">Name of prediction:</label>
            <input name="bet-name" type="text" class="range-bet-head" :value="name" @input="changeName" placeholder="Enter prediction name">
        </div>
        <div class="range-bet-description-container">
            <label for="bet-desc">Description:</label>
            <textarea maxlength="200" name="bet-desc" type="text" class="range-bet-description" :value="description" @input="changeDescription" placeholder="Enter prediction description (max: 200 symbols)" width="100%"></textarea>
            <label for="pair">Select exchange:</label>
            <select name="pair" class="range-bet-select-pair" @change="changeExchange">
                <option class="range-bet-select-pair-option" value="bittrex">bittrex</option>
                <option class="range-bet-select-pair-option" value="poloniex">poloniex</option>
                <option class="range-bet-select-pair-option" value="binance">binance</option>
                
            </select>
            <label for="exchange">Select pair:</label>            
            <select name="exchange" class="range-bet-select-exchange" @change="changePair">
                <option class="range-bet-select-exchange-option" value="ETH/USD">ETH/USD</option>
                <option class="range-bet-select-exchange-option" value="BTC/USD">BTC/USD</option>
                <option class="range-bet-select-exchange-option" value="DASH/USD">DASH/USD</option>
            </select>
        </div>
        <div class="range-bet-description-expired">
            <label for="bet-desc">Expired:</label>
            <datepicker placeholder="Enter your date" class="datepicker-expired" :value="expired" @selected="changeExpired"></datepicker>
        </div>
        <div class="rangeitem-container">
            <div v-for="(item,index) in options" class="range-bet-rangeitem">
                <input type="number" :value="item.priceFrom" @input="itemPriceFromChange($event, index)" placeholder="from">
                <input type="number" :value="item.priceTo" @input="itemPriceToChange($event,index)" placeholder="to">
                <div class="delete-button" @click="deleteRange(item)"><span>delete</span></div>
            </div>
            <div class="add-to-ranges">
                <button @click="addNewRange" v-if="options.length < 5" class="save-button">Add</button>
            </div>
        </div>
        <button @click="saveRangePrediction" class="save-button">SAVVEEEEE</button>
    </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
    import {
        mapState,
        mapActions
    } from 'vuex'
    
    export default {
        name: 'Range',
        components: {
            Datepicker
        },
        computed: {
            options() {
                return this.$store.state.range.options
            },
            name() {
                return this.$store.state.range.name
            },
            description() {
                return this.$store.state.range.description
            },
            expired () {
                return this.$store.state.range.expired
            },
            created () {
                return this.$store.state.range.created
            }
    
        },
        watch: {
          created () {
              this.$router.push('/dashboard')
          } 
        },
       
        methods: {
            changeExchange(e) {
                this.$store.commit('updateExchange', e.target.value)                  
            },
            changePair(e) {
                this.$store.commit('updatePair', e.target.value)  
            },
            changeName(e) {
                this.$store.commit('updateName', e.target.value)
            },
            changeDescription(e) {
                this.$store.commit('updateDesc', e.target.value)
            },
            changeExpired(e) {
                e = e.toISOString().slice(0,-5)
                this.$store.commit('updateExp', e)
            },
            deleteRange(item) {
                this.$store.commit('deleteRange', item.name)
            },
            itemNameChange(e,index) {
                let payload = [e.target.value, index]
                this.$store.commit('itemName', payload)
            },
            itemPriceFromChange(e,index) {
                let payload = [e.target.value, index]
                this.$store.commit('itemPriceFrom', payload)    
            },
            itemPriceToChange(e,index) {
                let payload = [e.target.value, index]                
                this.$store.commit('itemPriceTo', payload)
            },
            ...mapActions(['addNewRange', 'saveRangePrediction'])
    
        },
        data() {
            return {
                date: ''
            }
        }
    }
</script>

<style lang="scss">

.range-bet-head:active, .range-bet-head:focus {
    outline: none;
    border-bottom: 2px solid orange;
}


    .range-create {
        .range-bet-head-container {
    }
    
    
    
    .range-bet-description {
        &-container {
    }
     &-expired {
        display: flex;
         margin: 50px;
    }
    }
    
.datepicker-expired input {
    background: transparent;
    outline: 0;
    border: 0;
    color: #757575;
    font-size: 24px;
    margin: 20px 0 0 -40px;
}
    
    .rangeitem-container {
        display: flex;
        flex-flow: row;
    }
    
    textarea {
        outline: none;
    width: 470px;
    margin-bottom: -30px;
    }
    .range-bet-rangeitem {
        display: flex;
        flex-flow: column;
        width: 20%;
        margin: 10px;
        height: 200px;
        border: 1px solid orange;
        & > input {
            font-size: 24px;
    background-color: #1a1a1a;
    color: white;
    border: none;
    outline:0;
    &:active, &:focus {
        outline: none;
        border-bottom: 2px solid orange;
    }
        }
    }
    
    .bet-name {
        margin-left: auto;
        margin-right: auto;
    }
    
    select {
        color: white;
    }
    
    .save-button {
        display: flex;
        flex-flow: row;
        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
    }
    
    .delete-button {
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        padding: 10px;
        border: 1px solid white;
        border-radius: 5px;
        
    }
    
    
    
input[type="text"] {
    background: transparent;
}
.range-bet-head {
    width: 400px;
    padding-left: 20px;
    font-size: 24px;
    background-color: #1a1a1a;
    color: white;
    border: none;
}
.range-bet-head {
    width: 400px;
    padding-left: 20px;
    font-size: 24px;
    background-color: #1a1a1a;
    color: white;
    border: none;
    outline: 0;
}
    }
</style>
