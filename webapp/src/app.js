define(["require", "exports", "bootstrap"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var App = (function () {
        function App() {
        }
        App.prototype.configureRouter = function (config, router) {
            config.title = 'StreetCred';
            config.map([
                { route: '', moduleId: 'pre-calculation', title: 'Welcome to StreetCred' },
                { route: 'score', moduleId: 'score-detail', name: 'score' }
            ]);
            this.router = router;
        };
        return App;
    }());
    exports.App = App;
});
//# sourceMappingURL=app.js.map