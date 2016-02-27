<template>
  <h1 class="uMB-30">Your groups</h1>
  <form id="search">
    <div class="form-group">
      <input name="query" v-model="searchQuery" class="form-control" placeholder="Search for a group">
    </div>
  </form>
  <listingtable
    :data="gridData"
    :columns="gridColumns"
    :filter-key="searchQuery">
  </listingtable>
</template>

<script>
  import listingtable from '../../modules/listing-table.vue'
  import settings from '../../settings.js'

  export default {
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
      listingtable
    },

    methods: {
      fetchData: function() {
        this.$http.get(settings.apiURL + '/groups').then(
          function (response) {
            this.gridData = response.data;
          }, function (response) {
            this.gridData = [];
        });
      }
    }
  }
</script>
