/* eslint-disable @typescript-eslint/camelcase */
import { VuexModule, Module, Mutation, Action } from 'vuex-module-decorators';
import axios from 'axios';
import { Person } from 'src/models/person.model';
import { ContactMethodType } from 'src/models/contact-method-type.model';
import { ContactMap } from 'src/models/contact-map.model';

const API_ENDPOINT = 'https://fusion-test-fernando.herokuapp.com';

@Module({
  name: 'people',
  namespaced: true
})
export default class People extends VuexModule {
  private people: Person[] = [];
  private contactMap: ContactMap<string> = {};
  private contactMethodTypes: ContactMethodType[] = [];

  public get allPeople() {
    return this.people;
  }

  public get contactMethods() {
    return this.contactMap;
  }

  public get contactMethodTypesList() {
    return this.contactMethodTypes;
  }

  @Mutation
  private setPeople(people: Person[]) {
    this.people = people;
  }

  @Mutation
  private setContactInfoForPerson({
    contactInfo,
    personId
  }: {
    contactInfo: string;
    personId: number;
  }) {
    const template = Object.assign({}, this.contactMap);
    template[personId] = contactInfo;
    this.contactMap = template;
  }

  @Mutation
  private setContactMethods(types: ContactMethodType[]) {
    this.contactMethodTypes = types;
  }

  @Action
  public async fetchPeople() {
    const response = await axios.get(`${API_ENDPOINT}/api/people`);
    this.setPeople(
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      response.data.map((raw: any) => {
        return {
          firstName: raw.first_name,
          lastName: raw.last_name,
          birthDate: raw.date_of_birth,
          id: raw.id
        };
      })
    );
    this.context.commit('application/hideLoading', null, { root: true });
  }

  @Action
  public async fetchContactMethodTypes() {
    const response = await axios.get(`${API_ENDPOINT}/api/contact-type`);
    this.setContactMethods(response.data);
  }

  @Action
  public async fetchContactForPerson({
    personId,
    callback
  }: {
    personId: number;
    callback: Function;
  }) {
    const response = await axios.get(
      `${API_ENDPOINT}/api/people/${personId}/contact`
    );
    this.setContactInfoForPerson({
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      contactInfo: response.data.map((raw: any) => {
        const methodType = this.contactMethodTypes.find(
          ct => ct.id === raw.type
        );
        return {
          info: raw.info,
          type: methodType ? methodType.desc : '',
          id: raw.id
        };
      }),
      personId
    });
    this.context.commit('application/hideLoading', null, { root: true });
    if (callback) {
      callback();
    }
  }

  @Action
  public async createPerson(payload: {
    firstName: string;
    lastName: string;
    birthDate: string;
  }) {
    await axios.post(`${API_ENDPOINT}/api/people`, payload);
    this.fetchPeople();
  }

  @Action
  public async deletePerson(personId: number) {
    await axios.delete(`${API_ENDPOINT}/api/people/${personId}`);
    this.fetchPeople();
  }

  @Action
  public async addContactMethod({
    personId,
    methodId,
    info
  }: {
    personId: number;
    methodId?: number;
    info: string;
  }) {
    await axios.post(`${API_ENDPOINT}/api/people/${personId}/contact`, {
      typeId: methodId,
      info
    });
    this.fetchContactForPerson({ personId, callback: () => {} });
  }

  @Action
  public async deleteContactMethod({
    personId,
    methodId
  }: {
    personId: number;
    methodId: number;
  }) {
    await axios.delete(
      `${API_ENDPOINT}/api/people/${personId}/contact/${methodId}`
    );
    this.fetchContactForPerson({ personId, callback: () => {} });
  }
}
