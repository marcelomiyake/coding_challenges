export class BST {
  value: number;

  left: BST | null;

  right: BST | null;

  constructor(value: number) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

export function findClosestValueInBst(tree: BST, target: number): number {
  if (target == tree.value) {
    return tree.value;
  } else if (target < tree.value && tree.left != null) {
    const leftTree = findClosestValueInBst(tree.left, target);
    if (Math.abs(target - leftTree) < Math.abs(target - tree.value)) {
      return leftTree;
    }
  } else if (tree.right != null) {
    const rightTree = findClosestValueInBst(tree.right, target);
    if (Math.abs(target - rightTree) < Math.abs(target - tree.value)) {
      return rightTree;
    }
  }
  return tree.value;
}
