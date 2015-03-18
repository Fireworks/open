var modal = angular.module('modal', []);

modal.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

modal.controller("RegisterCtrl", function RegisterCtrl($scope, $http){
    $scope.errors = null;
    $scope.working = false;

    $scope.register = function(){
        $scope.errors = null;
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
            $scope.errors = data;
            $scope.working = false;
        });
    }
});

modal.controller("SigninCtrl", function SigninCtrl($scope, $http){
    console.log("test");
    $scope.error = false;

    $scope.signin = function(){
        $scope.error = false;
        $http({
            method: 'POST',
            url: "/signin/",
            data: $.param({
                username: $scope.username,
                password: $scope.password
            }),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data){
            location.reload();
        }).error(function(data){
            $scope.error = true;
        });
    }
});