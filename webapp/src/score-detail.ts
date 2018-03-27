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
        data.result.category_scores.forEach(categoryScore => {
          categoryScore.metric_scores.forEach(metricScore => {
            this.metricScores.push(metricScore);
          });
        });
        this.totalScore = data.result.score;
      });
  };
}
