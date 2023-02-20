import {Node} from '../../../src/graphs/easy/DepthFirstSearch'

describe('Depth-first Search', () => {
  test('Test Case 0', () => {
    const a = new Node('A')
    const b = a.addChild('B')
    const c = a.addChild('C')
    const d = a.addChild('D')
    const e = b.addChild('E')
    const f = b.addChild('F')
    const g = d.addChild('G')
    const h = d.addChild('H')
    const i = f.addChild('I')
    const j = f.addChild('J')
    const k = g.addChild('K')

    const expected = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
    expect(a.depthFirstSearch([])).toStrictEqual(expected)
  })
})
