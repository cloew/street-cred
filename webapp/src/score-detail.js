define(["require", "exports", "aurelia-fetch-client"], function (require, exports, aurelia_fetch_client_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var client = new aurelia_fetch_client_1.HttpClient();
    client.configure(function (config) {
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
    var ScoreDetail = (function () {
        function ScoreDetail() {
            this.categoryScores = [];
            this.metricScores = [];
        }
        ScoreDetail.prototype.activate = function () {
            var _this = this;
            return client.fetch('score')
                .then(function (response) { return response.json(); })
                .then(function (data) {
                _this.categoryScores = data.result.category_scores;
                _this.totalScore = data.result.score;
            });
        };
        ;
        return ScoreDetail;
    }());
    exports.ScoreDetail = ScoreDetail;
});
//# sourceMappingURL=score-detail.js.map