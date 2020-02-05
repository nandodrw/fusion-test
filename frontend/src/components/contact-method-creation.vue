<template>
  <div class="q-pa-md" style="max-width: 400px">
    <q-form @submit="onSubmit" class="q-gutter-md" ref="contactMethodForm">
      <q-input
        filled
        v-model="data"
        label="Contact Information"
        hint="e.g. +1 786 987 888"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type the first name']"
      />

      <q-select
        v-model="selectedMethod"
        :options="peopleStore.contactMethodTypesList"
        :option-value="(item) => item === null ? null : item.id"
        :option-label="(item) => item === null ? 'Null value' : item.desc"
        label="Standard"
      />

      <div>
        <q-btn label="Add contact method" type="submit" color="primary" />
      </div>
    </q-form>
  </div>
</template>

<script lang="ts">
import People from '../store/people-module';
import { getModule } from 'vuex-module-decorators';
import Application from '../store/application-module';
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component({
  name: 'ContactMethodCreation'
})
export default class ContactMethodCreation extends Vue {
  @Prop(Number) readonly personId: number | undefined;

  peopleStore = getModule(People, this.$store);
  appStore = getModule(Application, this.$store);

  data = '';
  selectedMethod: {
    id?: number;
  } = {};

  async onSubmit() {
    if (!this.data || !this.selectedMethod) return;
    this.appStore.ShowLoading();
    await this.peopleStore.addContactMethod({
      personId: this.personId || 0,
      methodId: this.selectedMethod.id,
      info: this.data
    });
    this.data = '';
    this.selectedMethod = {};
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (this.$refs.contactMethodForm as any).resetValidation();
  }
}
</script>