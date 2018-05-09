<template>
    <router-link tag="div"  :to="'event' + '/' + details.id + '/'" :id="details.id" class="dashboard-element-block">
        <div class="top-block">
            <div class="pair">{{ details.currency_pair }}</div>
            <div class="exchange">at {{ details.exchange }}</div>
            <div class="type">{{ predictionType }}</div>
        </div>
        <div class="main-block-content">
            <div class="name">{{ details.name }}</div>
            <div class="description">{{ details.description }}</div>
            <div class="expired">⏰ in {{ expiredDay }} days</div>
        </div>
        <div class="bottom-block">
            <div class="block-icon users-voted"><span><font-awesome-icon :icon="sum" /></span>   {{ details.total_sum }} ACEY</div>
            <br>
            <div class="block-icon total-used"><span><font-awesome-icon :icon="user" /></span>{{ details.total_users }}</div>
        </div>
        
    </router-link>
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import { faUser } from '@fortawesome/fontawesome-free-solid'
import { faDatabase } from '@fortawesome/fontawesome-free-solid'

 
    export default {
        components: {
            FontAwesomeIcon
        },
        props: {
            details: Object,
        },
        computed: {
            expiredDay() {
                let oneDay = 24 * 60 * 60 * 1000;
                let firstDate = new Date(this.details.expired) || ''
                let secondDate = new Date(this.details.created) || ''
                return Math.round(Math.abs((firstDate.getTime() - secondDate.getTime()) / (oneDay)));
            },
            predictionType() {
                switch (this.details.type) {
                    case "Prediction":
                        return "Interval"
                    case "AccuratePrediction":
                        return "Accurate price"
                    case "Parlay":
                        return "Parlay"
                }
            },
            sum() {
                return faDatabase
            },
            user() {
                return faUser
            },
           
    icon () {
      return faCoffee
    },
            
        },
        mounted() {
        },
        data() {
            return {

            }
        },
        
    }

</script>