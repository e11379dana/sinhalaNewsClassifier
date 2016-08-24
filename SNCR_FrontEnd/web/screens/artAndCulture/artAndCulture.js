SNCR_app.controller("artAndCulture", function ($scope, $controller, $http, $filter) {



    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('art');

});