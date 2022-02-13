const n = parseInt(readline());
const position = readline();
let idx;
for (let i = 0; i < position.length; i++) {
    if (position[i] === '#') {
        idx = i
    }
}
let coutintervals = 0
for (let i = 0; i < n; i++) {
    let startidx;
    let startinclusive
    let endidx;
    let endinclusive
    const interval = readline();
    for (let j = 0; j < interval.length; j++) {
        if (interval[j] === ']' || interval[j]==='[') {
            if (startidx === undefined) {
                startidx = j;
                startinclusive = interval[j]==='['
            } else {
                endidx = j;
                endinclusive = interval[j]===']'
            }
        }
    }
    console.error(idx)
    if (idx >= startidx && idx <=endidx) {
        if (idx !== startidx && idx !== endidx) {
            coutintervals++
        } else if (idx === startidx && startinclusive) {
            coutintervals++
        } else if (idx === endidx && endinclusive) {
            coutintervals++
        }
    }
}
 

console.log(coutintervals);
