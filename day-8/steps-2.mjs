import fs from 'fs'
import path from 'path'


const dirname = import.meta.dirname
const input = fs.readFileSync(path.resolve(dirname, 'input.txt'), 'utf-8').split('\n')
let s = 1

const moves = input[0].split("")
const nodes_map = {}

for (const line of input.slice(2)) {
    const re = new RegExp("\\w+", 'g')
    const l = line.match(re)
    nodes_map[l[0]] = [l[1], l[2]]
}

function lcm(...numbers) {
    return numbers.reduce((a, b) => a * b / gcd(a, b));
}

function gcd(...numbers) {
    return numbers.reduce((a, b) => {
        while (b) {
            let t = b;
            b = a % b;
            a = t;
        }
        return a;
    });
}

const current = []
const result = [0, 0, 0, 0, 0, 0]

for (const key of Object.keys(nodes_map)) {
    if (key.at(-1) === 'A') {
        current.push(key)
    }
}


for (let i = 0; i < current.length; i++){
    while (!current[i].endsWith('Z')) {
        for (const move of moves) {
            const idx = move === 'L' ? 0 : 1;
            current[i] = nodes_map[current[i]][idx];
            result[i]++;
            if (current[i].endsWith('Z')) break;
        }
    }
}

console.log(lcm(...result))

