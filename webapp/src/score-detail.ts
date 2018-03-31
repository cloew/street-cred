import {HttpClient} from 'aurelia-fetch-client';

interface MetricScore {
  name: string;
  description: string;
  score: number;
}

interface CategoryScore {
  name: string;
  description: string;
  score: number;
  metric_scores: MetricScore[];
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
  categoryScores: CategoryScore[] = [];
  metricScores: MetricScore[] = [];
  totalScore: number;

  activate() {
    return client.fetch('score')
      .then(response => response.json())
      .then(data => {
        this.categoryScores = data.result.category_scores;
        this.totalScore = data.result.score;
      });
  };
}
