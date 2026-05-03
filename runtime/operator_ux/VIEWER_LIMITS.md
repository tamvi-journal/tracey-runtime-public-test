# Viewer Limits

This UX is a viewer, not an actor.

It may display:
- route
- gate
- evidence
- verification
- completion status
- open loops
- next hint

It must not:
- execute actions
- approve actions
- write files
- mutate memory
- write to external knowledge store
- send messages
- schedule cron
- call network/API
- override MainBrain final synthesis
- turn evidence into truth
