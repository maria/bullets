<template>
  <h1 class="uMB-30">Your groups</h1>
  <form id="search">
    <div class="form-group">
      <input name="query" v-model="searchQuery" class="form-control" placeholder="Search for a group">
    </div>
  </form>
  <listing-table
    :data="gridData"
    :columns="gridColumns"
    :filter-key="searchQuery">
  </listing-table>
</template>

<script>
  import ListingTable from '../../modules/listing-table.vue'
  import Settings from '../../settings.js'

  export default {
    name: 'groups-list',

    data() {
      return {
        groups: null,
        searchQuery: '',
        gridColumns: ['name'],
        gridData: []
      }
    },

    created: function () {
      this.fetchData()
    },

    components: {
      ListingTable
    },

    methods: {
      fetchData: function() {
        this.$http.get(Settings.apiURL + '/groups').then(
          function (response) {
            this.gridData = response.data;
          }, function (response) {
            this.gridData = [];
        });
      }
    }
  }
</script>
