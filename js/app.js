// (() => {
    var haystax = angular.module('haystaxApp', []);

    haystax.controller('MyController', function MyController($scope, $http) {

      $http.get('http://127.0.0.1/api/twitter_search.py')
          .then(function(response) {
              let ajaxRes = response.data.result;
              $scope.tweets = ajaxRes ? response.data.payload: [];
              // $scope.tweet = $scope.tweets[0];

        });
    });
// })();