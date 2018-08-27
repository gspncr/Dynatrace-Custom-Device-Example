# Dynatrace Custom Device Example
This example required an API token to write custom metrics to your environment, and the fully qualified tenant address (SaaS: `https://tenant.live.dynatrace.com` and for managed: `https://{{ManagedURI}}/e/{{Environment}}`)

This is tested with Python 3.7.

This script is logging at `INFO` level. Set the logging info on line 5.

This script is resolving by DNS `gallery.gspncr.com`, either set this or if your machine has no DNS resolver to public DNS it is fine to use a private, or set to any IP address. This is just for demonstration purposes.