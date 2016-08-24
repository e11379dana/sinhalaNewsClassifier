SNCR_app.controller("buisenessAndEconomics", function ($scope, $controller, $http, $filter) {

    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('buiseness');

});