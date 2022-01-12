/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const s = readline().split(" ");

// Write an answer using console.log()
// To debug: console.error('Debug messages...');
let r = "";
for (let i = 0; i < s.length; i++) {
    r+=s[i][0];
}
for (let i = s.length-1; i >= 0; i--) {
    r+=s[i][s[i].length-1];
}

console.log(r);
