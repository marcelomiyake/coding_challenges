// This is the class of the input root.
// Do not edit it.
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

export function branchSums(root: BinaryTree): number[] {
  let result = [];
  if (root.left === null && root.right === null) {
    result.push(root.value)
  }
  if (root.left !== null) {
    root.left.value += root.value;
    result = result.concat(branchSums(root.left));
  }
  if (root.right !== null) {
    root.right.value += root.value;
    result = result.concat(branchSums(root.right));
  }

  return result;
}
