test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose([below_3_r, above_3_r], [0.290189526493, 0.372782225571])
          True
          >>> [len(below_3), len(above_3)]
          [97, 175]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
