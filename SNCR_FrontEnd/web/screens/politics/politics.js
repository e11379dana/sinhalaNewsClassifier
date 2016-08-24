SNCR_app.controller("politics", function ($scope, $controller, $http, $filter) {



    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('politics');


});