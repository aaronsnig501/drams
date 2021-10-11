import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _c9c9ff5c = () => interopDefault(import('../pages/blog/index.vue' /* webpackChunkName: "pages/blog/index" */))
const _1a5dc706 = () => interopDefault(import('../pages/inspire.vue' /* webpackChunkName: "pages/inspire" */))
const _468856aa = () => interopDefault(import('../pages/whiskey/index.vue' /* webpackChunkName: "pages/whiskey/index" */))
const _4485f868 = () => interopDefault(import('../pages/accounts/create.vue' /* webpackChunkName: "pages/accounts/create" */))
const _4674982d = () => interopDefault(import('../pages/accounts/login.vue' /* webpackChunkName: "pages/accounts/login" */))
const _9b926d58 = () => interopDefault(import('../pages/whiskey/create.vue' /* webpackChunkName: "pages/whiskey/create" */))
const _cd3741ec = () => interopDefault(import('../pages/blog/_slug.vue' /* webpackChunkName: "pages/blog/_slug" */))
const _02affb92 = () => interopDefault(import('../pages/whiskey/_id.vue' /* webpackChunkName: "pages/whiskey/_id" */))
const _cbd0c596 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/blog",
    component: _c9c9ff5c,
    name: "blog"
  }, {
    path: "/inspire",
    component: _1a5dc706,
    name: "inspire"
  }, {
    path: "/whiskey",
    component: _468856aa,
    name: "whiskey"
  }, {
    path: "/accounts/create",
    component: _4485f868,
    name: "accounts-create"
  }, {
    path: "/accounts/login",
    component: _4674982d,
    name: "accounts-login"
  }, {
    path: "/whiskey/create",
    component: _9b926d58,
    name: "whiskey-create"
  }, {
    path: "/blog/:slug",
    component: _cd3741ec,
    name: "blog-slug"
  }, {
    path: "/whiskey/:id",
    component: _02affb92,
    name: "whiskey-id"
  }, {
    path: "/",
    component: _cbd0c596,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
