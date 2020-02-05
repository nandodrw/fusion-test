<template>
  <div class="q-pa-md">
    <q-list bordered>
      <q-item v-for="method in listOfMethods" v-bind:key="method.id" clickable v-ripple>
        <q-item-section avatar>
          <q-icon v-if="method.type == 'email'" color="primary" name="mail" />
          <q-icon v-if="method.type == 'address'" color="primary" name="home" />
          <q-icon v-if="method.type == 'phone'" color="primary" name="phonelink_ring" />
        </q-item-section>
        <q-item-section>{{method.info}}</q-item-section>
        <q-item-section auto-width>
          <div class="btn-container">
            <q-btn
              size="sm"
              color="accent"
              dense
              @click="deleteMethod(method.id)"
              :icon="'delete_forever'"
            />
          </div>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<style lang="scss" scoped>
.btn-container {
  width: 25px;
  align-self: flex-end;
}
</style>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import { getModule } from 'vuex-module-decorators';
import People from '../store/people-module';
import Application from '../store/application-module';
import { ContactMap } from 'src/models/contact-map.model';

@Component({
  name: 'ContactMethods',
  props: ['methods', 'personId']
})
export default class ContactMethods extends Vue {
  @Prop(Map) readonly methods: ContactMap<string> | undefined;
  @Prop(Number) readonly personId: number | undefined;

  peopleStore = getModule(People, this.$store);
  appStore = getModule(Application, this.$store);

  tempVal = '';

  get listOfMethods() {
    // eslint-disable-next-line @typescript-eslint/no-angle-bracket-type-assertion
    if (this.methods && this.methods[this.personId || -1])
      return this.methods[this.personId || -1];
    return [];
  }

  deleteMethod(methodId: number) {
    this.peopleStore.deleteContactMethod({
      personId: this.personId || -1,
      methodId: methodId
    });
    this.appStore.ShowLoading();
  }
}
</script>