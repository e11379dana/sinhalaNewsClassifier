SNCR_app.controller("commonController", function ($scope, $http, $filter) {


    $scope.getNews = function (category) { // Getting News Data from DB
        var url = 'http://127.0.0.1:5000/category/' + category;
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

    $scope.sendUserHistory = function (userId, articleId) {

        var data = {
            "UserId": userId,
            "ArticleId": articleId
        };
        var url = 'http://127.0.0.1:5000/userHistory';
        $http
            .post(url, data)
            .then(
                function (resp) {
                    console.log(data)
                },
                function (err) {
                    console.error(err);
                });
    }

});