# Certificate Renewal Planner

I need a renewal calendar that assigns certificates to available maintenance days before their deadlines and explains which renewals cannot fit.

The starter inventories synthetic records. Implement the decision command and reporting workflow described in [ASSIGNMENT.md](ASSIGNMENT.md). Use Python 3.10 or newer with the standard library.

```sh
python certificate.py inventory examples/horizon-2/deadline-1-capacity-0.json
python -m unittest discover -s tests -v
python acceptance.py --inventory
```

Example files contain input and expected results. The acceptance runner passes only the input to your implementation.
