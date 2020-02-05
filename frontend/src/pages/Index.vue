<template>
  <q-page class="flex flex-center">
    <PeopleList></PeopleList>
  </q-page>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import { getModule } from 'vuex-module-decorators';
import People from '../store/people-module';
import Application from '../store/application-module';
import PeopleList from '../components/people-list.vue';

@Component({
  name: 'PageIndex',
  components: {
    PeopleList
  }
})
export default class MainPage extends Vue {
  peopleStore = getModule(People, this.$store);
  appStore = getModule(Application, this.$store);

  mounted() {
    this.appStore.ShowLoading();
    this.peopleStore.fetchPeople();
    this.peopleStore.fetchContactMethodTypes();
  }
}
</script>
