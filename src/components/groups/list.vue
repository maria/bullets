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
  import ListingTable from '../../modules/listing-table.vue';
  import {apiURL} from '../../settings.js';

  export default {
    name: 'groups-list',

    components: {
      ListingTable
    },

    data() {
      return {
        groups: null,
        searchQuery: '',
        gridColumns: ['name'],
        gridData: []
      }
    },

    created() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        this.$http.get(`${apiURL}/groups`)
        .then((response) => {
          this.gridData = response.data;
        })
        .catch(() => {
          return 'Fetch failed';
        });
      }
    }
  }
</script>
