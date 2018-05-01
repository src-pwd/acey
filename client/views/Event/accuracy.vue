<template>
  <div class="accuracy-control">
    <input type="number" min="0" v-model="currentValue">
    <div>
      <input v-model="currentValue" name="gdskill[2]" id="gdskill2" type="range" min="500" :max="1000" step="1" list="ticks" oninput="Output2.value = gdskill2.value" /><br />
      <output id="Output2" class="output"></output>
    </div>
  
    <datalist id="ticks">
        <option v-for="item in 1000" :value="item">{{item}}</option>
      </datalist>
      <div>
      <input class="betting-sum" v-model="sum"/><br />
    </div>
    <div class="row-block-button">
      <div><button @click="voteFor">voteeeeee</button></div>
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
          "event":  this.eventId,
          "bettor": this.username,
          "sum":    this.sum,
          "stake":  this.currentValue
        }
        this.$store.dispatch("accurateBet", payload).then(() => {
          this.$router.push('/dashboard')
        })
      }
    },
    data() {
      return {
        currentValue: 500,
        sum:0
      }
    }
  }
</script>

<style lang="scss">
  .output {
    width: 100%;
    margin-left: 50%;
  }
  
  input[type=range] {
    -webkit-appearance: none;
    /* Hides the slider so that custom slider can be made */
    height: 5px;
    width: 100%;
    cursor: pointer;
    background: #07C;
    margin-bottom: 10px;
  }
  
  input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    border: 2px solid #07C;
    height: 20px;
    width: 20px;
    border-radius: 20px;
    background: #fff;
    cursor: pointer;
    margin-top: 0px;
    /* You need to specify a margin in Chrome, but in Firefox and IE it is automatic */
  }
  
  input[type=range]:focus {
    outline: none;
  }
</style>