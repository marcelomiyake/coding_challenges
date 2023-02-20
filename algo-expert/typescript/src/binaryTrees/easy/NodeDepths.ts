export function nodeDepths(root: BinaryTree, level = 0): number {
  let sum = 0;
  if (root.left !== null) {
    sum += nodeDepths(root.left, level + 1);
  }
  if (root.right !== null) {
    sum += nodeDepths(root.right, level + 1);
  }
  sum += level;
  return sum;
}

// This is the class of the input binary tree.
export class BinaryTree {
  value: number;
  left: BinaryTree | null;
  right: BinaryTree | null;

  constructor(value: number) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
