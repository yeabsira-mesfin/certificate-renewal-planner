# Certificate Renewal Planner

I need a renewal calendar that assigns certificates to available maintenance days before their deadlines and explains which renewals cannot fit.

## Required decision command

`python certificate.py schedule INPUT.json` reads a raw JSON object as shown under input in examples/. Each certificate has a unique id, an inclusive earliest day and an inclusive deadline. Calendar days are integers from 1 through horizon. Process certificates by (deadline, id), taking the earliest day in the allowed range that is not blocked and still has capacity. Capacity is a daily nonnegative integer. Return an array in processing order with id and day (null if unscheduled). An earliest day after the deadline represents an empty window.

Print the JSON decision to stdout. For invalid input return nonzero and write a readable diagnostic to stderr. Use exact JSON types, including rejecting booleans where integers are required. Input ordering must not affect the result. Preserve the inventory CLI.

## Reporting and integration work

Add a calendar report listing each day, assigned ids and unused capacity; distinguish blocked, outside-horizon, empty-window and capacity-exhausted cases in a separate explanation. Include alternative-policy scenarios and demonstrate deterministic output after input shuffling. Document the reporting CLI, its input schema, one working example, and failure behavior. Exercise both success and failure paths through subprocess tests. Keep input files read-only. Use deterministic output and temporary paths for tests.

## Estimated implementation session

Allow 40 minutes for input modeling, 90 for the decision algorithm, 65 for the reporting feature, 50 for validation and edge cases, 60 for integration and regression tests, and 30 for documentation and reviewer evidence. Total estimate: 5 hours 35 minutes. Record actual time worked.
