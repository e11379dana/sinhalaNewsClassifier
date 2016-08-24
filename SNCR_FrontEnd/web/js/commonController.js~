SNCR_app.controller("commonController", function ($scope, $http, $filter) {


    $scope.getNews = function (category) { // Getting News Data from DB
        var url = 'localhost:5000/' + category;
        $http
            .get(url)
            .then(function (resp) {
                    $scope.items = resp.data;
                    console.log($scope.items);
                },
                function (err) {
                    console.log('Item request ERR ' + err);
                })
    };
    console.log("common is running");

});