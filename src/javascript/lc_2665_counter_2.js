/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let start = init
    return {
        increment: function() {
            init += 1
            return init
        },
        decrement: function() {
            init -= 1
            return init
        },
        reset: function() {
            init = start
            return init
        }
    }
};