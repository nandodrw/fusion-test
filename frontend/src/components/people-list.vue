<template>
  <div class="q-pa-lg">
    <PersonCreation></PersonCreation>
    <br />
    <br />
    <br />
    <q-table
      title="People List"
      :data="peopleStore.allPeople"
      :columns="columns"
      row-key="id"
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th auto-width />
          <q-th v-for="col in props.cols" :key="col.name" :props="props">{{
            col.label
          }}</q-th>
          <q-th auto-width />
        </q-tr>
      </template>

      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td auto-width>
            <q-btn
              size="sm"
              color="accent"
              round
              dense
              @click="expandRowDetail(props)"
              :icon="props.expand ? 'remove' : 'add'"
            />
          </q-td>
          <q-td v-for="col in props.cols" :key="col.name" :props="props">{{
            col.value
          }}</q-td>
          <q-td auto-width>
            <q-btn
              size="sm"
              color="accent"
              dense
              @click="deleteRecord(props)"
              :icon="'delete_forever'"
            />
          </q-td>
        </q-tr>
        <q-tr v-if="props.expand" :props="props">
          <q-td colspan="100%">
            <ContactMethods
              v-bind:personId="props.row.id"
              v-bind:methods="peopleStore.contactMethods"
            ></ContactMethods>
            <ContactMethodCreation
              v-bind:personId="props.row.id"
            ></ContactMethodCreation>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import { getModule } from 'vuex-module-decorators';
import People from '../store/people-module';
import Application from '../store/application-module';
import ContactMethods from './contact-methods.vue';
import PersonCreation from './person-creation.vue';
import ContactMethodCreation from './contact-method-creation.vue';
import { Person } from 'src/models/person.model';

@Component({
  name: 'PeopleList',
  components: {
    ContactMethods,
    PersonCreation,
    ContactMethodCreation
  }
})
export default class PeopleList extends Vue {
  peopleStore = getModule(People, this.$store);
  appStore = getModule(Application, this.$store);

  columns = [
    {
      name: 'FirstName',
      label: 'First Name',
      required: true,
      align: 'left',
      field: (row: Person) => row.firstName,
      format: (val: string) => {
        return `${val}`;
      },
      sortable: true
    },
    {
      name: 'LastName',
      label: 'Last Name',
      required: true,
      align: 'left',
      field: (row: Person) => row.lastName,
      format: (val: string) => {
        return `${val}`;
      },
      sortable: true
    },
    {
      name: 'BirthDate',
      label: 'Birth Date',
      required: false,
      align: 'left',
      field: (row: Person) => row.birthDate,
      format: (val: string) => `${val}`,
      sortable: true
    }
  ];

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  expandRowDetail(rowProp: any) {
    this.appStore.ShowLoading();
    this.peopleStore.fetchContactForPerson({
      personId: rowProp.row.id,
      callback: () => {
        rowProp.expand = !rowProp.expand;
      }
    });
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  deleteRecord(props: any) {
    this.appStore.ShowLoading();
    this.peopleStore.deletePerson(props.row.id);
  }
}
</script>
