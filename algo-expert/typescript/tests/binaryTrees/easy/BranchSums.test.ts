import {BinaryTree, branchSums} from '../../../src/binaryTrees/easy/BranchSums'

describe('Branch Sums', () => {
  test('Test Case 0', () => {
    const tree = new BinaryTree(1)
    tree.left = new BinaryTree(2)
    tree.left.left = new BinaryTree(4)
    tree.left.left.left = new BinaryTree(8)
    tree.left.left.right = new BinaryTree(9)
    tree.left.right = new BinaryTree(5)
    tree.left.right.left = new BinaryTree(10)
    tree.right = new BinaryTree(3)
    tree.right.left = new BinaryTree(6)
    tree.right.right = new BinaryTree(7)

    const expected = [15, 16, 18, 10, 11]

    expect(branchSums(tree)).toStrictEqual(expected)
  })
})
