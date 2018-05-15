

<template>
    <div class="container range-create">
        <p class="first-create-desc"><span class="big-number-create">2</span> Configure your prediction</p>
        <div class="range-bet-head-container">
            <label class="range-bet-name-label" for="bet-name">Prediction name </label>
            <input name="bet-name" type="text" class="range-bet-name" :value="name" @input="changeName" placeholder="Name of event">
            <p class="text-danger" v-if="errors.name">
            	{{ errorDescription(errors.name) }}
            </p>
        </div>
        <div class="range-bet-description-container">
            <label for="bet-desc" class="range-bet-description-label">Description</label>
            <input maxlength="200" name="bet-desc" type="text" class="range-bet-desc" :value="description" @input="changeDescription" placeholder="Provide short description">
            <p class="text-danger" v-if="errors.description">
            	{{ errorDescription(errors.description) }}
            </p>
        </div>
        <div class="range-bet-exchange-container">
            <div class="range-bet-exchange-selector">
                <label for="pair" class="range-bet-select-pair-label">Select exchange</label>
                <select name="pair" class="range-bet-select-pair" @change="changeExchange">
                        <option class="range-bet-select-pair-option" value="bittrex" selected>bitfinex</option>
                        <option class="range-bet-select-pair-option" value="poloniex" disabled>poloniex</option>
                        <option class="range-bet-select-pair-option" value="binance" disabled>binance</option>
                    </select>
                     <p class="text-danger" v-if="errors.exchange">
            	{{ errorDescription(errors.exchange) }}
            </p>
            </div>
            <div class="range-bet-exchange-selector">
                <label for="exchange" class="range-bet-select-exchange-label">Select pair</label>
                <select name="exchange" class="range-bet-select-exchange" size="5" @change="changePairIn">
                        <option class="range-bet-select-exchange-option" :disabled="pairOut == 'DASH'" value="DASH" selected>DASH</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairOut == 'XMR'" value="XMR">XMR</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairOut == 'BTC'" value="BTC">BTC</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairOut == 'LTC'" value="LTC">LTC</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairOut == 'ETH'" value="ETH">ETH</option>
                    </select>
                <select name="exchange" class="range-bet-select-exchange" size="5" @change="changePairOut">
                        <option class="range-bet-select-exchange-option" :disabled="pairIn == 'DASH'" value="DASH">DASH</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairIn == 'XMR'"  value="XMR" selected>XMR</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairIn == 'BTC'"  value="BTC">BTC</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairIn == 'LTC'"  value="LTC">LTC</option>
                        <option class="range-bet-select-exchange-option" :disabled="pairIn == 'ETH'"  value="ETH">ETH</option>
                    </select>
                    <p class="text-danger" v-if="errors.pair">
            	{{ errorDescription(errors.pair) }}
            </p>
            </div>
            <div class="range-bet-exchange-selector">
                <label for="bet-desc" class="datepicker-expired-label">Expired</label>
                <datepicker :monday-first="true" :disabledDates="disabledDates" placeholder="Enter your date" class="datepicker-expired" :value="expired" @selected="changeExpired"></datepicker>
                <p class="text-danger" v-if="errors.expired">
            	{{ errorDescription(errors.expired) }}
            </p>
            </div>
        </div>
        <div class="rangeitem-container">
            <div v-for="(item,index) in options" class="range-bet-rangeitem">
                <input type="number" v-model="item.sum_from" placeholder="from">
                <input type="number" v-model="item.sum_to" placeholder="to">
                <div class="delete-button" @click="deleteRange(item)"><span>delete</span></div>
            </div>
            
            <div class="add-to-ranges">
                <button @click="addNewRange" v-if="options.length < 7" class="save-button">Add</button>
            </div>
        </div>
        <div class="rangeitem-button">
            <button @click="saveRange" class="save-button">SAVE</button>
        </div>
        	<p class="text-danger" v-if="errors.save">
					{{ errorDescription(errors.save) }}
				</p>
    </div>
</template>

<script>
    import Datepicker from 'vuejs-datepicker';
    import {
        mapState,
        mapActions
    }
    from 'vuex'
    
    export default {
        name: 'Range',
        components: {
            Datepicker
        },
        computed: {
            name() {
                return this.$store.state.range.name
            },
            description() {
                return this.$store.state.range.description
            },
            expired() {
                return this.$store.state.range.expired
            },
            created() {
                return this.$store.state.range.created
            },
            errors() {
                return this.$store.state.range.errors
            },
            pairIn() {
                return this.$store.state.range.currency_pairin
            },
            pairOut() {
                return this.$store.state.range.currency_pairout
            }
    
        },
        watch: {
            created() {
                this.$router.push('/dashboard')
            },
            errors() {
                this.errorsList = this.errors
            }
        },
        methods: {
            errorDescription(error) {
                if (error === this.errors.expired) {
                    let err = error[0]
                    err = err.substr(0,26)
                    return err
                }
                return error[0]
            },
            changeExchange(e) {
                this.$store.commit('updateExchange', e.target.value)
            },
            changePairIn(e) {
                this.$store.commit('updatePairIn', e.target.value)
            },
            changePairOut(e) {
                this.$store.commit('updatePairOut', e.target.value)
            },
            changeName(e) {
                this.$store.commit('updateName', e.target.value)
            },
            changeDescription(e) {
                this.$store.commit('updateDesc', e.target.value)
            },
            changeExpired(e) {
                e = e.toISOString().slice(0, -5)
                this.$store.commit('updateExp', e)
            },
            deleteRange(item) {
                this.options = this.options.filter(el => el.index != item.index)
            },
            itemNameChange(e, index) {
                let payload = [e.target.value, index]
                this.$store.commit('itemName', payload)
            },
            addNewRange(e) {
                let min = Math.ceil(1);
                let max = Math.floor(50);
                
                let newIndex = Math.floor(Math.random() * (max - min)) + min;
                let item = {
                    index: newIndex,
                    sum_from: 0,
                    sum_to: 0
                }
                this.options.find(el => el.index == newIndex) ?
                        this.options.push({
                            index: newIndex + newIndex,
                            sum_from: 0,
                            sum_to: 0
                        }) :
                        this.options.push(item)
                this.$store.commit('updateOptions', this.options)
            },
          saveRange(e) {
               this.$store.dispatch('saveRangePrediction')
               setTimeout(()=>{
                   console.log('el')
                   this.errorsList = []
               }, 5000)
          }
    
        },
        data() {
            return {
                date: '',
                options: [{
                        index: 0,
                        sum_from: 0,
                        sum_to: 0
                    },
                ],
                errorsList: []
    
            }
        }
    }
</script>
