/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let map = {}
    return function(...args) {
        if (map[args] !== undefined)
            return map[args]
        let res = fn(...args)
        map[args] = res
        return res
    }
}
