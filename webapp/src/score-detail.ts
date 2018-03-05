import {HttpClient} from 'aurelia-fetch-client';

interface MetricScore {
  name: string;
  description: string;
  score: number;
}

let client = new HttpClient();

client.configure(config => {
  config
    .withBaseUrl('api/')
    .withDefaults({
      credentials: 'same-origin',
      headers: {
        'Accept': 'application/json',
        'X-Requested-With': 'Fetch'
      }
    });
});

export class ScoreDetail {
  metricScores: MetricScore[] = [];
  totalScore: number;

  activate() {
    return client.fetch('score')
      .then(response => response.json())
      .then(data => {
        data.result.metric_scores.forEach(element => {
          this.metricScores.push(element);
        });
        this.totalScore = data.result.score;
      });
  };
}
