import {findClosestValueInBst, BST} from '../../../src/binarySearchTrees/easy/FindClosestValueInBST'

describe('Find Closest Value in BST', () => {
  test('Test Case 0', () => {
    const tree = new BST(10)
    tree.left = new BST(5)
    tree.left.left = new BST(2)
    tree.left.left.left = new BST(1)
    tree.left.right = new BST(5)
    tree.right = new BST(15)
    tree.right.left = new BST(13)
    tree.right.left.right = new BST(14)
    tree.right.right = new BST(22)
    const target = 12

    const expected = 13

    expect(findClosestValueInBst(tree, target)).toBe(expected)
  })
})
