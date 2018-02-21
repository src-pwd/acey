<template>
  <div>
    <h1>Play page</h1>
    <div class="events">
    <router-link :to="`/event/${item.id}`" :key="item" tag="div" :item="item"  v-for="(item, key) in events" class="event-block-outer">
      <p>{{ item.name }}</p>
      <p>{{ item.description }}</p>
      <p>{{ item.peoplesVoted }}</p>
      <p>{{ item.aceyVoted }}</p>
      <p>{{ item.ends }}</p>
      <p>{{ item.type }}</p>
    </router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Play',
    components: {
  
    },
    computed: {
      events() {
        return this.$store.state.eventsDashboard.events
      },
    }
  
  }
</script>

<style>
  .events {
    display: flex;
    flex-flow: row;
    flex-wrap: nowrap;
  }
  .event-block-outer {
    width: 200px;
    height: 300px;
    display: flex;
    margin: 20px;
    flex-flow: column;
    border: 1px solid pink;
  }
</style>
