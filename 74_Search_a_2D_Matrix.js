/**
 * You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
// Old my version - Because miss info sort matrix
// class Node {
//     constructor(value) {
//         this.value = value;
//         this.left = null;
//         this.right = null;
//     }
// }

// var searchMatrix = function(matrix, target) {
//     graph = new Node(matrix[0][0]);
//     let current = graph;
//     for (let i = 0; i < matrix.length; i++) {
//         for (let j = 0; j < matrix[i].length; j++) {
//             if (i === 0 && j === 0) continue;
//             if (matrix[i][j] < current.value) {
//                 current.left = new Node(matrix[i][j]);
//                 current = current.left;
//             } else {
//                 current.right = new Node(matrix[i][j]);
//                 current = current.right;
//             }
//         }
//     }

//     while (graph) {
//         if (graph.value === target) return true;
//         if (graph.value > target) graph = graph.left;
//         else graph = graph.right;
//     }

//     return false;
// };

// Best version
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let [rows, cols] = [matrix.length, matrix[0].length];
    let [top, bot] = [0, rows-1];
    
    while(top <= bot){
        let row = Math.floor((top +  bot) / 2);
        if(target > matrix[row][cols-1]) {
            top = row + 1;
        } else if(target < matrix[row][0]) {
            bot = row - 1; 
        } else {
            break;
        }
    }
    
    if(!(top <= bot)) {
        return false;
    }
    
    let row = Math.floor((top + bot) / 2);
    let [left, right] = [0, cols - 1];

    while(left <= right){
        let mid = Math.floor((left + right) / 2);

        if(target > matrix[row][mid]) {
            left = mid + 1;
        } else if(target < matrix[row][mid]) {
            right = mid - 1;
        } else if(target == matrix[row][mid]) {
            return true;
        }
    }

    return false;    
};

const TestCase = require('./TestCase');
const test = new TestCase();

test.test_case([
    [() => searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), true],
    [() => searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), false],
    [() => searchMatrix([[1]], 1), true],
    [() => searchMatrix([[1, 3]], 3), true]
]);

