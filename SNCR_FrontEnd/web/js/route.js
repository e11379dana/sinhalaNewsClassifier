var SNCR_app = angular.module('sncrSystem', ['ngRoute']);

SNCR_app.config(function ($routeProvider) {

    $routeProvider

        .when('/hotNews', {
        templateUrl: 'screens/hotNews/hotNews.html',
        controller: 'hotNews'
    })

    .when('/artAndCulture', {
        templateUrl: 'screens/artAndCulture/artAndCulture.html',
        controller: 'artAndCulture'
    })

    .when('/buisenessAndEconomics', {
        templateUrl: 'screens/buisenessAndEconomics/buisenessAndEconomics.html',
        controller: 'buisenessAndEconomics'
    })

    .when('/defenseAndLaw', {
        templateUrl: 'screens/defenseAndLaw/defenseAndLaw.html',
        controller: 'defenseAndLaw'
    })

    .when('/politics', {
        templateUrl: 'screens/politics/politics.html',
        controller: 'politics'
    })

    .when('/sports', {
        templateUrl: 'screens/sports/sports.html',
        controller: 'sports'
    })

    .when('/', {
        templateUrl: 'screens/hotNews/hotNews.html',
        controller: 'hotNews'
    })


});