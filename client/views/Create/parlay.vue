<template>
    <div class="container">
        <p class="first-create-desc">2. Configure your prediction</p>
        <h1 class="prediction-type">Parlay</h1>
        <div class="range-bet-head-container">
            <label for="bet-name">Name of prediction:</label>
            <input name="bet-name" type="text" class="range-bet-head" :value="name" @input="changeName" placeholder="Enter prediction name">
        </div>
        <div class="range-bet-description-container">
            <label for="bet-desc">Description:</label>
            <textarea maxlength="200" name="bet-desc" type="text" class="range-bet-description" :value="description" @input="changeDescription" placeholder="Enter prediction description (max: 200 symbols)" width="100%"></textarea>
            <label for="pair">Select exchange:</label>
            <select name="pair" class="range-bet-select-pair" @change="changeExchange">
                <option class="range-bet-select-pair-option" :value="bittrex">bittrex</option>
                <option class="range-bet-select-pair-option" :value="poloniex">poloniex</option>
                <option class="range-bet-select-pair-option" :value="binance">binance</option>
            </select>
            <label for="exchange">Select pair:</label>
            <select name="exchange" class="range-bet-select-exchange" @change="changePair">
                <option class="range-bet-select-exchange-option" :value="ETH/USD">ETH/USD</option>
                <option class="range-bet-select-exchange-option" :value="BTC/USD">BTC/USD</option>
                <option class="range-bet-select-exchange-option" :value="DASH/USD">DASH/USD</option>
            </select>
        </div>
        <div class="range-bet-description-expired range-bet-description-container">
            <label for="bet-name">Expired:</label>
            <datepicker placeholder="Enter your date" class="datepicker-expired" :value="expired" @selected="changeExpired"></datepicker>
        </div>
        <button class="save-button" @click="saveAccuracy"><span>SAVE</span></button>
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
                this.$store.commit('updateExchangeAcc', e.target.value)
            },
            changePair(e) {
                this.$store.commit('updatePairAcc', e.target.value)
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

<style lang="scss">
    .range-bet-head-container {
        margin: 50px;
    }
    
    .range-bet-description-container {
        margin: 50px;
    }
    
    .rangeitem-container {
        display: flex;
        flex-flow: row;
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
        &>span {
            text-align: center;
        }
    }
</style>
