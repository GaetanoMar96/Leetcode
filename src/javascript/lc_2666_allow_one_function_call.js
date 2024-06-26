/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let counter = 0
    return function(...args){
        if (counter != 0)
            return 
        counter++
        return fn(...args)
        
    }
};