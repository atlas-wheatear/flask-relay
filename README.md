# Flask Relay

This is the relay server component for the system, serving as the download point for _.ogg_ files generated by
the flite-flask synthesiser component. It represents the other publicly-facing container, besides the Godot
engine game-server instance itself.

## Issues

### Security

This is currently **_very_** insecure, _e.g._:

- The root POST method is available to the wider internet, potentially allowing an attacker to replace a file
with a malicious payload, given prior knowledge of the UUID access point using which other players will download.
- The secure filename facility is untested, and may (potentially) allow a
[path traversal attack](https://owasp.org/www-community/attacks/Path_Traversal)

### (Lack of) Testing

Tests need to be added, prefarably with a CI/CD solution.

### Performance

- Ogg files are never deleted once uploaded - they can be a maximum of 1MB in size, but this will eventually
add up
    - This could _hypothetically_ be fixed using a system like [Redis](https://redis.io/) for cache
