(() => {

    const haystax = angular.module('haystaxApp', []);

    haystax.controller('MyController', ($scope, $http) => {

        // Change this API endpoint according to your own backend.
        // Mine is deployed on a Google Cloud instance, but your endpoint URL will be different.
        let apiEndpoint = 'http://35.227.108.253/api/twitter_search.py';

        $http.get(apiEndpoint).then(
            response => {
                let ajaxRes = response.data.result;
                $scope.tweets = ajaxRes ? response.data.payload : [];
            }
        );

        $scope.submitSearch = keyEvent => {
            if (keyEvent.which === 13) {
                let payloadData = JSON.stringify({username: $scope.searchQuery});
                $http.post(apiEndpoint, payloadData).then(
                    response => {
                        let ajaxRes = response.data.result;
                        $scope.tweets = ajaxRes ? response.data.payload: [];
                        let twitterTimeline = angular.element(document.querySelector('.twitter-timeline'));
                        twitterTimeline.replaceWith(`<a class="twitter-timeline" data-width="420" data-height="760" data-theme="light" data-link-color="#FAB81E" href="https://twitter.com/${$scope.searchQuery}">Tweets by ${$scope.searchQuery}</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>`);
                    }
                );
            }
        };

    });
})();
