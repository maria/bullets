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
  const apiURL = '';

  import listingtable from '../../modules/listing-table.vue'

  export default {
    data() {
      return {
        groups: null,
        searchQuery: '',
        gridColumns: ['name'],
        gridData: [
          { name: 'Chuck Norris' },
          { name: 'Bruce Lee' },
          { name: 'Jackie Chan' },
          { name: 'Jet Li' }
        ]
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
        var xhr = new XMLHttpRequest()
        var self = this
        xhr.open('GET', apiURL + self.currentBranch)
        xhr.onload = function () {
          self.groups = JSON.parse(xhr.responseText)
        }
        xhr.send()
      }
    }
  }
</script>
