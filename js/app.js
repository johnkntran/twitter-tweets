(() => {

    const haystax = angular.module('haystaxApp', []);

    haystax.controller('MyController', ($scope, $http) => {

        // Change this API endpoint according to your own backend.
        // Mine is deployed on a Google Cloud instance, but your endpoint URL will be different.
        const apiEndpoint = 'http://35.196.93.111/api/twitter_search.py';

        $http.get(apiEndpoint).then(
            response => {
                let ajaxRes = response.data.result;
                $scope.tweets = ajaxRes ? response.data.payload : [];
                makeChart();
            }
        );

        $scope.submitSearch = keyEvent => {
            if (keyEvent.which === 13) {
                let payloadData = JSON.stringify({username: $scope.searchQuery});
                $http.post(apiEndpoint, payloadData).then(
                    response => {
                        let ajaxRes = response.data.result;
                        $scope.tweets = ajaxRes ? response.data.payload: [];
                        makeChart();
                        let twitterTimeline = angular.element(document.querySelector('.twitter-timeline'));
                        twitterTimeline.replaceWith(`<a class="twitter-timeline" data-width="420" data-height="760" data-theme="light" data-link-color="#FAB81E" href="https://twitter.com/${$scope.searchQuery}">Tweets by ${$scope.searchQuery}</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>`);
                    }
                );
            }
        };

        const makeChart = () => {
            let num_words = $scope.tweets.map(twt => twt.num_words);
            let dates = $scope.tweets.map(twt => twt.time);
            let context = document.getElementById("tweetGraph").getContext("2d");
            let chart = new Chart(context, {
                type: "line",
                data: {
                    labels: [1,2,3,4,5,6].map(num => "#" + num),
                    datasets: [{
                        label: "",
                        backgroundColor: "rgb(43, 196, 79)",
                        borderColor: "rgb(71, 171, 94)",
                        data: num_words,
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
                    title:{
                        display:true,
                        text:"Total Words per Tweet over Time"
                    },
                    tooltips: {
                        mode: "index",
                        intersect: false,
                    },
                    hover: {
                        mode: "nearest",
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: "Tweets"
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: "Words"
                            },
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
            });
        }
    });
})();
