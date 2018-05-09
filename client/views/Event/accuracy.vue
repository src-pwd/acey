<template>
  <div class="accuracy-control">
    <input class="accuracy-easy" type="number" min="0" v-model="currentValue">
    <div>
      <input v-model="currentValue" name="gdskill[2]" id="gdskill2" type="range" min="0" :max="10000" step="1" list="ticks" oninput="Output2.value = gdskill2.value" /><br />
      <!--<output id="Output2" class="output"></output> -->
    </div>
  
    <datalist id="ticks">
              <option v-for="item in 1000" :value="item">{{item}}</option>
            </datalist>
    <div class="range-items-pay">
      <label class="range-items-pay-label">
              Your investment
             </label>
      <br>
      <input class="range-items-pay-input" v-model="sum" placeholder="your investment" />
      <span class="range-items-pay-currency"> ACEY</span>
    </div>
     <div class="row-block-button">
            <div><button class="vote-range-button" @click="voteFor">vote</button></div>
        </div>
  </div>
</template>

<script>
  export default {
    computed: {
      eventId() {
        return this.$route.params.id
      },
      username() {
        return this.$store.state.auth.username
      }
    },
    methods: {
      voteFor() {
        var payload = {
          "event": this.eventId,
          "bettor": this.username,
          "sum": this.sum,
          "stake": this.currentValue
        }
        this.$store.dispatch("accurateBet", payload).then(() => {
          this.$router.push('/dashboard')
        })
      }
    },
    data() {
      return {
        currentValue: 500,
        sum: 0
      }
    }
  }
</script>
