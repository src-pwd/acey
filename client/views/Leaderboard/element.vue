<template>
  <div class="leaderboard-element">
      <div class="leaderboard-number"> 
          <span class="big-number-create">{{id + 1 }}</span>
      </div>
      <div class="leaderboard-username"> 
          <span class="">{{details.user.username}}</span>
      </div>
      <div class="leaderboard-rate">
          <span class="">{{details.rate}}</span> 
      </div>
  </div>
  
</template>

<script>
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

 
    export default {
        props: {
            details: Object,
            id: Number
        }
    }

</script>