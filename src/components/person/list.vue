<template>
  <h1>Persons</h1>
  <div id="demo">
  <form id="search">
    <div class="form-group">
      <input name="query" v-model="searchQuery" class="form-control" placeholder="Search for a person">
    </div>
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
  import settings from '../../settings.js'

  export default {
    data() {
      return {
        searchQuery: '',
        gridColumns: ['name', 'email', 'groups'],
        gridData: []
      }
    },

    components: {
      listingtable
    },

    methods: {
      fetchData: function() {
        this.$http.get(settings.apiURL + '/person/').then(
          function (response) {
            this.gridData = response.data;
          }, function (response) {
            this.gridData = [];
        });
    }
    }
  }
</script>
