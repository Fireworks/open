var modal = angular.module('modal', []);

modal.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

modal.controller("RegisterCtrl", function RegisterCtrl($scope, $http){
    $scope.error = null;
    $scope.working = false;

    $scope.register = function(){
        $scope.error = null;
        $scope.working = true;
        $http({
            method: 'POST',
            url: "/register/",
            data: $.param({
                username: $scope.username,
                password1: $scope.password,
                password2: $scope.confirm,
                email: $scope.email}),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            location.reload();
        }).error(function(data){
            console.log(data);
            $scope.error = data.reason || 'error';
            $scope.working = false;
        });
    }
})