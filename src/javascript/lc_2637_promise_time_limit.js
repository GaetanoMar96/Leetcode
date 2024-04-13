/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        return new Promise((resolve, reject) => {
            fn(...args)
            .then(result => resolve(result)) 
            .catch(error => reject(error));
            
            setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
            })
    }
};