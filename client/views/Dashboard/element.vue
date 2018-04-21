<template>
     <router-link tag="div" :to="'event' + '/' + details.id + '/'" :id="details.id" class="dashboard-element-block">
          <div class="dashboard-element-text">
          <div class="dashboard-element-bg">
          <img src="dashboard_block.png">   
          </div>
              <div class="dashboard-element-text-name">{{ details.name }}</div>
              <div class="dashboard-element-text-desc">{{ details.description }}</div>
              <div class="dashboard-element-text-creator">by
              {{ details.creator }}</div>
              <div class="dashboard-element-text-type">type: {{ details.type }}</div>
              <div class="dashboard-element-text-expire">⏰ expires in {{details.expires}}</div>
          </div>
          <div class="dashboard-element-pic">
              
          </div>
      </router-link>
</template>

<script>
    
    export default {
        props: {
            details: Object,
         
        }
    }
    
</script>

<style lang="scss">
    .dashboard-element{
        &-bg {
            margin-left: -6px;
            width: 340px;
            height: 50px;
            & > img {
                max-width: 100%;
            }    
        }
        &-text-id {
            position: relative;
            left: 10px;
            font-size: 20px;
            top: -40px;
        }
        &-text-name {
            position: relative;
            top: -100px;
            color: #fff;
            padding-left: 15px;
            padding-right: 15px;
            margin-top: 70px;
            font-size: 22px;
        }
        &-text-desc {
            position: relative;
            top: -90px;
            padding-left: 15px;
            padding-right: 15px;
            font-size: 16px;
        }
        &-text-creator {
            color: #fff;
            position:relative;
            top:60px;
            left: 15px;
        }
        &-text-expire {
            margin-left: 15px;
            padding-left: 15px;
            border-radius: 15px;
            position: relative;
            border: 2px solid white;
            width: 180px;
            color: white;
               top: -110px;
        }
        &-text-type {
            padding-left: 15px;
        }
    }
</style>


// curl -H "Content-Type: application/json" -d '{"creator":"andrey_shishkin", "name":"POT Price", "type": "Parley", "expired": "2021-02-02T00:58:00+02:00", "description": "EOS price would reach 9k before may", "currency_pair": "POT/BTC", "exchange": "Bittrex"}' -X POST http://127.0.0.1:8000/api/events/
