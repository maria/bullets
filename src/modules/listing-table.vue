<style scoped>
  a {
    display: block;
    color: #E91E63;
    font-weight: bold;
    line-height: 2;
    padding: 0 10px;
  }

  a:hover {
    background-color: #E91E63;
    color: #FFF;
    text-decoration: none;
  }
</style>

<!-- component template -->
<template>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th v-for="key in columns"
            @click="sortBy(key)"
            :class="{active: sortKey == key}">
            {{key | capitalize}}
            <span class="arrow"
              :class="sortOrders[key] > 0 ? 'asc' : 'dsc'">
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for=" entry in data  | filterBy filterKey | orderBy sortKey sortOrders[sortKey]">
          <td v-for="key in columns">
            <a href="#">
              <i class="glyphicon glyphicon-chevron-right pull-right"></i>
              {{entry[key]}}
            </a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    replace: false,
    props: {
      data: Array,
      columns: Array,
      filterKey: String
    },
    data: function () {
      var sortOrders = {}
      this.columns.forEach(function (key) {
        sortOrders[key] = 1
      })
      return {
        sortKey: '',
        sortOrders: sortOrders
      }
    },
    methods: {
      sortBy: function (key) {
        this.sortKey = key
        this.sortOrders[key] = this.sortOrders[key] * -1
      }
    }
  }
</script>
