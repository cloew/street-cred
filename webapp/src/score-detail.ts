import {HttpClient} from 'aurelia-fetch-client';

interface MetricScore {
  name: string;
  description: string;
  score: number;
}

let metricScoreFoo = {name: "foo_name", description: "foo_desc", score: 123};
let metricScoreBar = {name: "bar_name", description: "bar_desc", score: 456};
let metricScoreBaz = {name: "baz_name", description: "baz_desc", score: 789};

let client = new HttpClient();

/*
client.configure(config => {
  config
    .withDefaults({
      credentials: 'include',
      headers: {
        'Accept': 'application/json',
        'X-Requested-With/#/score': 'Fetch'
      }
    });
});
*/

export class ScoreDetail {
  metricScores: MetricScore[] = [metricScoreFoo, metricScoreBar, metricScoreBaz];
  singleMetric = metricScoreFoo;
}
