gameApp.controller('moodController', function($scope, $http) {

    $scope.report = {
        mood: "",
        reason: ""
    };


    $http({
        method: 'GET',
        url: 'http://127.0.0.1:5000/getMoodTypes'
    })
    .then(function successCallback(response) {
        $scope.mood = response.data.data;
    }, function errorCallback(response) {
        $scope.message = response;
    });

    $scope.send = function()
    {
      $http({
          method: 'POST',
          url: 'http://127.0.0.1:5000/reportMood',
          data: JSON.stringify($scope.report)
      })
      .then(function successCallback(response) {
          $scope.message = "succesfully sent";
      }, function errorCallback(response) {
          $scope.message = response;
      });

    };
});
