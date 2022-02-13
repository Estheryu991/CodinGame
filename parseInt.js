
const N = parseInt(readline());
const M = parseInt(readline());

let minvariance = Number.POSITIVE_INFINITY
//represents the positive Infinity value.

let minvarianceidx = -1
//stdin and console are just local variable names.

for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ').map(c=>+c);
    let mean = inputs.reduce((p,c)=>p+c,0)/inputs.length
    let variance = inputs.reduce((p,c)=>p+((c-mean)**2),0)
    if (variance<minvariance) {
        minvariance = variance
        minvarianceidx = i+1
    }
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');

console.log(minvarianceidx);
