/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        while (functions != undefined) {
            fn = functions.pop()
            if (fn === undefined)
                break
            x = fn(x)
        }
        return x
    }
};