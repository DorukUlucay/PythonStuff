gameApp.controller('workReportController', function($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://127.0.0.1:5000/getWorkTypes'
    })

    .then(function successCallback(response) {
        $scope.workTypes = response.data;
    }, function errorCallback(response) {
        $scope.message = response;
    });

    $scope.users = ['doruk', 'volkan', 'emir'];

    $scope.getSubtypes = function()
    {
      $http({
          method: 'POST',
          url: 'http://127.0.0.1:5000/getWorkSubTypes',
          data: JSON.stringify({parentId:$scope.workType})
      })

      .then(function successCallback(response) {
          $scope.workSubTypes = response.data;
      }, function errorCallback(response) {
          $scope.message = response;
      });
    };

});
