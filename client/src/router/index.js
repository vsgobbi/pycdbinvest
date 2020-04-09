import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Teste from "../components/Teste.vue";
import History from "../components/History.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/",
    name: "History",
    component: History
  },
  {
    path: "/api/v1",
    name: "Teste",
    component: Teste
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
