import fs from 'fs'
import path from 'path'

const dirname = import.meta.dirname
const input = fs.readFileSync(path.resolve(dirname, 'input.txt'), 'utf-8').split('\n')
let result = 0

const moves = input[0].split("")
const nodes_map = {}

for (const line of input.slice(2)) {
    const re = new RegExp("\\w+", 'g')
    const l = line.match(re)
    nodes_map[l[0]] = [l[1], l[2]]
}

let current = 'AAA'

while (current != 'ZZZ') {
    for (const move of moves) {
        const idx = move === 'L' ? 0 : 1
        current = nodes_map[current][idx];
        result++;
        if (current == 'ZZZ') {
            break;
        }
    }
}

console.log(result)

