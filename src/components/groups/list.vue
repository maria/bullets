<template>
  <h1>Your groups</h1>
  <div id="demo">
  <form id="search">
    Search <input name="query" v-model="searchQuery">
  </form>
  <listingtable
    :data="gridData"
    :columns="gridColumns"
    :filter-key="searchQuery">
  </listingtable>
</div>
</template>

<script>
  import listingtable from '../../modules/listing-table.vue'

  export default {
    data() {
      return {
        searchQuery: '',
        gridColumns: ['name', 'power'],
        gridData: [
          { name: 'Chuck Norris', power: Infinity },
          { name: 'Bruce Lee', power: 9000 },
          { name: 'Jackie Chan', power: 7000 },
          { name: 'Jet Li', power: 8000 }
        ]
      }
    },

    components: {
      listingtable
    }
  }
</script>
