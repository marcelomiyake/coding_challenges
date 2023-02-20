import {BinaryTree, nodeDepths} from "../../../src/binaryTrees/easy/NodeDepths"

describe('Node Depths', () => {
  test('Test Case 0', () => {
    const tree = new BinaryTree(1)
    tree.left = new BinaryTree(2)
    tree.left.left = new BinaryTree(4)
    tree.left.left.left = new BinaryTree(8)
    tree.left.left.right = new BinaryTree(9)
    tree.left.right = new BinaryTree(5)
    tree.right = new BinaryTree(3)
    tree.right.left = new BinaryTree(6)
    tree.right.right = new BinaryTree(7)

    const expected = 16

    expect(nodeDepths(tree)).toStrictEqual(expected)
  })
})
