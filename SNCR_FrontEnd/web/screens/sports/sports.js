SNCR_app.controller("sports", function ($scope, $controller, $http, $filter) {



    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('sports');




});