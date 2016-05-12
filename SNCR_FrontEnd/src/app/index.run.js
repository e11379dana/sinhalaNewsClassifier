(function() {
  'use strict';

  angular
    .module('sncrFrontEnd')
    .run(runBlock);

  /** @ngInject */
  function runBlock($log) {

    $log.debug('runBlock end');
  }

})();
