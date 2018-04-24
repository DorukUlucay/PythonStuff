gameApp.controller('loginController', function($scope, $http, $location) {

    $scope.login = function() {
        $http({
            method: 'POST',
            url: 'http://127.0.0.1:5000',
            data: JSON.stringify({
                username: $scope.username,
                password: $scope.password
            })
        }).then(function successCallback(response) {
            if (response.data.ok == "True") {
                $location.path("/overview");
            } else {
                $scope.message = response.data.message;
            }
        }, function errorCallback(response) {
            $scope.message = response.data.message;
        });
    }
});
