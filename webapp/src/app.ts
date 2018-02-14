import {Router, RouterConfiguration} from 'aurelia-router';
import {inject} from 'aurelia-framework';

export class App {
  router: Router;

  constructor() {}

  configureRouter(config: RouterConfiguration, router: Router) {
    config.title = 'Contacts';
    config.map([
      { route: '',      moduleId: 'pre-calculation',   title: 'Welcome to StreetCred'},
      { route: 'score', moduleId: 'score-detail', name:'score' }
    ]);

    this.router = router;
  }
}