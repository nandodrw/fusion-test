<template>
  <div style="max-width: 1200px">
    <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="q-gutter-md"
      ref="personForm"
    >
      <q-input
        filled
        v-model="firstName"
        label="Person name"
        hint="Name and surname"
        lazy-rules
        :rules="[
          val => (val && val.length > 0) || 'Please type the first name'
        ]"
      />

      <q-input
        filled
        v-model="lastName"
        label="Person last name"
        lazy-rules
        :rules="[
          val => (val !== null && val !== '') || 'Please type the last name'
        ]"
      />

      <q-input filled v-model="birthDate" mask="date" :rules="[]">
        <template v-slot:append>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy
              ref="qDateProxy"
              transition-show="scale"
              transition-hide="scale"
            >
              <q-date
                v-model="birthDate"
                @input="() => $refs.qDateProxy.hide()"
              />
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>

      <div>
        <q-btn label="Create Person" type="submit" color="primary" />
      </div>
    </q-form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import People from '../store/people-module';
import { getModule } from 'vuex-module-decorators';
import Application from '../store/application-module';

@Component({
  name: 'PersonCreation'
})
export default class PersonCreation extends Vue {
  peopleStore = getModule(People, this.$store);
  appStore = getModule(Application, this.$store);

  firstName = '';
  lastName = '';
  birthDate = '';

  onSubmit() {
    if (!this.firstName || !this.lastName) return;

    this.appStore.ShowLoading();
    this.peopleStore.createPerson({
      firstName: this.firstName,
      lastName: this.lastName,
      birthDate: this.birthDate
    });

    this.firstName = '';
    this.lastName = '';
    this.birthDate = '';

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (this.$refs.personForm as any).resetValidation();
  }

  onReset() {}
}
</script>
