<template>
    <div>
        <h1>Range page</h1>
        <div class="range-bet-head-container">
            <label for="bet-name">Name of prediction:</label>
            <input name="bet-name" type="text" class="range-bet-head" :value="name" @input="changeName" placeholder="enter prediction name">
        </div>
        <div class="range-bet-description-container">
            <label for="bet-desc">Description:</label>
            <textarea name="bet-desc" type="text" class="range-bet-description" :value="description" @input="changeDescription" placeholder="enter prediction description" width="100%"></textarea>
        </div>
        <div class="range-bet-description-expired">
            <label for="bet-desc">Expired:</label>
            <input name="bet-desc" type="text" class="range-bet-description" :value="expired" @input="changeExpired" placeholder="enter prediction description" width="100%">
        </div>
        <div class="rangeitem-container">
            <div v-for="(item,index) in ranges" class="range-bet-rangeitem">
                <input type="text" :value="item.name" @input="itemNameChange($event,index)" placeholder="name">
                <input type="number" :value="item.priceFrom" @input="itemPriceFromChange($event, index)" placeholder="from">
                <input type="number" :value="item.priceTo" @input="itemPriceToChange($event,index)" placeholder="to">
                <button @click="deleteRange(item)">X</button>
            </div>
            <div class="add-to-ranges">
                <button @click="addNewRange" v-if="ranges.length < 5">Add nahuy</button>
            </div>
        </div>
        <button @click="saveRangePrediction" class="save-button">SAVVEEEEE</button>
    </div>
</template>

<script>
    import {
        mapState,
        mapActions
    } from 'vuex'
    
    export default {
        name: 'Range',
        components: {
            addRange() {
    
            }
        },
        computed: {
            ranges() {
                return this.$store.state.range.ranges
            },
            name() {
                return this.$store.state.range.name
            },
            description() {
                return this.$store.state.range.description
            },
            expired () {
                return this.$store.state.range.expired
            }
    
        },
        created() {
    
        },
        methods: {
            changeName(e) {
                this.$store.commit('updateName', e.target.value)
            },
            changeDescription(e) {
                this.$store.commit('updateDesc', e.target.value)
            },
            changeExpired(e) {
                this.$store.commit('updateExp', e.target.value)
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
    
            }
        }
    }
</script>

<style scoped>
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
    
    .range-bet-rangeitem {
        display: flex;
        flex-flow: column;
        width: 20%;
        margin: 10px;
        height: 200px;
        border: 1px solid pink;
    }
    
    .save-button {
        display: flex;
        flex-flow: row;
        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
    }
</style>
