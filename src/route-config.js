export function configRouter (router) {
  router.map({
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
