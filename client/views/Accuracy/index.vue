<template>
<div>
    <h1>Accuracy page</h1>
    <div class="range-bet-head-container">
            <label for="bet-name">Name of prediction:</label>
            <input name="bet-name" type="text" class="range-bet-head" :value="name" @input="changeName" placeholder="enter prediction name">
    </div>
    <div class="range-bet-description-container">
        <label for="bet-desc">Description:</label>
        <textarea name="bet-desc" type="text" class="range-bet-description" :value="description" @input="changeDescription" placeholder="enter prediction description" width="100%"></textarea>
    </div>
    <div class="range-bet-description-expired">
            <label for="bet-name">Expired</label>
            <input name="bet-name" type="text" class="range-bet-head" :value="expired" @input="changeExpired" placeholder="enter prediction name">
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
        name: 'Accuracy',
        components: {
            addRange() {
    
            }
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
            }
        },
        created() {
    
        },
        methods: {
           changeName(e) {
                this.$store.commit('updateNameAcc', e.target.value)
            },
            changeDescription(e) {
                this.$store.commit('updateDescAcc', e.target.value)
            },
            changeExpired(e) {
                this.$store.commit('updateExpAcc', e.target.value)
            },
        },
        data() {
            return {
    
            }
        }
    }
</script>

<style>
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
        margin-top: 100px;
    }
    
</style>
