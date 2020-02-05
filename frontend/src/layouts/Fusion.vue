<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>Fusion Test</q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import { getModule } from 'vuex-module-decorators';
import Application from '../store/application-module';

@Component({
  name: 'FusionLayout'
})
export default class FusionLayout extends Vue {
  store = getModule(Application, this.$store);
}
</script>
