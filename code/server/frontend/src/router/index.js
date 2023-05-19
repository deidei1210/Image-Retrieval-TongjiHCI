import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "search",
            component: () => import("@/views/Search.vue"),
        },
        {
            path: "/collect",
            name: "collect",
            component: () => import("@/views/Collection.vue"),
        }
    ]
});
