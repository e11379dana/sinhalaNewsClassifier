SNCR_app.controller("defenseAndLaw", function ($scope, $controller, $http, $filter) {



    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('defence');

});