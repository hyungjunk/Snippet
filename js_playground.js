/**
 * Functional Programming fragment
 */
function curry(fn,arity = fn.length) {
  return (function nextCurried(prevArgs){
      return function curried(nextArg){
          var args = [ ...prevArgs, nextArg ];
          if (args.length >= arity) {
              return fn( ...args );
          }
          else {
              return nextCurried( args );
          }
      };
  })( [] );
}

/**
 * Functional Programming fragment
 */
const pipe = function(...fns) {
  return function(x) {
      return fns.reduce(function(v, f) {
          return f(v);
      }, x);
  }
};

/**
 * Functional Programming fragment
 */
const compose = function(...fns) {
  return function(x) {
      return fns.reduceRight(function(v, f) {
          return f(v);
      }, x);
  }
};
