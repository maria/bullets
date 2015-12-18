export function configRouter (router) {
  router.map({
    '/about': {
      component: require('./components/about.vue')
    },

    '/groups': {
      component: require('./components/groups/list.vue')
    },

    '/groups/:groupId': {
      component: require('./components/groups/item.vue'),
      subRoutes: {
        // matches /groups/:groupId/people
        'people': {
          component: require('./components/groups/item-people.vue')
        },

        // matches /groups/:groupId/passwords
        'passwords': {
          component: require('./components/groups/item-passwords.vue')
        }
      }
    }
  })
}
