var gameApp = angular.module('gameApp', ['ngRoute']);

gameApp.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl : 'views/login.html',
            controller  : 'loginController'
        })

    $routeProvider
            .when('/actions', {
                templateUrl : 'views/actions.html',
                controller  : 'workReportController'
            })

            $routeProvider
                    .when('/mood', {
                        templateUrl : 'views/mood.html',
                        controller  : 'moodController'
                    })


                    $routeProvider
                            .when('/overview', {
                                templateUrl : 'views/overview.html',
                                controller  : 'overviewController'
                            })
});
