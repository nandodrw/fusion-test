import { VuexModule, Module, Mutation } from 'vuex-module-decorators';
import { Loading } from 'quasar';

@Module({
  name: 'application',
  namespaced: true
})
export default class Application extends VuexModule {
  private showLoading = false;

  public get loading(): boolean {
    return this.showLoading;
  }

  @Mutation
  public hideLoading() {
    Loading.hide();
    this.showLoading = false;
  }

  @Mutation
  public ShowLoading() {
    Loading.show();
    this.showLoading = true;
  }
}
