<template>
    <div>
        <div>Event #{{ this.$store.state.route.params.id }}</div>
        <div class="event-info">
            <p>Event name :{{ currentEvent.name }}</p>
            <p>Event description: {{ currentEvent.description }}</p>
            <p>Expired date: {{ currentEvent.ends }}</p>
        </div>
        <div class="event-control-vote">
            <div class="event-choose-control-range" v-if="currentEvent.type == 'range'">
                <p>Choose range:</p>
                <div v-for="item in options" class="range-choose">
                    <p>{{ item.name }}</p>
                    <p>{{ item.priceFrom }}</p>
                    <p>{{ item.priceTo }}</p>
                </div>
            </div>
            <div class="event-choose-control-accuracy" v-else>
                <input type="number" class="event-choose-control-accuracy-input" style="width: 50%;" placeholder="Enter specific price value:">
            </div>
        </div>
        <div>
            <button></button>
        </div>
        <router-link to="/play" tag="button">
            PLAY DASHBOARD
        </router-link>
    </div>
</template>

<script>
    import {
        mapGetters
    } from 'vuex'
    export default {
        name: 'Event',
    
        computed: {
            ...mapGetters([
                'currentEvent',
            ]),
            routerID() {
                return this.$store.state.route.params.id
            },
            options() {
                return this.$store.state.event.options ? this.$store.state.event.options : ''
            }
        }
    }
</script>

<style>
    .range-choose {
        display: block;
        flex-flow: column;
        padding: 50px;
        margin: 50px;
        border: 1px solid pink;
    }
    
    .event-choose-control-range {
        display: flex;
        flex-flow: row;
    }
    
    .event-choose-control-accuracy-input {
        margin: 100px;
        font-size: 50px;
        text-align: center;
    }
</style>
