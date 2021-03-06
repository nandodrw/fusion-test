import Vue from 'vue';
import Vuex from 'vuex';
import application from './application-module';
import people from './people-module';

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function(/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      application,
      people
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    strict: (process as any).env.DEV
  });

  return Store;
}
