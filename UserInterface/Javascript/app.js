/**
    app EmmeDomotica
    @Author SamuelFinocchioNJP
    Started: 15/04/2017
    Defines the front controllers
**/

var application = angular.module('EmmeDomotica', []);
application.constant('API', 'http://localhost:8000');
application.filter('capitalize', function() {
    return function(input) {
        if(input)
            return input.charAt(0).toUpperCase() + input.substr(1).toLowerCase();
        else
            return '';
    }
});

application.controller('homeController', function($scope, $http, API) {
    $scope.devices = {};
    $scope.getDevices = function() {
        $http.get(API + '/device/read').then(
            // Terminata la chiamata get

            // Se tutto ok
            function(response) {
                $scope.devices = response.data;
            },
            // Se c'è un errore
            function(response) {
                alert('Impossibile effettuare la chiamata alle api');
            })
    };

    $scope.getDevices();

});
