<template>
    <div class="container range-create">
        <p class="first-create-desc"><span class="big-number-create">2</span> Configure your prediction</p>
        <div class="range-bet-head-container">
            <label class="range-bet-name-label" for="bet-name">Prediction name </label>         
            <input name="bet-name" type="text" class="range-bet-name" :value="name" @input="changeName" placeholder="Name of event">
            <span class="highlight"></span>
            <span class="bar"></span>
        </div>
        <div class="range-bet-description-container">
            <label for="bet-desc" class="range-bet-description-label">Description</label>
            <input maxlength="200" name="bet-desc" type="text" class="range-bet-desc" :value="description" @input="changeDescription" placeholder="Provide short description">
        </div>
        <div class="range-bet-exchange-container">
            <div class="range-bet-exchange-selector">
             <label for="pair" class="range-bet-select-pair-label">Select exchange</label>
            <select name="pair" class="range-bet-select-pair" @change="changeExchange">
                <option class="range-bet-select-pair-option" value="bittrex">bittrex</option>
                <option class="range-bet-select-pair-option" value="poloniex">poloniex</option>
                <option class="range-bet-select-pair-option" value="binance">binance</option>
            </select>
            </div>
            <div class="range-bet-exchange-selector">
            <label for="exchange" class="range-bet-select-exchange-label">Select pair</label>            
            <select name="exchange" class="range-bet-select-exchange" @change="changePair">
                <option class="range-bet-select-exchange-option" value="ETH/USD">ETH/USD</option>
                <option class="range-bet-select-exchange-option" value="BTC/USD">BTC/USD</option>
                <option class="range-bet-select-exchange-option" value="DASH/USD">DASH/USD</option>
            </select>
            </div>
            <div class="range-bet-exchange-selector">
            <label for="bet-desc" class="datepicker-expired-label">Expired</label>
            <datepicker placeholder="Enter your date" class="datepicker-expired" :value="expired" @selected="changeExpired"></datepicker>
        </div>
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
        <div class="rangeitem-button">     
            <button @click="saveRangePrediction" class="save-button">SAVE</button>
        </div>
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
                console.log(item)
                this.$store.commit('deleteRange', item.index)
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
