<template>
    <div class="container">
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
                <option class="range-bet-select-pair-option" value="bittrex" selected>bitfinex</option>
                <option class="range-bet-select-pair-option" value="poloniex" disabled>poloniex</option>
                <option class="range-bet-select-pair-option" value="binance" disabled>binance</option>
            </select>
            </div>
            <div class="range-bet-exchange-selector">
            <label for="exchange" class="range-bet-select-exchange-label">Select pair</label>            
            <select name="exchange" class="range-bet-select-exchange" size="5" @change="changePairIn">
            dsh, xmr, btc, ltc, eth
                <option class="range-bet-select-exchange-option" value="DASH" selected>DASH</option>
                <option class="range-bet-select-exchange-option" value="XMR">XMR</option>
                <option class="range-bet-select-exchange-option" value="BTC">BTC</option>
                <option class="range-bet-select-exchange-option" value="LTC">LTC</option>
                <option class="range-bet-select-exchange-option" value="ETH">ETH</option>
            </select>
            <select name="exchange" class="range-bet-select-exchange" size="5" @change="changePairOut">
                <option class="range-bet-select-exchange-option" value="DASH">DASH</option>
                <option class="range-bet-select-exchange-option" value="XMR" selected>XMR</option>
                <option class="range-bet-select-exchange-option" value="BTC">BTC</option>
                <option class="range-bet-select-exchange-option" value="LTC">LTC</option>
                <option class="range-bet-select-exchange-option" value="ETH">ETH</option>
            </select>
            </div>
            <div class="range-bet-exchange-selector">
            <label for="bet-desc" class="datepicker-expired-label">Expired</label>
            <datepicker placeholder="Enter your date" class="datepicker-expired" :value="expired" @selected="changeExpired"></datepicker>
        </div>
        </div>
        <div class="rangeitem-button">     
            <button @click="saveAccuracy" class="save-button">SAVE</button>
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
        name: 'Accuracy',
        components: {
            Datepicker
        },
        computed: {
            name() {
                return this.$store.state.accuracy.name
            },
            description() {
                return this.$store.state.accuracy.description
            },
            expired() {
                return this.$store.state.accuracy.expired
            },
            created () {
                return this.$store.state.accuracy.created
            }
        },
        watch: {
          created () {
              this.$router.push('/dashboard')
          } 
        },
        methods: {
            changeExchange(e) {
                this.$store.commit('updateExchangeAcc', e.target.value)
            },
            changePairIn(e) {
                this.$store.commit('updatePairAccIn', e.target.value)
            },
            changePairOut(e) {
                this.$store.commit('updatePairAccOut', e.target.value)
            },
            changeName(e) {
                this.$store.commit('updateNameAcc', e.target.value)
            },
            changeDescription(e) {
                this.$store.commit('updateDescAcc', e.target.value)
            },
            changeExpired(e) {
                e = e.toISOString().slice(0, -5)
                this.$store.commit('updateExpAcc', e)
            },
               ...mapActions(['saveAccuracy'])
        },
        data() {
            return {
    
            }
        }
    }
</script>
